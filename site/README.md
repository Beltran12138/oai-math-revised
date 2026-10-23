# Website

The website is generated from the files already in this repository:

- `overview.tex`: disciplines and the order of result families
- `CONTENTS.md`: families, paper titles and abstracts
- `preprints/*/README.md`: dates, BibTeX, version notes, withdrawals
- `preprints/*/NOTES.md` and `preprints/*/AGENT_NOTES.md`: notes shown on paper pages. The "Contributions" section of NOTES.md (format in [AGENTS.md](../AGENTS.md)) also feeds the "Recent activity" box on the front page, `/activity/` and the Atom feed `activity.xml`; the build prints a warning for lines it cannot parse and shows them unformatted on the paper page.
- `lean/docs/*.md`: links to Lean scope notes
- `site/data/external_links.csv`: links to other sites per paper (shown under "Elsewhere"). Collected on 2026-10-20 from VibeMathed (dataset API), Hexagon (works whose bibliography cites the paper; human understanding "all" or "some"), Palomar (entries that formalize or adapt the paper), whataifound, Readable Intelligence and Lance Fortnow's expositions. Emergent Mind family pages are linked by URL pattern. Edit by hand or regenerate; do not scrape Emergent Mind (their terms forbid it).

It is rebuilt and deployed to GitHub Pages by `.github/workflows/pages.yml` on every push to `main` that touches these files.

## Building locally

```sh
pip install jinja2 markdown nh3
python3 site/build.py --pdfs link      # symlinks PDFs instead of copying them
python3 -m http.server -d _site 8000   # then open http://localhost:8000
```

`--pdfs none` skips the PDFs entirely; the default `--pdfs copy` is what the deployment uses.

## Layout

- `catalog.py` reads the repository and builds the paper/family/discipline data
- `build.py` renders the pages
- `templates/` page templates (Jinja2)
- `static/` CSS, JavaScript and a copy of KaTeX 0.16.11 (MIT, see `static/katex/LICENSE`)
