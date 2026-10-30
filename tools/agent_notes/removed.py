"""Keep automated updates of AGENT_NOTES.md additive.

Items were removed from these files on purpose (the screening pass, expert
feedback, hand edits). `blocked_urls` reads those removals from the git history,
so that a later run does not bring them back; `additive` validates a run's output
against the current file.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from check import LINK


def canonical(url: str) -> str:
    """Same page, same string: scheme, www, trailing slash, X's domains, arXiv abs/pdf/versions."""
    u = re.sub(r"^http://", "https://", url.strip()).rstrip("/")
    u = re.sub(r"^https://www\.", "https://", u).replace("https://twitter.com/", "https://x.com/")
    u = re.sub(r"^(https://x\.com/[^?#]+)[?#].*$", r"\1", u)
    m = re.match(r"https://arxiv\.org/(?:abs|pdf)/([^?#]+?)(?:v\d+)?(?:\.pdf)?$", u)
    return f"https://arxiv.org/abs/{m.group(1)}" if m else u


def urls_in(text: str) -> set[str]:
    return {canonical(u) for u in LINK.findall(text)}


def blocked_urls(root: Path, families: dict) -> dict[str, set[str]]:
    """folder -> URLs once in the notes of its family that are not in its notes now."""
    log = subprocess.run(["git", "-C", str(root), "log", "-p", "--unified=0", "--format=", "--",
                          "preprints/*/AGENT_NOTES.md"], capture_output=True, text=True, check=True).stdout
    removed: dict[str, set[str]] = {}
    folder = ""
    for line in log.splitlines():
        if m := re.match(r"--- a/preprints/(.+)/AGENT_NOTES\.md$", line):
            folder = m.group(1)
        elif line.startswith("-") and not line.startswith("---") and folder:
            removed.setdefault(folder, set()).update(urls_in(line))
    out = {}
    for fam in families.values():
        gone = set().union(*(removed.get(s, set()) for s in fam.papers))
        for s in fam.papers:
            notes = root / "preprints" / s / "AGENT_NOTES.md"
            out[s] = gone - urls_in(notes.read_text(encoding="utf-8") if notes.is_file() else "")
    return out


def additive(new: str, old: str, blocked: set[str]) -> tuple[str, list[str], list[str]]:
    """Return (text without unwanted new items, existing items missing from it, dropped new items).

    A new item is dropped if its main link is already in the notes or any link is blocked.
    """
    old_lines = old.splitlines()
    have, kept, dropped = urls_in(old), [], []
    for line in new.splitlines():
        links = [canonical(u) for u in LINK.findall(line)]
        if line.startswith("- ") and links and line not in old_lines:
            if links[0] in have or blocked.intersection(links):
                dropped.append(line)
                continue
            have.add(links[0])
        kept.append(line)
    lost = [l for l in old_lines if l.startswith("- [") and l not in kept]
    return "\n".join(kept) + "\n", lost, dropped
