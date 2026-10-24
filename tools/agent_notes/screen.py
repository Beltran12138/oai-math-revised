#!/usr/bin/env python3
"""Screen existing AGENT_NOTES.md items for ones that add little for readers.

    screen.py run WORK [--batch 12] [--jobs 6] [--only FOLDER ...]
    screen.py report WORK            # writes WORK/drops.md for review
    screen.py apply WORK [--skip ID ...]

`run` sends the notes of a batch of papers to `claude -p` with SCREEN.md and
stores the proposed drops per batch (resumable). `apply` removes the proposed
items, checking each line still matches; a section left empty gets
"- None found.". Nothing is removed without a review of drops.md.
"""
import argparse
import concurrent.futures as cf
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
MODEL = "claude-opus-5-5"
NONE = "- None found."


def load(only=None):
    """Return [(folder, [(id, section, lineno, line)])] with ids '<paper>.<item>'."""
    papers = []
    folders = sorted(p.parent.name for p in (ROOT / "preprints").glob("*/AGENT_NOTES.md"))
    for pi, folder in enumerate(folders):
        if only and folder not in only:
            continue
        items, section = [], None
        lines = (ROOT / "preprints" / folder / "AGENT_NOTES.md").read_text(encoding="utf-8").splitlines()
        for n, line in enumerate(lines):
            if line.startswith("## "):
                section = line[3:]
            elif line.startswith("- [") and section:
                items.append((f"{pi}.{len(items)}", section, n, line))
        if items:
            papers.append((folder, items))
    return papers


def render(batch):
    out = []
    for folder, items in batch:
        out.append(f"### Paper: {folder}")
        section = None
        for iid, sec, _, line in items:
            if sec != section:
                out.append(f"## {sec}")
                section = sec
            out.append(f"[{iid}] {line[2:]}")
        out.append("")
    return "\n".join(out)


def screen(batch, path: Path):
    prompt = (HERE / "SCREEN.md").read_text(encoding="utf-8").replace("{NOTES}", render(batch))
    cmd = ["claude", "-p", "--model", MODEL, "--no-session-persistence", "--tools", ""]
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=1800)
    m = re.search(r"\[.*\]", r.stdout, re.S)
    if r.returncode or not m:
        return f"{path.name}: failed (exit {r.returncode}): {(r.stdout + r.stderr)[-300:]}"
    ids = {iid for _, items in batch for iid, *_ in items}
    drops = [d for d in json.loads(m.group(0)) if d.get("id") in ids]
    path.write_text(json.dumps(drops, ensure_ascii=False, indent=1), encoding="utf-8")
    return f"{path.name}: {len(drops)} drops"


def all_drops(work: Path):
    drops = {}
    for f in sorted(work.glob("batch-*.json")):
        for d in json.loads(f.read_text(encoding="utf-8")):
            drops[d["id"]] = d["reason"]
    return drops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["run", "report", "apply"])
    ap.add_argument("work", type=Path)
    ap.add_argument("--batch", type=int, default=12)
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--skip", nargs="*", default=[])
    a = ap.parse_args()
    a.work.mkdir(parents=True, exist_ok=True)
    papers = load(a.only)

    if a.cmd == "run":
        batches = [papers[i:i + a.batch] for i in range(0, len(papers), a.batch)]
        todo = [(b, a.work / f"batch-{b[0][1][0][0].split('.')[0]}.json") for b in batches]
        todo = [(b, p) for b, p in todo if not p.exists()]
        with cf.ThreadPoolExecutor(a.jobs) as ex:
            for msg in ex.map(lambda t: screen(*t), todo):
                print(msg, flush=True)
        return

    drops = all_drops(a.work)
    if a.cmd == "report":
        out, total = [], 0
        for folder, items in papers:
            hits = [(iid, sec, line) for iid, sec, _, line in items if iid in drops]
            if hits:
                out.append(f"## {folder}\n")
                for iid, sec, line in hits:
                    out.append(f"- `{iid}` *{sec}* — {drops[iid]}\n  {line[2:]}")
                    total += 1
                out.append("")
        (a.work / "drops.md").write_text(f"# Proposed drops: {total}\n\n" + "\n".join(out), encoding="utf-8")
        print(f"{total} proposed drops in {a.work / 'drops.md'}")
        return

    removed = 0
    for folder, items in papers:
        hit = {n: line for iid, _, n, line in items if iid in drops and iid not in a.skip}
        if not hit:
            continue
        path = ROOT / "preprints" / folder / "AGENT_NOTES.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        assert all(lines[n] == line for n, line in hit.items()), f"{folder} changed since screening"
        keep = [l for n, l in enumerate(lines) if n not in hit]
        fixed = []
        for i, l in enumerate(keep):  # fill sections left empty
            fixed.append(l)
            nxt = next((x for x in keep[i + 1:] if x.strip()), "## ")
            if l.startswith("## ") and nxt.startswith("## "):
                fixed.append(NONE)
        path.write_text("\n".join(fixed) + "\n", encoding="utf-8")
        removed += len(hit)
    print(f"removed {removed} items")


if __name__ == "__main__":
    sys.exit(main())
