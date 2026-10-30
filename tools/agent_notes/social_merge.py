"""Fold social-media candidates (from social.py) into the existing AGENT_NOTES.md files.

    python3 tools/agent_notes/social_merge.py --work DIR --social a.json b.json ... [--families ...] [--jobs 6]

For each family with candidates, a Claude Code run without web access (restricted
to Read/Write in its own job directory) gets copies of the current notes and the
candidate posts with their text, and writes updated notes (SOCIAL.md). Results are
validated and land in DIR/social_merged/<folder>/AGENT_NOTES.md; finalize.py-style
copying into the repository is done separately with --apply.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import shutil
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "site"))
from catalog import load  # noqa: E402
from check import problems_in  # noqa: E402
from removed import additive, blocked_urls, canonical, urls_in  # noqa: E402
from run_all import CLAUDE_MODEL, log, publish, recover_from_log, run  # noqa: E402
from social import oembed_text  # noqa: E402


def merge_family(fam, cands: list[dict], work: Path, blocked: dict[str, set[str]]) -> bool:
    marker = work / "done" / f"social-{fam.num}"
    if marker.exists():
        return True
    job = work / "jobs" / f"social-{fam.num}-{time.strftime('%Y%m%d-%H%M%S')}"
    out = job / "out"
    out.mkdir(parents=True)
    inputs = []
    for f in fam.papers:
        dst = job / "notes" / f / "AGENT_NOTES.md"
        dst.parent.mkdir(parents=True)
        shutil.copy(ROOT / "preprints" / f / "AGENT_NOTES.md", dst)
        inputs.append(f"- `{f}`: {dst}")
    (job / "docs").mkdir()
    shutil.copy(ROOT / "docs" / "AGENT_NOTES_FORMAT.md", job / "docs")
    lines = [f"- {c['source']}: {c['title']} <{c['url']}>\n  {c['context']}" for c in cands]
    text = (HERE / "SOCIAL.md").read_text(encoding="utf-8")
    for k, v in {"FAMILY": fam.num, "FAMILY_TITLE": fam.title, "INPUTS": "\n".join(inputs),
                 "REPO": str(job), "CANDIDATES": "\n".join(lines), "OUT": str(out)}.items():
        text = text.replace("{" + k + "}", v)
    cmd = ["claude", "-p", "--model", CLAUDE_MODEL, "--effort", "medium", "--restricted", "--no-session-persistence",
           "--tools", "Read,Glob,Write", "--allowedTools", "Read,Glob,Write", "--permission-mode", "acceptEdits"]
    logfile = work / "logs" / f"social-{fam.num}.log"
    t = time.time()
    code = run(cmd, job, logfile, text)
    recover_from_log(logfile, out, fam.papers)
    problems = []
    for f in fam.papers:  # the merge may only add items, never drop or edit existing ones
        result = out / f / "AGENT_NOTES.md"
        new = result.read_text(encoding="utf-8") if result.is_file() else ""
        text, lost, dropped = additive(new, (job / "notes" / f / "AGENT_NOTES.md").read_text(encoding="utf-8"), blocked[f])
        if result.is_file():
            result.write_text(text, encoding="utf-8")
        problems += [f"{f}: existing item changed or dropped: {l[:80]}" for l in lost]
        if dropped:
            log(work, f"social {fam.num}: {f}: dropped {len(dropped)} repeated or removed items")
    if not problems:
        problems = publish(out, work / "social_merged", fam.papers) if code == 0 else [f"exit {code}"]
    ok = not problems
    log(work, f"social {fam.num}: {'ok' if ok else 'FAILED: ' + '; '.join(problems)[:300]} ({time.time() - t:.0f}s)")
    if ok:
        marker.touch()
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--social", nargs="+", default=[])
    ap.add_argument("--families", nargs="*")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--apply", action="store_true", help="copy validated results into preprints/")
    args = ap.parse_args()
    work = Path(args.work).resolve()
    for d in ("done", "logs", "jobs", "social_merged"):
        (work / d).mkdir(parents=True, exist_ok=True)
    _, families, _ = load(ROOT)
    blocked = blocked_urls(ROOT, families)

    if args.apply:
        # Only the selected families (default: all) are copied.
        nums = [f.zfill(3) for f in args.families] if args.families else sorted(families)
        selected = {s for n in nums for s in families[n].papers}
        n = 0
        for f in sorted((work / "social_merged").glob("*/AGENT_NOTES.md")):
            if f.parent.name not in selected:
                continue
            if not problems_in(f) and (ROOT / "preprints" / f.parent.name).is_dir():
                shutil.copy(f, ROOT / "preprints" / f.parent.name / "AGENT_NOTES.md")
                n += 1
        print(f"{n} files copied into preprints/")
        return

    by_folder: dict[str, list] = {}
    for path in args.social:
        for folder, cands in json.loads(Path(path).read_text()).items():
            have = {c["url"] for c in by_folder.get(folder, [])}
            by_folder.setdefault(folder, []).extend(c for c in cands if c["url"] not in have)
    nums = [f.zfill(3) for f in args.families] if args.families else sorted(families)
    todo = []
    for num in nums:
        fam = families[num]
        cands = {c["url"]: c for s in fam.papers for c in by_folder.get(s, [])}
        for c in cands.values():  # X candidates from runs before oEmbed verification
            if c["source"].startswith("X") and not c["context"].startswith("Post text:"):
                text = oembed_text(c["url"])
                c["context"] = f"Post text: {text} | Grok's summary: {c['context']}" if text is not None else None
        if not cands:
            continue
        known = set().union(*(urls_in((ROOT / "preprints" / s / "AGENT_NOTES.md").read_text(encoding="utf-8")) | blocked[s]
                              for s in fam.papers))
        cands = [c for c in cands.values() if c["context"] is not None and canonical(c["url"]) not in known]
        if cands:
            todo.append((fam, cands))
    log(work, f"social merge: {len(todo)} families with candidates")
    with cf.ThreadPoolExecutor(args.jobs) as ex:
        results = list(ex.map(lambda a: merge_family(*a, work, blocked), todo))
    log(work, f"social merge finished: {sum(results)}/{len(todo)} ok")


if __name__ == "__main__":
    main()
