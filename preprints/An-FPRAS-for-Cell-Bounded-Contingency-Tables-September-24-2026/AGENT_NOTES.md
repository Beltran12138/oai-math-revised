# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [EcoDataLab, *contingency-tables: Open research on bounded contingency tables*](https://github.com/EcoDataLab/contingency-tables) (GitHub repository, October 2026). Describes itself as auditing and improving OpenAI result #115, noting that the companion FPRAS "covers cell bounds and structural zeros"; it also reports a separate Lean development (1511 named declarations) for a bounded sampler, whose strict Comparator verification it says "remains open". [AI-generated per source] [family-level]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Sampling and counting contingency tables with arbitrary margins: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/115.md) (lean/docs/115.md, 2026). The release's scope statement for the FPRAS: binary-encoded margins and bounds, zero bounds allowed, relative error $\varepsilon$ with probability $1-\delta$, output zero when no table exists, and polynomial running time on every random tape; it shares the Comparator file `ContingencyTables.lean` with the companion sampling results. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Miller, Harrison, *Exact Enumeration and Sampling of Matrices with Specified Margins*](https://arxiv.org/abs/1104.0323) (arXiv:1104.0323, 2011). Exact dynamic-programming counting of integer and binary matrices with given margins, polynomial when column sums are bounded; relevant to the account of exact versus approximate counting in Section 1.1, which does not cite it.

## Digests and expositions
- [Latent Seminar, *Contingency tables: exact sampling and relative counting*](https://lowrank.github.io/latent-seminar/OpenAI-Math/115-contingency-tables) (Latent Seminar, 2026-10-07). Explains the sampling manuscript's rare residual correction and the counting manuscript's forest coordinates and multiplicity corrections, stating that it reviews selected sections rather than independently verifying the full proofs. [family-level]

## News and blogs
- None found.
