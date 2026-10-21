"""Check AGENT_NOTES.md files: format (docs/AGENT_NOTES_FORMAT.md) and that every link resolves.

    python3 tools/agent_notes/check.py FILE_OR_DIR [...] [--no-links]

Prints one line per problem and exits non-zero if there are any.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

SECTIONS = [
    "Follow-up works",
    "Expert comments and discussion",
    "Formalization",
    "Related prior literature mentioned by others",
    "Possibly relevant literature (found by the agent, not checked)",
    "Digests and expositions",
    "News and blogs",
]
HEADER = re.compile(r"\A# Automatically collected context\n\nCollected by an AI agent \(.+\) on \d{4}-\d{2}-\d{2}\.\n")
LINK = re.compile(r"\]\((https?://[^)\s]+)\)")
# Sites that refuse automated requests but are fine in a browser.
NO_CHECK = ("x.com", "twitter.com", "science.org", "sciencedirect.com", "jstor.org", "wiley.com", "forbes.com")


def problems_in(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    out = []
    if not HEADER.match(text):
        out.append("header: expected '# Automatically collected context' and 'Collected by an AI agent (...) on YYYY-MM-DD.'")
    found = re.findall(r"^## (.+)$", text, flags=re.M)
    if found != SECTIONS:
        out.append(f"sections: expected {SECTIONS}, got {found}")
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        title, _, body = block.partition("\n")
        items = [l for l in body.splitlines() if l.strip()]
        if not items:
            out.append(f"{title}: empty (write '- None found.')")
        for line in items:
            if not line.startswith("- "):
                out.append(f"{title}: not a list item: {line[:80]}")
            elif line != "- None found." and not LINK.search(line):
                out.append(f"{title}: item without a link: {line[:80]}")
        if title == SECTIONS[4] and len(items) > 7:  # docs say 5; older pilot files have up to 7
            out.append(f"{title}: {len(items)} items (keep it to about 5)")
        if re.search(r"(?i)\bsearched\b|\bno results\b", body):
            out.append(f"{title}: mentions the search process; remove")
    return out


def status(url: str) -> int | str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (link check; github.com/mathcommunity/oai-math-revised)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:  # DNS, TLS, timeout
        return type(e).__name__


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--no-links", action="store_true")
    args = ap.parse_args()
    files = []
    for p in map(Path, args.paths):
        files += sorted(p.rglob("AGENT_NOTES.md")) if p.is_dir() else [p]

    bad = 0
    urls: dict[str, list[Path]] = {}
    for f in files:
        for msg in problems_in(f):
            print(f"{f}: {msg}")
            bad += 1
        for url in LINK.findall(f.read_text(encoding="utf-8")):
            urls.setdefault(url, []).append(f)
    if not args.no_links:
        todo = [u for u in urls if not any(h in u for h in NO_CHECK)]
        with concurrent.futures.ThreadPoolExecutor(8) as ex:
            for url, code in zip(todo, ex.map(status, todo)):
                if code != 200:
                    for f in urls[url]:
                        print(f"{f}: link {code}: {url}")
                    bad += 1
    print(f"{len(files)} files, {len(urls)} links, {bad} problems", file=sys.stderr)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
