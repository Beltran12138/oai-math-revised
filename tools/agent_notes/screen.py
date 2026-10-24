#!/usr/bin/env python3
"""Screen existing AGENT_NOTES.md items for ones that add little for readers.

    screen.py run WORK [--batch 12] [--jobs 6] [--only FOLDER ...]
    screen.py report WORK            # writes WORK/drops.md for review
    screen.py apply WORK [--skip ID ...]   # IDs as shown in drops.md

`run` sends the notes of a batch of papers to `claude -p` with SCREEN.md and
stores the proposed drops per batch, each with its folder and line text
(drops of an item with identical copies are marked ambiguous and never applied)
(resumable: a batch is reused only for exactly the same papers). `apply`
removes those lines by exact text, so drops whose line changed or is already
gone are reported and skipped; a section left empty gets "- None found.".
Nothing is removed without a review of drops.md.
"""
import argparse
import concurrent.futures as cf
import hashlib
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
            out.append(f"#{iid} {line[2:]}")
        out.append("")
    return "\n".join(out)


def screen(batch, path: Path):
    prompt = (HERE / "SCREEN.md").read_text(encoding="utf-8").replace("{NOTES}", render(batch))
    cmd = ["claude", "-p", "--model", MODEL, "--no-session-persistence", "--tools", ""]
    try:
        r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=1800)
        m = re.search(r"^\[.*\]", r.stdout.strip(), re.S)
        if r.returncode or not m:
            raise ValueError(f"exit {r.returncode}: {(r.stdout + r.stderr)[-300:]}")
        reply = json.loads(m.group(0))
    except (subprocess.TimeoutExpired, ValueError) as e:  # JSONDecodeError is a ValueError
        return f"{path.name}: failed: {e}"
    where = {iid: (folder, line) for folder, items in batch for iid, _, _, line in items}
    lines = [(folder, line) for folder, items in batch for *_, line in items]
    drops = [{"id": d["id"], "folder": where[d["id"]][0], "line": where[d["id"]][1], "reason": str(d.get("reason", "")),
              "ambiguous": lines.count(where[d["id"]]) > 1}  # identical copies: never applied, remove by hand
             for d in reply if isinstance(d, dict) and d.get("id") in where]
    data = {"folders": [folder for folder, _ in batch], "drops": drops}
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return f"{path.name}: {len(drops)} drops"


def all_drops(work: Path):
    """{(folder, line): (id, reason)} over all stored batches."""
    drops = {}
    for f in sorted(work.glob("batch-*.json")):
        for d in json.loads(f.read_text(encoding="utf-8"))["drops"]:
            reason = d["reason"] + (" [AMBIGUOUS: identical copies, not applied]" if d.get("ambiguous") else "")
            drops.setdefault((d["folder"], d["line"]), (d["id"], reason))
            if d.get("ambiguous"):  # once ambiguous, always ambiguous
                drops[(d["folder"], d["line"])] = (d["id"], reason)
    return drops


def key(folder, line):
    """Stable review ID of an item (positional IDs are only used inside a batch prompt)."""
    return hashlib.sha1(f"{folder}\n{line}".encode()).hexdigest()[:10]


def batch_path(work: Path, batch):
    key = hashlib.sha1("\n".join(folder for folder, _ in batch).encode()).hexdigest()[:12]
    return work / f"batch-{key}.json"


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
        todo = [(b, batch_path(a.work, b)) for b in batches]
        todo = [(b, p) for b, p in todo if not p.exists()]
        with cf.ThreadPoolExecutor(a.jobs) as ex:
            for msg in ex.map(lambda t: screen(*t), todo):
                print(msg, flush=True)
        return

    drops = all_drops(a.work)
    if a.cmd == "report":
        out, total = [], 0
        for folder, items in papers:
            hits = [(sec, line) for _, sec, _, line in items if (folder, line) in drops]
            if hits:
                out.append(f"## {folder}\n")
                for sec, line in hits:
                    reason = drops[(folder, line)][1]
                    out.append(f"- `{key(folder, line)}` *{sec}* — {reason}\n  {line[2:]}")
                    total += 1
                out.append("")
        (a.work / "drops.md").write_text(f"# Proposed drops: {total}\n\n" + "\n".join(out), encoding="utf-8")
        print(f"{total} proposed drops in {a.work / 'drops.md'}")
        return

    wanted = {k for k, (_, reason) in drops.items()
              if key(*k) not in a.skip and (not a.only or k[0] in a.only) and "[AMBIGUOUS" not in reason}
    removed, found = 0, set()
    for folder, items in papers:
        count = {}
        for _, _, _, line in items:
            count[line] = count.get(line, 0) + 1
        for line in {l for _, _, _, l in items if count[l] > 1 and (folder, l) in wanted}:
            print(f"ambiguous ({count[line]} identical items), remove by hand: {folder}: {line[:100]}")
            found.add((folder, line))
        hit = {n for _, _, n, line in items if (folder, line) in wanted and count[line] == 1}
        if not hit:
            continue
        found |= {(folder, line) for _, _, n, line in items if n in hit}
        path = ROOT / "preprints" / folder / "AGENT_NOTES.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        keep = [l for n, l in enumerate(lines) if n not in hit]
        fixed = []
        for i, l in enumerate(keep):  # fill sections left empty
            fixed.append(l)
            nxt = next((x for x in keep[i + 1:] if x.strip()), "## ")
            if l.startswith("## ") and nxt.startswith("## "):
                fixed.append(NONE)
        path.write_text("\n".join(fixed) + "\n", encoding="utf-8")
        removed += len(hit)
    for folder, line in sorted(wanted - found):
        print(f"not found (changed or already removed), skipped: {folder}: {line[:100]}")
    print(f"removed {removed} items")


if __name__ == "__main__":
    sys.exit(main())
