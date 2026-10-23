"""Build the static website into _site/.

    python3 site/build.py [--out _site] [--pdfs copy|link|none]

--pdfs link symlinks the PDFs instead of copying them (fast local previews);
--pdfs none skips them.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import hashlib
import html
import posixpath
import json
import os
import re
import shutil
from pathlib import Path
from urllib.parse import quote, urlencode

import markdown
import nh3
from jinja2 import Environment, FileSystemLoader, pass_context, select_autoescape

from catalog import _date_from_slug, load

ROOT = Path(__file__).resolve().parent.parent
SITE_SRC = Path(__file__).resolve().parent
REPO = os.environ.get("SITE_REPO", "mathcommunity/oai-math-revised")
BRANCH = os.environ.get("SITE_BRANCH", "main")
GITHUB = f"https://github.com/{REPO}"
SITE_URL = os.environ.get("SITE_URL", "https://mathcommunity.github.io/oai-math-revised").rstrip("/")
UPSTREAM = "https://github.com/openai/math"


# --- text helpers -----------------------------------------------------------

_MATH = re.compile(r"(\$\$.+?\$\$|\$[^$\n]+?\$)", re.S)

ALLOWED_TAGS = {
    "a", "abbr", "b", "blockquote", "br", "code", "del", "em", "h2", "h3", "h4", "h5", "h6", "hr",
    "i", "img", "li", "ol", "p", "pre", "small", "strong", "sub", "sup", "table", "tbody", "td",
    "th", "thead", "tr", "ul",
}
ALLOWED_ATTRS = {"a": {"href", "title"}, "img": {"src", "alt", "title"}, "h2": {"id"}, "h3": {"id"},
                 "h4": {"id"}, "h5": {"id"}, "h6": {"id"}, "th": {"align"}, "td": {"align"}}


def clean(fragment: str) -> str:
    """Allowlist-sanitize an HTML fragment (contributed notes, catalogue text)."""
    return nh3.clean(fragment, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS,
                     url_schemes={"http", "https", "mailto"}, link_rel=None)


def resolve(target: str, base: str, root: str) -> str:
    """Map a relative link in a repository file under `base` to a site or GitHub URL."""
    if re.match(r"[a-z][a-z0-9+.-]*:|#", target, flags=re.I):
        return target
    path, _, frag = target.partition("#")
    frag = f"#{frag}" if frag else ""
    full = posixpath.normpath(posixpath.join(base, path)) if path else base
    if full.startswith("../") or full == "..":
        return "#"
    m = re.fullmatch(r"preprints/([^/]+)(?:/(?:README\.md|NOTES\.md|AGENT_NOTES\.md|[^/]+\.pdf))?/?", full)
    if m:  # another paper (or its main files): link to its page on this site
        return f"{root}/papers/{m.group(1)}/{frag}"
    return f"{GITHUB}/blob/{BRANCH}/{full}{frag}"


def render_md(text: str, slug: str | None = None, root: str = ".") -> str:
    """Markdown to sanitized HTML, leaving $..$ math untouched for KaTeX."""
    stash: list[str] = []

    def keep(m):
        stash.append(m.group(0))
        return f"\x00{len(stash) - 1}\x00"

    md = markdown.Markdown(extensions=["tables", "fenced_code", "footnotes", "sane_lists", "toc"],
                           extension_configs={"toc": {"slugify": lambda v, sep: slugify(v)}})
    out = md.convert(_MATH.sub(keep, text))
    out = re.sub(r"\x00(\d+)\x00", lambda m: html.escape(stash[int(m.group(1))]), out)
    return _rewrite_links(clean(out), f"preprints/{slug}" if slug else ".", root)


def _rewrite_links(out: str, base: str, root: str) -> str:
    def fix(m):
        url = resolve(html.unescape(m.group(2)), base, root)
        if m.group(1) == "src":  # images must come from the raw file, not GitHub's page view
            url = url.replace(f"{GITHUB}/blob/", f"https://raw.githubusercontent.com/{REPO}/", 1)
        return f'{m.group(1)}="{html.escape(url)}"'

    return re.sub(r'\b(href|src)="([^"]*)"', fix, out)


def inline_links(text: str, root: str = ".") -> str:
    """Catalogue text (titles, summaries, abstracts) as sanitized HTML.

    CONTENTS.md embeds Markdown links ([label](target)) in its HTML; turn
    them into anchors first.
    """

    def link(m):
        return f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>'

    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    return _rewrite_links(clean(out), ".", root)


def render_notes(text: str, slug: str | None = None, root: str = ".") -> str:
    """Render a NOTES.md-style file, dropping headings with nothing under them."""
    # A top-level title ("# Notes") would repeat the page's section heading.
    text = re.sub(r"^# .*\n?", "", text, flags=re.M)
    kept = []
    for block in re.split(r"^(?=#{2,6} )", text, flags=re.M):
        head, _, body = block.partition("\n") if block.startswith("#") else ("", "", block)
        if re.fullmatch(r"\s*(-\s*None found\.?\s*)?", body, flags=re.I):
            continue
        kept.append(block)
    return render_md("".join(kept), slug, root)


def split_agent_notes(text: str | None) -> tuple[str, str] | None:
    """Pull the "Collected by an AI agent (tool) on date." line out of AGENT_NOTES.md."""
    if text is None:
        return None
    m = re.search(r"^Collected by an AI agent \(([^)]*)\) on (\d{4}-\d{2}-\d{2})\..*$", text, flags=re.M)
    if not m:
        return "", text
    return f"{m.group(1)}, {m.group(2)}", text[:m.start()] + text[m.end():]


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def split_readme(extra: str) -> tuple[str, str]:
    """Separate the README's "Version note" section from the rest."""
    parts = re.split(r"^(?=## )", extra, flags=re.M)
    note = "".join(p for p in parts if p.startswith("## Version note"))
    rest = "".join(p for p in parts if not p.startswith("## Version note"))
    return re.sub(r"\A## Version note\s*", "", note).strip(), rest.strip()


def search_text(text: str) -> str:
    """Lower-case text without tags, TeX commands, $ or accents, for search."""
    import unicodedata

    text = plain(inline_links(text))
    text = re.sub(r"\\[a-zA-Z]+|[${}^_\\]", " ", text).replace("--", "-")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", text).lower().strip()


def plain(text: str) -> str:
    """Strip tags and entities, for search and <title>."""
    return html.unescape(re.sub(r"<[^>]+>", "", text)).strip()


# --- links into GitHub ------------------------------------------------------

NOTES_TEMPLATE = """## Contributions

## Follow-up works

## Constructive comments / reviews

## People interested in meeting to work on digestion
"""


def long_date(iso: str) -> str:
    """2026-10-20 -> October 20, 2026 (the format used elsewhere on the site)."""
    d = datetime.date.fromisoformat(iso)
    return f"{d:%B} {d.day}, {d.year}"


def activity_entries(papers: dict) -> list[dict]:
    """All "Contributions" lines from NOTES.md files, newest first."""
    out = []
    host = SITE_URL.split("://")[-1].split("/")[0]
    for slug, p in papers.items():
        seen: dict[tuple, int] = {}
        for c in p.contributions:
            # Feed id from paper, date and people (stable when the text is edited),
            # numbered if the same people have several entries on one day.
            who = tuple(h or n for h, n in c.people)
            seen[(c.date, who)] = k = seen.get((c.date, who), 0) + 1
            key = hashlib.sha1("|".join(who).encode()).hexdigest()[:10]
            out.append({"slug": slug, "paper": p, "c": c, "id": f"tag:{host},2026:{slug}/{c.date}/{key}/{k}"})
    out.sort(key=lambda e: (e["c"].date, e["slug"], e["c"].order), reverse=True)
    return out


def issue_url(template: str, slug: str, title: str) -> str:
    tag = {"problem": "problem", "reference": "reference", "interest": "interested"}[template]
    params = {"template": f"{template}.yml", "title": f"[{tag}] {title}", "paper": slug}
    return f"{GITHUB}/issues/new?{urlencode(params, quote_via=quote)}"


def notes_edit_url(slug: str, exists: bool) -> str:
    if exists:
        return f"{GITHUB}/edit/{BRANCH}/preprints/{slug}/NOTES.md"
    q = urlencode({"filename": "NOTES.md", "value": NOTES_TEMPLATE}, quote_via=quote)
    return f"{GITHUB}/new/{BRANCH}/preprints/{slug}?{q}"


def issues_search_url(slug: str) -> str:
    return f"{GITHUB}/issues?{urlencode({'q': f'is:issue \"{slug}\"'}, quote_via=quote)}"


# --- build ------------------------------------------------------------------

def build(out: Path, pdf_mode: str) -> None:
    disciplines, families, papers = load(ROOT)

    env = Environment(loader=FileSystemLoader(SITE_SRC / "templates"),
                      autoescape=select_autoescape(["html", "xml"]), trim_blocks=True, lstrip_blocks=True)
    env.globals.update(
        GITHUB=GITHUB, UPSTREAM=UPSTREAM, BRANCH=BRANCH,
        BUILD_DATE=datetime.date.today().isoformat(),
        SITE_ISSUE=f"{GITHUB}/issues/new?" + urlencode({"labels": "site", "title": "[site] "}, quote_via=quote),
    )
    env.filters["md"] = pass_context(lambda ctx, t, slug=None: render_md(t, slug, ctx["root"]))
    env.filters["notes"] = pass_context(lambda ctx, t, slug=None: render_notes(t, slug, ctx["root"]))
    env.filters["inline_md"] = pass_context(lambda ctx, t, slug=None: re.sub(
        r"\A<p>(.*)</p>\Z", r"\1", render_md(t, slug, ctx["root"]).strip(), flags=re.S))
    env.filters["long_date"] = long_date
    env.filters["unbullet"] = lambda line: re.sub(r"\A[-*]\s+", "", line)
    env.filters["slugify"] = slugify
    env.filters["plain"] = plain
    env.filters["html"] = pass_context(lambda ctx, t: inline_links(t, ctx["root"]))

    if out.exists():
        shutil.rmtree(out)
    (out / "papers").mkdir(parents=True)
    shutil.copytree(SITE_SRC / "static", out / "assets")

    withdrawn = sorted((p for p in papers.values() if p.status == "withdrawn"), key=lambda p: p.title)

    def chain_older(slug):  # all earlier editions, newest first
        out = []
        for o in papers[slug].older:
            out += [o] + chain_older(o)
        return out

    def newest(slug):
        while papers[slug].newer:
            slug = papers[slug].newer
        return slug

    earlier = {slug: chain_older(slug) for slug in papers}

    # Links to other sites, curated in site/data/external_links.csv.
    elsewhere: dict[str, list[dict]] = {}
    with open(SITE_SRC / "data" / "external_links.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            elsewhere.setdefault(row["paper"], []).append(row)
    for d in disciplines:
        d.n_papers = sum(len(families[n].papers) for n in d.families)

    def write(path: Path, template: str, **ctx):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(env.get_template(template).render(**ctx), encoding="utf-8")

    activity = activity_entries(papers)
    for slug, p in papers.items():
        for line in p.contribution_problems:
            print(f"warning: preprints/{slug}/NOTES.md: Contributions line not understood: {line}")

    write(out / "index.html", "index.html", root=".", disciplines=disciplines,
          families=families, papers=papers, withdrawn=withdrawn, earlier=earlier, activity=activity[:3],
          n_with_notes=sum(p.has_notes for p in papers.values()),
          n_earlier=sum(p.status == "superseded" for p in papers.values()))
    write(out / "contribute" / "index.html", "contribute.html", root="..")
    write(out / "activity" / "index.html", "activity.html", root="..", activity=activity)
    feed = env.get_template("activity.xml").render(
        root=SITE_URL, activity=activity[:50], SITE_URL=SITE_URL,
        updated=(activity[0]["c"].date if activity else datetime.date.today().isoformat()))
    (out / "activity.xml").write_text(feed, encoding="utf-8")

    index = []
    for slug, p in papers.items():
        fam = families.get(p.family) if p.family else None
        current = newest(slug)
        siblings = [papers[s] for s in fam.papers if s not in (slug, current)] if fam else []
        version_note, other_readme = split_readme(p.readme_extra) if p.status != "withdrawn" else ("", "")
        # Issues and notes for an earlier edition belong to the current one.
        target = papers[current]
        links = {
            "report": issue_url("problem", current, plain(target.title)),
            "reference": issue_url("reference", current, plain(target.title)),
            "interest": issue_url("interest", current, plain(target.title)),
            "notes_edit": notes_edit_url(current, target.notes_md is not None),
            "issues": issues_search_url(current),
            "source": f"{GITHUB}/tree/{BRANCH}/preprints/{slug}",
            "upstream": f"{UPSTREAM}/tree/main/preprints/{slug}",
            "upstream_pdf": f"{UPSTREAM}/blob/main/preprints/{slug}/{p.pdf}",
            "history": f"{GITHUB}/commits/{BRANCH}/preprints/{slug}",
        }
        write(out / "papers" / slug / "index.html", "paper.html", root="../..", p=p, fam=fam,
              siblings=siblings, papers=papers, links=links, current=current,
              version_note=version_note, other_readme=other_readme,
              original_date=_date_from_slug(slug), agent=split_agent_notes(p.agent_notes_md),
              elsewhere=elsewhere.get(slug, []),
              contributions=sorted(p.contributions, key=lambda c: (c.date, c.order), reverse=True))
        if p.pdf and pdf_mode != "none":
            src, dst = ROOT / "preprints" / slug / p.pdf, out / "papers" / slug / p.pdf
            if pdf_mode == "link":
                dst.symlink_to(src)
            else:
                shutil.copyfile(src, dst)
        index.append({
            "s": slug,
            "t": search_text(p.title),
            "f": p.family or "",
            "ft": search_text(fam.title) if fam else "",
            "x": " ".join(search_text(t) for t in (
                p.abstract, fam.summary if fam else "", p.notes_md or "", p.discipline or "")),
            "d": p.discipline or "",
            "st": p.status,
            "n": int(p.has_notes),
            "l": int(bool(fam and fam.lean_doc)),
        })

    (out / "assets" / "index.json").write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")),
                                                encoding="utf-8")
    (out / ".nojekyll").touch()
    print(f"built {len(papers)} paper pages into {out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "_site"))
    ap.add_argument("--pdfs", choices=["copy", "link", "none"], default="copy")
    args = ap.parse_args()
    build(Path(args.out), args.pdfs)
