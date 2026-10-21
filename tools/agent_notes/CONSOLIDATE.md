# Task: merge automatically collected notes

Two AI agents independently collected context for the papers of result family {FAMILY} of the OpenAI math release, following the same instructions and the same format. Merge their outputs into one `AGENT_NOTES.md` per paper.

Inputs, per paper folder (some may be missing; an existing older file may also be present):

{INPUTS}

The format and rules are in {REPO}/docs/AGENT_NOTES_FORMAT.md; read it first.

Merging rules:
- Use only items that appear in the inputs. Do not add sources, do not search the web, do not change URLs.
- Two items with the same URL, or about the same work (e.g. arXiv abstract page and PDF, or two versions), become one item: keep the most informative and precise description, and keep a second URL only if it adds something (e.g. a published version).
- Put each item in the right section as defined in the format doc. Drop items that are bare catalogue or registry listings (Emergent Mind, VibeMathed, whataifound, kisonecat, Pitt catalogue, readable-intelligence pages without a readable version), descriptions of the search process, and items whose description judges the paper's correctness in the agent's own voice (rephrase neutrally if the source itself says it).
- "Possibly relevant literature": at most 5 items; prefer those tied to a specific claim of the paper.
- Keep math in `$...$` as given. Keep descriptions to one or two sentences.
- Header line: `Collected by an AI agent ({MODELS}) on {DATE}.`

Write the result for each folder to `{OUT}/<folder>/AGENT_NOTES.md` (all seven sections, empty ones `- None found.`). Reply with one line per folder: number of items kept and dropped.
