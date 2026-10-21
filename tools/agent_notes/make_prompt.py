"""Fill PROMPT.md for one result family.

    python3 tools/agent_notes/make_prompt.py 102 --candidates candidates.json --out DIR --model "Claude Opus 5.5"
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "site"))
from catalog import load  # noqa: E402


def make_prompt(family: str, candidates: dict, out: str, model: str, repo: Path = ROOT) -> str:
    _, families, papers = load(ROOT)
    fam = families[family]
    folders = "\n".join(f"- `{s}`: {papers[s].title}" for s in fam.papers)
    cands = []
    for s in fam.papers:
        for c in candidates.get(s, []):
            cands.append(f"- for `{s}`: {c['source']}: [{c['title']}]({c['url']}). {c['context'][:300]}")
    # Hand-collected links shown on the website (expositions, rewrites).
    with open(ROOT / "site" / "data" / "external_links.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["paper"] in fam.papers and row["source"] in ("Lance Fortnow", "Readable Intelligence"):
                cands.append(f"- for `{row['paper']}`: {row['source']}: [{row['title']}]({row['url']})")
    text = (Path(__file__).parent / "PROMPT.md").read_text(encoding="utf-8")
    for key, value in {
        "FAMILY": family, "FAMILY_TITLE": fam.title, "REPO": str(repo), "FOLDERS": folders,
        "CANDIDATES": "\n".join(cands) or "- None.", "OUT": out, "MODEL": model,
        "DATE": datetime.date.today().isoformat(),
    }.items():
        text = text.replace("{" + key + "}", value)
    return text


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("family")
    ap.add_argument("--candidates", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", required=True)
    args = ap.parse_args()
    print(make_prompt(args.family.zfill(3), json.loads(Path(args.candidates).read_text()), args.out, args.model))
