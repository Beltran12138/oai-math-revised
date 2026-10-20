# Website

The website is generated from the files already in this repository:

- `overview.tex`: disciplines and the order of result families
- `CONTENTS.md`: families, paper titles and abstracts
- `preprints/*/README.md`: dates, BibTeX, version notes, withdrawals
- `preprints/*/NOTES.md` and `preprints/*/AGENT_NOTES.md`: notes shown on paper pages
- `lean/docs/*.md`: links to Lean scope notes

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
