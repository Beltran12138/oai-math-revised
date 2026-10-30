# Task: add newly found items to automatically collected notes

Two AI agents independently looked for new context about the papers of result family {FAMILY} of the OpenAI math release, following the same instructions and the same format. Their files contain only new items. Add these to the existing notes, one `AGENT_NOTES.md` per paper.

Inputs, per paper folder:

{INPUTS}

The format and rules are in {REPO}/docs/AGENT_NOTES_FORMAT.md; read it first.

Rules:
- Copy every existing item, byte for byte, in its section and in its order. Never change, shorten, move or drop an existing item, even if a new item supersedes it.
- Add new items at the end of their section, replacing `- None found.` there if it is the only line.
- Use only items that appear in the inputs. Do not add sources, do not search the web, do not change URLs.
- Two new items with the same URL or about the same work become one: keep the most informative and precise description. Skip a new item if an existing item already covers the same work or says the same thing.
- Put each item in the right section as defined in the format doc. Drop new items that are bare catalogue or registry listings, descriptions of the search process, items that only repeat what existing items say, and items whose description judges the paper's correctness in the agent's own voice (rephrase neutrally if the source itself says it).
- "Possibly relevant literature": at most 5 items in total; add new ones only below that limit.
- Keep math in `$...$` as given. Keep descriptions to one or two sentences.
- Header line: `Collected by an AI agent ({MODELS}) on {DATE}.`

Write the result for each folder to `{OUT}/<folder>/AGENT_NOTES.md` (all seven sections, empty ones `- None found.`). Reply with one line per folder: number of new items added.
