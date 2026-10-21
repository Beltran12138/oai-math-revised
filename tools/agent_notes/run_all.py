"""Collect AGENT_NOTES.md for many families with Claude Code and Codex, then merge.

    python3 tools/agent_notes/run_all.py --work DIR --candidates candidates.json [--families 001 002 ...]
                                          [--claude-jobs 5] [--codex-jobs 5] [--merge-jobs 3]

For each family, a Claude Code run (`claude -p`) and a Codex run (`codex exec`)
research the family independently (PROMPT.md). When both have succeeded, a
low-effort Claude run merges their outputs, together with any existing
AGENT_NOTES.md in the repository (CONSOLIDATE.md). Results land in
DIR/merged/<folder>/AGENT_NOTES.md; nothing in the repository is written.

Safety: every job runs in its own fresh directory holding a copy of just the
files it needs. Claude jobs run with --restricted (no shell, file tools confined
to that directory); Codex jobs run in its workspace-write sandbox (writes
confined to the job directory, no network except its own web search). Outputs
are validated (format) before they are published and marked done.

Resumable: stages with a DIR/done/<stage>-<family> marker are skipped. If a
usage limit or repeated failures are detected, the affected engine stops
launching new jobs; rerun later to continue.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime
import fcntl
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "site"))
from catalog import load  # noqa: E402
from check import problems_in  # noqa: E402
from make_prompt import make_prompt  # noqa: E402

CLAUDE_MODEL, CLAUDE_NAME = "claude-opus-5-5", "Claude Opus 5.5"
CODEX_MODEL, CODEX_NAME = "gpt-6-astra", "GPT-6 Astra"
TIMEOUT = 45 * 60
LIMIT_RE = re.compile(r"(?i)usage limit|rate.?limit|limit (?:reached|exceeded)|quota|too many requests|\b429\b|credit balance")
MAX_CONSECUTIVE_FAILURES = 4

lock = threading.Lock()
stopped: dict[str, str] = {}  # engine -> reason; "claude" also stops merges
failures = {"claude": 0, "codex": 0}
results: list[tuple[str, str, bool]] = []


def log(work: Path, msg: str) -> None:
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} {msg}"
    with lock:
        print(line, flush=True)
        with open(work / "run.log", "a") as f:
            f.write(line + "\n")


def run(cmd: list[str], cwd: Path, logfile: Path, stdin: str) -> int:
    """Run in its own process group; on timeout kill the whole group."""
    with open(logfile, "w") as out:
        p = subprocess.Popen(cmd, cwd=cwd, stdin=subprocess.PIPE, stdout=out, stderr=subprocess.STDOUT,
                             text=True, start_new_session=True)
        try:
            p.communicate(stdin, timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            os.killpg(p.pid, signal.SIGKILL)
            p.wait()
            return -1
        return p.returncode


def note_failure(engine: str, work: Path, logfile: Path, code: int) -> None:
    tail = logfile.read_text(errors="ignore")[-4000:] if logfile.exists() else ""
    with lock:
        failures[engine] += 1
        if LIMIT_RE.search(tail):
            stopped.setdefault(engine, f"usage/rate limit message in {logfile.name}")
        elif failures[engine] >= MAX_CONSECUTIVE_FAILURES:
            stopped.setdefault(engine, f"{failures[engine]} consecutive failures (last exit {code})")
    if engine in stopped:
        log(work, f"STOPPING {engine}: {stopped[engine]}")


def snapshot(job: Path, fam, folders: list[str]) -> Path:
    """Copy the files an agent needs (no PDFs) into job/repo."""
    repo = job / "repo"
    for f in folders:
        src = ROOT / "preprints" / f
        shutil.copytree(src, repo / "preprints" / f, ignore=shutil.ignore_patterns("*.pdf", "*.png", "*.jpg"))
    lean = ROOT / "lean" / "docs" / f"{fam.num}.md"
    if lean.exists():
        (repo / "lean" / "docs").mkdir(parents=True)
        shutil.copy(lean, repo / "lean" / "docs" / lean.name)
    (repo / "docs").mkdir()
    shutil.copy(ROOT / "docs" / "AGENT_NOTES_FORMAT.md", repo / "docs")
    (repo / "CONTENTS.md").write_text(f"**{fam.num}. {fam.title}.** {fam.summary}\n", encoding="utf-8")
    return repo


def publish(src: Path, dst: Path, folders: list[str]) -> list[str]:
    """Validate the files in src and copy them to dst; return problems (nothing is copied if any)."""
    problems = []
    for f in folders:
        p = src / f / "AGENT_NOTES.md"
        problems += [f"{f}: missing"] if not p.is_file() else [f"{f}: {m}" for m in problems_in(p)]
    if not problems:
        for f in folders:
            (dst / f).mkdir(parents=True, exist_ok=True)
            shutil.copy(src / f / "AGENT_NOTES.md", dst / f / "AGENT_NOTES.md")
    return problems


def research(engine: str, fam, work: Path, cands: dict) -> bool:
    marker = work / "done" / f"{engine}-{fam.num}"
    if marker.exists():
        return True
    if engine in stopped:
        return False
    job = work / "jobs" / f"{engine}-{fam.num}-{time.strftime('%Y%m%d-%H%M%S')}"
    out = job / "out"
    out.mkdir(parents=True)
    repo = snapshot(job, fam, fam.papers)
    prompt = make_prompt(fam.num, cands, str(out), CLAUDE_NAME if engine == "claude" else CODEX_NAME, repo=repo)
    logfile = work / "logs" / f"{engine}-{fam.num}.log"
    t = time.time()
    if engine == "claude":
        cmd = ["claude", "-p", "--model", CLAUDE_MODEL, "--restricted", "--no-session-persistence",
               "--tools", "Read,Glob,Grep,Write,WebSearch,WebFetch", "--permission-mode", "acceptEdits"]
    else:
        cmd = ["codex", "exec", "--model", CODEX_MODEL, "-c", "model_reasoning_effort=high",
               "-c", 'web_search="live"', "--sandbox", "workspace-write", "-C", str(job),
               "--skip-git-repo-check", "-"]
    code = run(cmd, job, logfile, prompt)
    problems = publish(out, work / engine, fam.papers) if code == 0 else [f"exit {code}"]
    ok = not problems
    log(work, f"{engine} {fam.num}: {'ok' if ok else 'FAILED: ' + '; '.join(problems)[:300]} ({time.time() - t:.0f}s)")
    if ok:
        marker.touch()
        with lock:
            failures[engine] = 0
    else:
        note_failure(engine, work, logfile, code)
    return ok


def merge(fam, work: Path) -> bool:
    marker = work / "done" / f"merge-{fam.num}"
    if marker.exists():
        return True
    if "claude" in stopped:
        return False
    job = work / "jobs" / f"merge-{fam.num}-{time.strftime('%Y%m%d-%H%M%S')}"
    out = job / "out"
    out.mkdir(parents=True)
    inputs = []
    for f in fam.papers:
        inputs.append(f"- `{f}`:")
        for engine in ("claude", "codex"):
            dst = job / "inputs" / engine / f / "AGENT_NOTES.md"
            dst.parent.mkdir(parents=True)
            shutil.copy(work / engine / f / "AGENT_NOTES.md", dst)
            inputs.append(f"  - {engine}: {dst}")
        existing = ROOT / "preprints" / f / "AGENT_NOTES.md"
        if existing.is_file():
            dst = job / "inputs" / "existing" / f / "AGENT_NOTES.md"
            dst.parent.mkdir(parents=True)
            shutil.copy(existing, dst)
            inputs.append(f"  - existing (older run): {dst}")
    (job / "docs").mkdir()
    shutil.copy(ROOT / "docs" / "AGENT_NOTES_FORMAT.md", job / "docs")
    text = (HERE / "CONSOLIDATE.md").read_text(encoding="utf-8")
    for k, v in {"FAMILY": fam.num, "INPUTS": "\n".join(inputs), "REPO": str(job), "OUT": str(out),
                 "MODELS": f"{CLAUDE_NAME} and {CODEX_NAME}", "DATE": datetime.date.today().isoformat()}.items():
        text = text.replace("{" + k + "}", v)
    cmd = ["claude", "-p", "--model", CLAUDE_MODEL, "--effort", "low", "--restricted", "--no-session-persistence",
           "--tools", "Read,Glob,Write", "--permission-mode", "acceptEdits"]
    logfile = work / "logs" / f"merge-{fam.num}.log"
    t = time.time()
    code = run(cmd, job, logfile, text)
    problems = publish(out, work / "merged", fam.papers) if code == 0 else [f"exit {code}"]
    ok = not problems
    log(work, f"merge {fam.num}: {'ok' if ok else 'FAILED: ' + '; '.join(problems)[:300]} ({time.time() - t:.0f}s)")
    if ok:
        marker.touch()
    else:
        note_failure("claude", work, logfile, code)
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--candidates", required=True)
    ap.add_argument("--families", nargs="*")
    ap.add_argument("--claude-jobs", type=int, default=5)
    ap.add_argument("--codex-jobs", type=int, default=5)
    ap.add_argument("--merge-jobs", type=int, default=3)
    args = ap.parse_args()
    work = Path(args.work).resolve()
    for d in ("done", "logs", "jobs", "claude", "codex", "merged"):
        (work / d).mkdir(parents=True, exist_ok=True)
    lockfile = open(work / ".lock", "w")
    try:
        fcntl.flock(lockfile, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        sys.exit(f"another run is using {work}")

    _, families, _ = load(ROOT)
    nums = list(dict.fromkeys(f.zfill(3) for f in args.families)) if args.families else sorted(families)
    cands = json.loads(Path(args.candidates).read_text())
    pools = {"claude": cf.ThreadPoolExecutor(args.claude_jobs), "codex": cf.ThreadPoolExecutor(args.codex_jobs)}
    merger = cf.ThreadPoolExecutor(args.merge_jobs)
    merges: list[cf.Future] = []

    def safe(fn, stage, num, *a):
        try:
            ok = fn(*a)
        except Exception as e:  # never let one job take down the run
            log(work, f"{stage} {num}: ERROR {type(e).__name__}: {e}")
            ok = False
        with lock:
            results.append((stage, num, ok))
        return ok

    def schedule(num):
        fam = families[num]
        futs = {e: pools[e].submit(safe, research, e, num, e, fam, work, cands) for e in pools}
        once = []

        def when_done(_):
            with lock:
                if once or not all(f.done() for f in futs.values()):
                    return
                once.append(True)
            if all(f.result() for f in futs.values()):
                merges.append(merger.submit(safe, merge, "merge", num, fam, work))
            else:
                log(work, f"merge {num}: waiting (research incomplete); rerun to continue")

        for f in futs.values():
            f.add_done_callback(when_done)

    log(work, f"start: {len(nums)} families")
    for num in nums:
        schedule(num)
    for p in pools.values():
        p.shutdown(wait=True)
    time.sleep(1)  # let the last callbacks submit their merges
    merger.shutdown(wait=True)

    failed = sorted(f"{s}-{n}" for s, n, ok in results if not ok)
    done = sum(1 for n in nums if (work / "done" / f"merge-{n}").exists())
    log(work, f"finished: {done}/{len(nums)} families merged; {len(failed)} failed stages"
              + (f": {' '.join(failed[:40])}" if failed else "") + (f"; stopped: {stopped}" if stopped else ""))
    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
