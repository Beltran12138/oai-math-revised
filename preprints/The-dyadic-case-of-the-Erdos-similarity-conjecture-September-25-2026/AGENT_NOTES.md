# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Kan Jiang and Lifeng Xi, *The Erdős similarity problem for null sequences with adjacent ratios bounded below*](https://arxiv.org/abs/2610.11449) (arXiv:2610.11449, 8 October 2026). Builds compact sets of measure above $1-\eta$ in $[0,1]$ that avoid affine copies of positive null sequences with $\liminf a_{n+1}/a_n>0$ (without monotonicity, and simultaneously for prescribed countable families), adapting the finite-tree construction of the dyadic and geometric manuscripts, which it cites as unpublished manuscripts [17, 18]. [family-level]
- [Harald Schilly, *Erdős similarity for distance sets: finite patterns, a pinned obstruction, and an open window*](https://github.com/haraldschilly/math-distance-set-similarity) (preprint and Lean repository, October 2026). This follow-up, prepared with substantial Claude assistance, derives pinned-distance obstructions from the avoidance results and reports replaying the dyadic Lean proof, while retaining general-ratio avoidance as an explicit hypothesis. [family-level]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, Lean scope note for family 084](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/084.md) (release Lean documentation). Describes a Lean formalization of Theorem 1.1 (compact $E\subset[0,1]$, $m(E)>1-\eta$, avoiding $x+s2^{-n}$ for all $x$ and both signs of $s\neq0$). [family-level]
- [OpenAI math release, *DyadicAvoidance/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/MeasureTheory/DyadicAvoidance/Main.lean) (openai/math, commit adc7f12). Contains the Lean theorem `Problem310.dyadic_affine_avoidance`, derived from a periodic hitting-set lemma. [family-level]
- [google-deepmind/formal-conjectures, *GreensOpenProblems/94.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/GreensOpenProblems/94.lean) (formal-conjectures, accessed 2026-10-21). States Green's Open Problem 94 (the dyadic case), marks it `research solved` citing this paper, and links the OpenAI Lean proof; the statement in this file ends in `sorry`.
- [mo271, *feat: mark problems solved in the OpenAI math release and link formal proofs*](https://github.com/google-deepmind/formal-conjectures/pull/6898) (formal-conjectures PR #6898, merged 11 October 2026). Lists "Green 94 (dyadic Erdős similarity)" among the newly solved problems; a commenter asked whether Erdős Problem 120 should also be updated, and the merged change does not include it.

## Related prior literature mentioned by others
- [Yeonwook Jung, Chun-Kit Lai, Yuveshen Mooroogen, *Fifty years of the Erdős similarity conjecture*](https://arxiv.org/abs/2412.11062) (arXiv:2412.11062v2, 2025-01-01). This survey states the conjecture "remains open for exponentially decaying sequences" and reviews variants of measure universality; Jiang–Xi and Schilly cite it, and it is not in this paper's bibliography.

## Possibly relevant literature (found by the agent, not checked)
- [Alex Burgin, Samuel Goldberg, Tamás Keleti, Connor MacMahon, Xianzhi Wang, *Large sets avoiding infinite arithmetic / geometric progressions*](https://arxiv.org/abs/2210.09284) (arXiv:2210.09284, October 2022). Builds a compact set with a density point at 0 that contains no non-constant infinite geometric progression, a variable-ratio variant of the avoidance of affine copies of $\{2^{-n}\}$ in Theorem 1.1; not in this paper's bibliography.

## Digests and expositions
- [Patrick White with Claude, Erdős Problem a Day, *Erdős #120: OpenAI claims the geometric case*](https://erdosproblemaday.com/day/120-openai-geometric-similarity-refereed) (2026-10-14). Explains the routing and scale-counting construction and reports AI-led proof audits and a dyadic Lean replay, explicitly distinguishing these from human verification of the general-ratio theorem. [AI-generated per source] [family-level]

## News and blogs
- None found.
