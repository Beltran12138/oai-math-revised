"""Collect candidate links for AGENT_NOTES.md from structured sources (no AI involved).

    python3 tools/agent_notes/prepass.py --cache DIR --out candidates.json

Fetches (and caches in DIR):
  - VibeMathed dataset (https://vibemathed.com/api/dataset)
  - whataifound entries (github.com/yigitisik/whataifound, data/entries.json)
  - Hexagon works and their bibliographies (https://hexagonmath.org/api/v1)
  - Palomar registry entries (https://data.palomar-registry.org/api/v1/results)
  - google-deepmind/formal-conjectures (shallow clone, grepped for openai/math)

Every source is searched for links into openai/math (or this fork) that name a
preprint folder; each hit becomes a candidate for that folder. The output maps
folder -> list of {source, title, url, context}.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "site"))
from catalog import load  # noqa: E402

FOLDER_RE = re.compile(r"github\.com/(?:openai/math|mathcommunity/oai-math-revised)/(?:blob|tree|raw)/[^/\s\"']+/preprints/([A-Za-z0-9()_.,'+-]+)")


def fetch(url: str, path: Path, refresh: bool = False) -> Path:
    if path.exists() and not refresh:
        return path
    req = urllib.request.Request(url, headers={"User-Agent": "oai-math-revised prepass (github.com/mathcommunity/oai-math-revised)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        path.write_bytes(r.read())
    time.sleep(0.3)
    return path


def folders_in(obj) -> set[str]:
    return set(FOLDER_RE.findall(json.dumps(obj) if not isinstance(obj, str) else obj))


def vibemathed(cache: Path):
    data = json.loads(fetch("https://vibemathed.com/api/dataset", cache / "vibemathed.json").read_text())
    for p in data["problems"]:
        for folder in folders_in(p):
            yield folder, {"source": "VibeMathed", "title": p.get("name", ""),
                           "url": f"https://vibemathed.com/problem/{p['slug']}",
                           "context": (p.get("resultNote") or p.get("statement") or "")[:600]}


def whataifound(cache: Path):
    url = "https://raw.githubusercontent.com/yigitisik/whataifound/main/data/entries.json"
    for e in json.loads(fetch(url, cache / "whataifound.json").read_text()):
        for folder in folders_in(e):
            yield folder, {"source": "whataifound", "title": e.get("title", ""),
                           "url": f"https://whataifound.org/finding/{e['id']}",
                           "context": " ".join(str(e.get(k, "")) for k in ("claim", "detail", "caveats"))[:800]}


def hexagon(cache: Path):
    (cache / "hexagon").mkdir(exist_ok=True)
    works, cursor, page = [], None, 1
    while True:
        url = "https://hexagonmath.org/api/v1/works?limit=100" + (f"&cursor={cursor}" if cursor else "")
        d = json.loads(fetch(url, cache / "hexagon" / f"list-{page}.json").read_text())
        works += d["works"]
        cursor = d["page"].get("next_cursor")
        if not d["page"].get("has_more") or not cursor:
            break
        page += 1
    for w in works:
        ident = w["identifier"]
        try:
            full = json.loads(fetch(f"https://hexagonmath.org/api/v1/works/{ident}", cache / "hexagon" / f"{ident}.json").read_text())["work"]
        except Exception:
            continue  # the API occasionally returns 500 for single works
        for folder in folders_in(full.get("bibliography", [])) | folders_in(full.get("abstract", "")):
            yield folder, {"source": "Hexagon", "title": full["title"],
                           "url": f"https://hexagonmath.org/abs/{ident}v{full.get('versionNumber', 1)}",
                           "context": f"authorship: {full.get('authorshipMode')}; human understanding: {full.get('humanUnderstanding')}. "
                                      + (full.get("abstract") or "")[:500]}


def palomar(cache: Path):
    (cache / "palomar").mkdir(exist_ok=True)
    entries, cursor, page = [], None, 1
    while True:
        url = "https://data.palomar-registry.org/api/v1/results" + (f"?cursor={cursor}" if cursor else "")
        d = json.loads(fetch(url, cache / "palomar" / f"list-{page}.json").read_text())
        entries += d["entries"]
        cursor = d.get("next")
        if not cursor or not d["entries"]:
            break
        page += 1
    for e in entries:
        try:
            full = json.loads(fetch(f"https://data.palomar-registry.org/{e['path']}", cache / "palomar" / Path(e["path"]).name).read_text())
        except Exception:
            continue
        for src in full.get("provenance", {}).get("mathematical_sources", []):
            if src.get("relationship") not in ("formalizes", "adapts"):
                continue
            for folder in folders_in(src):
                yield folder, {"source": "Palomar", "title": full.get("title", ""),
                               "url": f"https://palomar-registry.org/entry?id={full['id']}&version={full.get('version', 1)}",
                               "context": f"Lean formalization ({src['relationship']} this paper). " + (full.get("abstract") or "")[:500]}


def formal_conjectures(cache: Path):
    repo = cache / "formal-conjectures"
    if not repo.exists():
        subprocess.run(["git", "clone", "-q", "--depth", "1", "https://github.com/google-deepmind/formal-conjectures", str(repo)], check=True)
    out = subprocess.run(["git", "-C", str(repo), "grep", "-n", "-E", "openai/math|oai-math-revised"], capture_output=True, text=True).stdout
    for line in out.splitlines():
        path, lineno, text = line.split(":", 2)
        for folder in folders_in(text):
            yield folder, {"source": "formal-conjectures",
                           "title": path,
                           "url": f"https://github.com/google-deepmind/formal-conjectures/blob/main/{path}#L{lineno}",
                           "context": text.strip()[:300]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    cache = Path(args.cache)
    cache.mkdir(parents=True, exist_ok=True)

    _, families, papers = load(ROOT)
    out: dict[str, list] = {}
    for name, gen in [("vibemathed", vibemathed), ("whataifound", whataifound), ("hexagon", hexagon),
                      ("palomar", palomar), ("formal-conjectures", formal_conjectures)]:
        n = 0
        try:
            for folder, item in gen(cache):
                if folder in papers and item not in out.setdefault(folder, []):
                    out[folder].append(item)
                    n += 1
        except Exception as e:  # one broken source should not stop the others
            print(f"{name}: FAILED ({e})", file=sys.stderr)
            continue
        print(f"{name}: {n} candidates", file=sys.stderr)
    Path(args.out).write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(f"{sum(map(len, out.values()))} candidates for {len(out)} folders", file=sys.stderr)


if __name__ == "__main__":
    main()
