"""Screen the items a run adds, before they reach the repository.

    python3 tools/agent_notes/screen_new.py WORK [--jobs 5]          # writes WORK/new_drops.json
    python3 tools/agent_notes/screen_new.py WORK --apply [--keep ID ...]  # removes them from WORK/merged

Compares WORK/merged with preprints/. Items from sites that publish an AI-generated
entry for most of the release are held back without asking a model: they work as
catalogues, which the notes leave out. Everything else goes to `claude -p` with
SCREEN_NEW.md, one family at a time, with the family's existing items for
comparison. Items already in the repository are not touched.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "site"))
from catalog import load  # noqa: E402
from check import LINK, normalize  # noqa: E402
from removed import sections  # noqa: E402

MASS = ("aiprovedwhat.com", "binaryverseai.com", "closedform.nishachay.tech", "erdosproblemaday.com", "explainx.ai",
        "lowrank.github.io/latent-seminar", "openmaths.org", "postcutoff.com")


def item_id(line: str) -> str:
    return hashlib.sha1(line.encode()).hexdigest()[:10]


def new_items(work: Path, families: dict) -> dict[str, list[dict]]:
    """family -> new items, one per distinct line, with the folders holding it."""
    out: dict[str, dict] = {}
    for num, fam in families.items():
        for s in fam.papers:
            merged = work / "merged" / s / "AGENT_NOTES.md"
            notes = ROOT / "preprints" / s / "AGENT_NOTES.md"
            if not merged.is_file() or not notes.is_file():
                continue
            old = sections(notes.read_text(encoding="utf-8"))
            for title, items in sections(merged.read_text(encoding="utf-8")).items():
                for line in items:
                    if line not in old.get(title, []):
                        it = out.setdefault(num, {}).setdefault(item_id(line), {"id": item_id(line), "section": title, "line": line, "folders": []})
                        it["folders"].append(s)
    return {n: list(v.values()) for n, v in out.items()}


def screen(num: str, fam, items: list[dict]) -> list[dict]:
    blocks = []
    for s in fam.papers:
        new = [f"#{i['id']} ({i['section']}) {i['line']}" for i in items if s in i["folders"]]
        if new:
            old = sections((ROOT / "preprints" / s / "AGENT_NOTES.md").read_text(encoding="utf-8"))
            existing = [l[:300] for ls in old.values() for l in ls]
            blocks.append(f"## Paper {s}\n\nExisting items:\n" + ("\n".join(existing) or "(none)") + "\n\nNew items:\n" + "\n".join(new))
    prompt = (HERE / "SCREEN_NEW.md").read_text(encoding="utf-8").replace("{ITEMS}", "\n\n".join(blocks))
    r = subprocess.run(["claude", "-p", "--model", "claude-opus-5-5", "--effort", "medium", "--tools", "", "--no-session-persistence"],
                       input=prompt, capture_output=True, text=True, timeout=1800, cwd="/tmp")
    m = re.search(r"\[.*\]", r.stdout, flags=re.S)
    if r.returncode or not m:
        raise RuntimeError(f"{num}: exit {r.returncode}: {r.stdout[-200:]}")
    known = {i["id"] for i in items}
    return [d for d in json.loads(m.group(0)) if d.get("id") in known]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("work")
    ap.add_argument("--jobs", type=int, default=5)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--keep", nargs="*", default=[], help="IDs to keep after reviewing new_drops.json")
    args = ap.parse_args()
    work = Path(args.work).resolve()
    path = work / "new_drops.json"
    _, families, _ = load(ROOT)

    if args.apply:
        drops = json.loads(path.read_text())
        n = 0
        for d in drops:
            if d["id"] in args.keep:
                continue
            for s in d["folders"]:
                f = work / "merged" / s / "AGENT_NOTES.md"
                repo = (ROOT / "preprints" / s / "AGENT_NOTES.md").read_text(encoding="utf-8").splitlines()
                if d["line"] in repo:
                    print(f"kept, already in the repository: {d['line'][:80]}", file=sys.stderr)
                    continue
                lines = f.read_text(encoding="utf-8").splitlines()
                f.write_text(normalize("\n".join(l for l in lines if l != d["line"]) + "\n"), encoding="utf-8")
                n += 1
        print(f"{n} lines removed from {work / 'merged'}")
        return

    items = new_items(work, families)
    drops = []
    for its in items.values():
        drops += [{**i, "reason": "mass-produced AI entries"} for i in its if any(h in u for u in LINK.findall(i["line"])[:1] for h in MASS)]
    held = {d["id"] for d in drops}
    todo = {n: [i for i in its if i["id"] not in held] for n, its in items.items()}
    todo = {n: its for n, its in todo.items() if its}

    failed: list[str] = []

    def job(n):
        try:
            found = screen(n, families[n], todo[n])
        except Exception as e:  # one family's failure should not lose the others
            print(f"FAILED {e}", file=sys.stderr)
            failed.append(n)
            return []
        by_id = {i["id"]: i for i in todo[n]}
        print(f"{n}: {len(found)} of {len(todo[n])} dropped", file=sys.stderr)
        return [{**by_id[d["id"]], "reason": d.get("reason", "")} for d in found]

    with cf.ThreadPoolExecutor(args.jobs) as ex:
        for r in ex.map(job, todo):
            drops += r
    if failed:  # unscreened items must not pass as screened
        sys.exit(f"screen failed for families {' '.join(failed)}; nothing written, rerun")
    path.write_text(json.dumps(drops, indent=1, ensure_ascii=False))
    print(f"{sum(map(len, items.values()))} new items, {len(held)} held back, {len(drops) - len(held)} marked by the screen", file=sys.stderr)


if __name__ == "__main__":
    main()
