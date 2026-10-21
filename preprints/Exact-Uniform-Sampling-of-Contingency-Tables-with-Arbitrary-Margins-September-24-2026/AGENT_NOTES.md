# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [EcoDataLab, *contingency-tables: Open research on bounded contingency tables*](https://github.com/EcoDataLab/contingency-tables) (GitHub repository, October 2026). Describes itself as auditing and improving OpenAI result #115, including a separate Lean development (1511 named declarations) with a bounded sampler of total variation at most $2^{-h}$; it notes that "the source claim of exact expected-polynomial sampling concerns ordinary tables" and does not transfer it to the cell-bounded setting. [AI-generated per source] [family-level]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Sampling and counting contingency tables with arbitrary margins: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/115.md) (lean/docs/115.md, 2026). The release's scope statement: the exact sampler terminates almost surely, outputs feasible tables, and gives each table exactly the uniform limiting probability; it also covers the bounded-time $2^{-k}$ total-variation sampler and the companion cell-bounded FPRAS, all in the shared Comparator file `ContingencyTables.lean`. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- [Cryan, Dyer, Randall, *Approximately Counting Integral Flows and Cell-Bounded Contingency Tables*](https://homepages.inf.ed.ac.uk/mcryan/cdr-sicomp.pdf) (SIAM J. Comput. 39 (2010)). Cited in third-party listings of this family as the source naming unrestricted cell-bounded counting as open; it is cited in the companion FPRAS paper but not in this one. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [Miller, Harrison, *Exact Enumeration and Sampling of Matrices with Specified Margins*](https://arxiv.org/abs/1104.0323) (arXiv:1104.0323, 2011). A dynamic-programming exact counter and exactly uniform sampler for integer and binary matrices with given margins, polynomial when column sums are bounded; a point of comparison for the paper's unconditional exact uniform sampler (Theorem 1.1(ii)).

## Digests and expositions
- [Latent Seminar, *Contingency tables: exact sampling and relative counting*](https://lowrank.github.io/latent-seminar/OpenAI-Math/115-contingency-tables) (Latent Seminar, 2026-10-07). Explains the sampling manuscript's rare residual correction and the counting manuscript's forest coordinates and multiplicity corrections, stating that it reviews selected sections rather than independently verifying the full proofs. [family-level]

## News and blogs
- [Sean Moran, *What OpenAI’s 719 Maths Papers Mean for Data Science*](https://pub.towardsai.net/what-openais-719-maths-papers-mean-for-data-science-c32c2b0e039e) (Towards AI, 2026-10-11). The section on random tables discusses this manuscript's uniform fixed-margin sampling claim, distinguishes its distribution from record shuffling, and notes the implementation work needed to assess practical running time.
