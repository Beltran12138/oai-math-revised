# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Kan Jiang and Lifeng Xi, *The Erdős similarity problem for null sequences with adjacent ratios bounded below*](https://arxiv.org/abs/2610.11449) (arXiv:2610.11449, 8 October 2026). Builds compact sets of measure above $1-\eta$ in $[0,1]$ that avoid affine copies of positive null sequences with $\liminf a_{n+1}/a_n>0$ (without monotonicity, and simultaneously for prescribed countable families), adapting the finite-tree construction of the dyadic and geometric manuscripts, which it cites as unpublished manuscripts [17, 18]. [family-level]
- [Vjekoslav Kovač (submitter), generated with ChatGPT-6 Astra, *Superexponentially decaying sequences in the Erdos similarity problem*](https://hexagonmath.org/abs/2610.00176v1) (hexagon:2610.00176v1, 10 October 2026). Proves a non-universality criterion that covers some superexponentially decaying sequences, and states that its proof modifies the finite-tree construction of this geometric-case manuscript (its reference [18]). [AI-generated per source]
- [Harald Schilly, *Erdős similarity for distance sets: finite patterns, a pinned obstruction, and an open window*](https://github.com/haraldschilly/math-distance-set-similarity) (preprint and Lean repository, October 2026). This follow-up, prepared with substantial Claude assistance, derives pinned-distance obstructions from the avoidance results and reports replaying the dyadic Lean proof, while retaining general-ratio avoidance as an explicit hypothesis. [family-level]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, Lean scope note for family 084](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/084.md) (release Lean documentation). The scope note covers only the dyadic case $q=1/2$ of the companion paper (compact subsets of $[0,1]$ of measure arbitrarily close to one avoiding every translated dyadic sequence with either sign of nonzero dilation); there is no formalization of the general-$q$ theorem. [family-level]
- [OpenAI math release, *DyadicAvoidance/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/MeasureTheory/DyadicAvoidance/Main.lean) (openai/math, commit adc7f12). Lean theorem `Problem310.dyadic_affine_avoidance`, the $q=1/2$ special case of Theorem 1.1. [family-level]

## Related prior literature mentioned by others
- [Yeonwook Jung, Chun-Kit Lai, Yuveshen Mooroogen, *Fifty years of the Erdős similarity conjecture*](https://arxiv.org/abs/2412.11062) (arXiv:2412.11062v2, 2025-01-01). This survey states the conjecture "remains open for exponentially decaying sequences" and reviews variants of measure universality; the Jiang–Xi, Hexagon and Schilly follow-ups cite it, and it is not in this paper's bibliography.

## Possibly relevant literature (found by the agent, not checked)
- [Alex Burgin, Samuel Goldberg, Tamás Keleti, Connor MacMahon, Xianzhi Wang, *Large sets avoiding infinite arithmetic / geometric progressions*](https://arxiv.org/abs/2210.09284) (arXiv:2210.09284, October 2022). Builds a compact set with a density point at 0 that contains no non-constant infinite geometric progression of any ratio, a variant of the fixed-ratio avoidance problem in Theorem 1.1; not in this paper's bibliography.

## Digests and expositions
- [Patrick White with Claude, Erdős Problem a Day, *Erdős #120: OpenAI claims the geometric case*](https://erdosproblemaday.com/day/120-openai-geometric-similarity-refereed) (2026-10-14). Explains the routing and scale-counting construction and reports AI-led proof audits and a dyadic Lean replay, explicitly distinguishing these from human verification of the general-ratio theorem. [AI-generated per source] [family-level]

## News and blogs
- None found.
