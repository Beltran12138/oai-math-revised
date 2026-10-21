# AGENT_NOTES.md format

`preprints/<paper>/AGENT_NOTES.md` holds context about a paper that was collected automatically by AI tools. It is shown on the paper's page on the website, collapsed and marked as unreviewed. Human-written notes go in `NOTES.md` instead.

```
# Automatically collected context

Collected by an AI agent (<tool / model>) on <YYYY-MM-DD>.

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
- Every URL must have been opened successfully during the run. Never cite a search engine's summary.
- Neutral descriptions; no judgement of correctness by the agent. Quotes at most 25 words.
- "Possibly relevant literature": at most 5 items, each tied to a specific claim of the paper and not already in its bibliography.
- "News and blogs": articles and posts that discuss this paper. Not catalogue or registry listings (those are linked from the website automatically), and not a list of where the agent searched.
- Empty sections: `- None found.`
- No private or paywalled content, no personal information beyond public names.
