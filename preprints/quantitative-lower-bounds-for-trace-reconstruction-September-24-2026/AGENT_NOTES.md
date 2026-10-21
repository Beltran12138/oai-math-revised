# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- [AIM open-problem collection (MColbrook/AIM), *Problem 321: Polynomial sample complexity for deletion-trace reconstruction*](https://github.com/MColbrook/AIM/blob/main/problems/321-polynomial-trace-reconstruction.md) (AIM entry, last checked 2026-10-13). Marks the polynomial-sample question as solved by counterexample, citing this paper's Theorems 1.1 and 1.2; the entry calls itself "an AI statement-level review of a published manuscript, not a fresh independent audit." [AI-generated per source]
- [AIM, *OpenAI manuscript cross-reference, 13 October 2026*](https://github.com/MColbrook/AIM/blob/main/research/solution_reviews/2026-10-13-openai-crosscheck/README.md) (AIM solution review, 2026-10-13). Compares this paper's definitions (complete traces, a common randomized decoder, s=2/3) with AIM problem 321 and notes "No successful local replay/axiom log" for the Lean module. [AI-generated per source]
- [yuiyuiui for Kaiwen Jin, *321: proposed negative resolution from the OpenAI trace lower bound*](https://github.com/MColbrook/AIM/pull/50) (MColbrook/AIM PR #50, opened 2026-10-11, closed unmerged 2026-10-12). Proposed recording this paper's Theorem 1.2 as a negative answer to AIM problem 321; the author withdrew it as redundant with the existing entry. [AI-generated per source]

## Formalization
- [OpenAI math release / mathcommunity mirror, *Lean scope note 122: Quantitative trace-reconstruction bounds with a uniform decoder*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/122.md) (lean/docs/122.md, 2026-10-06). Links the comparator statement and describes the Lean formalization of this paper's bound $T_{q,s}(n)\ge n^{c\log(q^3\log n)}$, superpolynomial sample complexity at every fixed deletion probability, and the superpolynomial decay of the minimum one-trace total variation.
- [OpenAI, *TraceReconstruction.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/TraceReconstruction.lean) (openai/math, commit adc7f12). The Lean module stating `quantitative_sample_lower_bound`, `superpolynomial_one_trace` and `superpolynomial_sample_complexity`, which correspond to Theorems 1.1 and 1.2.

## Related prior literature mentioned by others
- [Arnav Burudgunte, Paul Valiant and Hongao Wang, *Quasipolynomial Trace Reconstruction*](https://arxiv.org/abs/2607.04073v1) (arXiv:2607.04073v1, 2026-07-05). The [AI Proved What? exposition](https://aiprovedwhat.com/episodes/122-trace-reconstruction-bounds/) identifies this earlier quasipolynomial sample upper bound as background to the family’s lower-bound and decoder claims. [family-level]
- [Zachary Chase, *New Lower Bounds for Trace Reconstruction*](https://arxiv.org/abs/1905.03031v2) (arXiv:1905.03031v2, 2020-07-23). The [AI Proved What? exposition](https://aiprovedwhat.com/episodes/122-trace-reconstruction-bounds/) compares the claimed superpolynomial lower bound with Chase’s earlier $\Omega(n^{3/2}/\log^7 n)$ lower bound.

## Possibly relevant literature (found by the agent, not checked)
- [Burudgunte, Valiant, Wang, *New Bounds for Circular Trace Reconstruction*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.30/LIPIcs.ITCS.2026.30.html) (ITCS 2026, LIPIcs, doi:10.4230/LIPIcs.ITCS.2026.30; arXiv:2512.02412). Proves an $\tilde\Omega(n^5)$ lower bound for the circular variant using pairs of constant-sparse strings with nearly indistinguishable traces, a related lower-bound construction not cited in the paper's history section.

## Digests and expositions
- [AI Proved What?, *Polynomially many traces? Lower and upper bounds for trace reconstruction*](https://aiprovedwhat.com/episodes/122-trace-reconstruction-bounds/) (Episode 122, October 2026). This video and transcript explain the three papers’ claims, the multiscale lower-bound construction and moment-based decoder, and distinguish the lower-bound Lean scope from the upper bounds. [AI-generated per source] [family-level]

## News and blogs
- None found.
