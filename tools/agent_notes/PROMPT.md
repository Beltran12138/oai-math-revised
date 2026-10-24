# Task: collect context for one result family of the OpenAI math release

You are collecting publicly available context about the papers of result family {FAMILY} ("{FAMILY_TITLE}") from the OpenAI math release (github.com/openai/math, 6 October 2026; 719 AI-generated manuscripts in 372 families). The output is shown, marked as automatically collected and unreviewed, on the community site mathcommunity.github.io/oai-math-revised. Mathematicians in the area will read it, so precision matters more than volume.

Repository (read-only for you): {REPO}. The family's papers are these folders under `preprints/`:

{FOLDERS}

For each folder, read `README.md`, the abstract and introduction of the TeX in `build/`, and its bibliography (`.bib` or `\begin{thebibliography}`). The family summary is in `CONTENTS.md` (search for `**{FAMILY}.`); Lean scope notes, if any, are in `lean/docs/{FAMILY}.md`.

## Candidates already found automatically

These links point to the papers from structured sources (VibeMathed, whataifound, Hexagon, Palomar, formal-conjectures). Use them as leads: open each, and include it only if it fits a section below. Do not list a bare catalogue or registry page as an item; use what it contains (for example an expert comment it quotes, with the original link if it opens). VibeMathed and whataifound entries are already linked from the website and their notes are AI-assisted: do not list them as expert comments or digests.

{CANDIDATES}

## Where to look next

Search for follow-up work, expositions, expert comments and formalizations about these specific papers:
- arXiv (search the titles and key terms of the main results; papers from October 2026 onwards that mention OpenAI or cite the release), hexagonmath.org (`https://hexagonmath.org/search?q=...`)
- blogs and their comment threads: Terence Tao, Gil Kalai, galoisrepresentations.org (Persiflage), Xena, Shtetl-Optimized, Lance Fortnow (and github.com/fortnow/AI-Papers), proofsandprompts.com; Hacker News (hn.algolia.com)
- github.com/google-deepmind/formal-conjectures issues and PRs; the Palomar registry
- readable-intelligence.com (readable rewrites of some papers)
- news coverage that discusses these papers specifically

Keep it efficient: about 15-30 web searches/fetches for the family. Never cite a search engine's summary; only pages you opened. Comments about the whole release go in only if they address these papers specifically.

## Output

Write one file per folder at `{OUT}/<folder>/AGENT_NOTES.md`. If you cannot write files, print each file's full contents between the lines `=== FILE <folder> ===` and `=== END ===`.

Exact format (all seven sections, in this order; empty sections contain `- None found.`):

```
# Automatically collected context

Collected by an AI agent ({MODEL}) on {DATE}.

## Follow-up works
## Comments and discussion
## Formalization
## Related prior literature mentioned by others
## Possibly relevant literature (found by the agent, not checked)
## Digests and expositions
## News and blogs
```

Rules:
- One item per line: `- [Author(s) or who/where, *Title*](URL) (ID or venue, date). One neutral sentence on how it relates to this paper.` Optional tags at the end: `[AI-generated per source]`, `[cites earlier version]`, `[family-level]`.
- An item about the whole family goes into the file of every paper it concerns, tagged `[family-level]`.
- Every URL must have been opened successfully by you. Never invent citations, identifiers, dates or quotes.
- Neutral descriptions. Do not judge correctness yourself. Quotes at most 25 words.
- "Possibly relevant literature": at most 5 items, each tied to a specific claim of the paper and not already in its bibliography (check!).
- "Formalization": Lean or other formal developments of these results, including the release's own (`lean/docs/{FAMILY}.md`, link it on github.com/mathcommunity/oai-math-revised) and independent ones.
- "News and blogs": articles and posts that discuss these papers. Not catalogue or registry listings, and not a description of where you searched.
- Comments must add something for a researcher in the area (an assessment with reasons, an explanation, a pointer, a correction, a specific question); skip comments that only restate the claim. No prediction markets, polls or votes.
- No private or paywalled content; no personal information beyond public names.
- Every list item must contain a link. Do not explain absences ("there is no Lean development ..."); just write `- None found.`

When done, reply with 2-4 sentences per paper: what you found and what a specialist should look at first.
