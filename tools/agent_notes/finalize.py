"""Copy merged AGENT_NOTES.md files into the repository, dropping items with dead links.

    python3 tools/agent_notes/finalize.py --work DIR [--dry-run]

An item is dropped only if every link in it is definitely gone (HTTP 404 or 410);
sites that block automated requests (403, 429, timeouts) are kept.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from check import LINK, NO_CHECK, normalize, problems_in, status  # noqa: E402

DEAD = {404, 410}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    files = sorted((Path(args.work) / "merged").glob("*/AGENT_NOTES.md"))
    texts = {f: f.read_text(encoding="utf-8") for f in files}
    urls = sorted({u for t in texts.values() for u in LINK.findall(t) if not any(h in u for h in NO_CHECK)})
    with cf.ThreadPoolExecutor(16) as ex:
        codes = dict(zip(urls, ex.map(status, urls)))
    dead = {u for u, c in codes.items() if c in DEAD}
    print(f"{len(files)} files, {len(urls)} links checked, {len(dead)} dead", file=sys.stderr)

    written = dropped = 0
    for f, text in texts.items():
        folder = f.parent.name
        target = ROOT / "preprints" / folder
        if not target.is_dir():
            print(f"skip {folder}: no such folder in preprints/", file=sys.stderr)
            continue
        lines = []
        for line in text.splitlines():
            links = LINK.findall(line)
            if line.startswith("- ") and links and all(u in dead for u in links):
                dropped += 1
                continue
            lines.append(line)
        out = normalize("\n".join(lines) + "\n")
        tmp = f.with_suffix(".final")
        tmp.write_text(out, encoding="utf-8")
        problems = problems_in(tmp)
        if problems:
            print(f"skip {folder}: {problems}", file=sys.stderr)
            continue
        if not args.dry_run:
            (target / "AGENT_NOTES.md").write_text(out, encoding="utf-8")
        written += 1
    print(f"{written} files written{' (dry run)' if args.dry_run else ''}, {dropped} items with dead links dropped",
          file=sys.stderr)


if __name__ == "__main__":
    main()
