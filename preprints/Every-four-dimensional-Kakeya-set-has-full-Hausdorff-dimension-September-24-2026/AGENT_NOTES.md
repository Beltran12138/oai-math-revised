# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [OpenAI, *Local smoothing for the Euclidean wave equation*](https://github.com/openai/math/blob/main/preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/paper.pdf) (OpenAI Math Release preprint, dated 2026-10-25, added 2026-10-26). This manuscript claims local smoothing in every dimension $n\ge2$ and derives that every subset of $\mathbb R^n$ containing a unit segment in every direction has Hausdorff dimension $n$, which would contain this paper's Theorem 1.1, and its Kakeya section cites this paper as the four-dimensional Hausdorff-dimension theorem. [AI-generated per source] [family-level]

## Comments and discussion
- [Florious (@Florious95), thread on X](https://x.com/Florious95/status/2108522391676870685) (2026-10-09). In Chinese, notes that this unreviewed four-dimensional proof takes the Wang–Zahl sticky Kakeya theorem and the Guth–Wang–Zahl three-dimensional estimates as key inputs, arguing it builds on that human work.
- [arutar, comment on Hacker News](https://news.ycombinator.com/item?id=50260957) (2026-10-27). In the thread on OpenAI's 26 October results, this pseudonymous commenter states that "Hong, Josh and coauthors were pretty far along the way to finishing the R4 case" when "they got scooped in the previous batch", a report of unpublished human work on the four-dimensional case.

## Formalization
- [mo271, *Wikipedia/Kakeya: the Kakeya set conjecture holds in dimension 4* (issue #6910)](https://github.com/google-deepmind/formal-conjectures/issues/6910) (google-deepmind/formal-conjectures, opened 2026-10-07). This open issue cites this paper and proposes adding `kakeya_4d : KakeyaSetConjectureDim 4`, tagged as solved, to `FormalConjectures/Wikipedia/Kakeya.lean`; it contains no proof or linked PR and says the comparison was prepared with AI assistance.
- [humanfia, *kakeya-four-dimensions-lean*](https://github.com/humanfia/kakeya-four-dimensions-lean) (GitHub repository, root proof accepted 2026-10-22, fidelity reconciliation dated 2026-10-23). This independent Lean 4 repository states `kakeya_four_dimensions`, with no measurability or boundedness hypothesis on $K$, reports no `sorry`, only the axioms `propext`, `Classical.choice` and `Quot.sound`, and acceptance by the comparator check, and its [fidelity verdict](https://github.com/humanfia/kakeya-four-dimensions-lean/blob/main/verification/FIDELITY-VERDICT.md) rates the statement faithful to Theorem 1.1 while recommending that an external expert read the challenge files and noting that the paper's consequences are not formalized. [AI-generated per source]

## Related prior literature mentioned by others
- [Hong Wang and Joshua Zahl, *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions*](https://arxiv.org/abs/2502.17655v1) (arXiv:2502.17655v1, 2025-02-24). Azmat's Binary Verse AI exposition distinguishes this three-dimensional Hausdorff- and Minkowski-dimension theorem from the release's three-dimensional maximal and four-dimensional Hausdorff claims. [family-level]
- [Larry Guth, Hong Wang, and Joshua Zahl, *A streamlined proof of the Kakeya set conjecture in R³*](https://arxiv.org/abs/2601.14411v1) (arXiv:2601.14411v1, 2026-01-20). Azmat's Binary Verse AI exposition identifies this union estimate as the foundation for the three-dimensional companion's weighted plank estimate used by the four-dimensional manuscript. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [Mukul Rai Choudhuri, *New bound on the Hausdorff dimension of Kakeya sets in $\mathbb{R}^4$*](https://arxiv.org/abs/2610.12480) (arXiv:2610.12480, submitted 30 Aug 2026). This paper combines Wang–Zahl with the Katz–Zahl planebrush to give the lower bound 3.073, whereas this paper's introduction names 3.059 as the prior Hausdorff bound.
- [Tiago Moreira, *Refinements on the Restriction and Kakeya problems range in $\mathbb{R}^4$*](https://arxiv.org/abs/2610.06181) (arXiv:2610.06181, 5 Oct 2026). This paper, posted after this manuscript's date, raises the four-dimensional Kakeya maximal dimension parameter to about 3.06737, above the value 3.0543 (Borges et al.) that the introduction treats as current.
- [Joshua Zahl, *A survey of the Kakeya conjecture, 2000–2025*](https://arxiv.org/abs/2512.09397) (arXiv:2512.09397, Dec 2025). This survey covers the status of the Kakeya problem in dimensions four and higher before this paper; the companion three-dimensional paper cites it, but this paper's bibliography does not.

## Digests and expositions
- [OpenAI Math Digest, *Every four-dimensional Kakeya set has full Hausdorff dimension*](https://masataka123.github.io/OpenAI-Math-Digest/en/papers/kakeya-hausdorff-four/) (undated; accessed 2026-10-21). This explicitly AI-generated guide maps the reduction from Hausdorff covers to positive horizon and the three narrowness regimes, and flags a numbering discrepancy in the citation of the companion's weighted plank estimate. [AI-generated per source]

## News and blogs
- [Azmat, *Kakeya Conjecture: How OpenAI Claims to Break the 4D Barrier*](https://binaryverseai.com/kakeya-conjecture-openai-4d-proof/) (Binary Verse AI, 2026-10-07). This exposition discusses both manuscripts, distinguishes their claims from the Wang–Zahl set theorem, and outlines the four-dimensional argument and its dependence on the three-dimensional companion. [family-level]
