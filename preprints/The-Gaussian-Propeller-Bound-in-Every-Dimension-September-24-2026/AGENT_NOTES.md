# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 096*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/096.md) (lean/docs/096.md, release of 2026-10-06). The scope note states that the Lean development covers the $9/(8\pi)$ bound for all $d,k\ge1$, including empty cells and arbitrary masses, and propeller attainment for $d\ge2$, $k\ge3$, but not the Gaussian-maxima corollary or the kernel-clustering consequence.
- [OpenAI, *GaussianPropeller/Main.lean*](https://github.com/openai/math/blob/main/lean/OAI/Probability/GaussianPropeller/Main.lean) (openai/math, 2026-10-06). This file holds the release's main Lean theorem `GaussianPropeller.all_partitions`, which combines the partition bound, proved by strong induction on the number of cells, with propeller attainment; the comparator statement is in `lean/ComparatorChallenges/GaussianPropeller.lean`.
- [anxkhn, *feat(Paper): add the Gaussian propeller bound*](https://github.com/google-deepmind/formal-conjectures/pull/7002) (google-deepmind/formal-conjectures PR #7002, opened 2026-10-08). This PR adds an independent Lean statement of the upper bound in Theorem 1.1 to formal-conjectures, without a proof and without attainment; it was open with one approving review (bocowgill, 2026-10-10). [AI-generated per source]
- [anxkhn, *Add the Gaussian propeller partition bound*](https://github.com/google-deepmind/formal-conjectures/issues/6997) (google-deepmind/formal-conjectures issue #6997, 2026-10-08). This issue proposes the statement scope used in PR #7002: positive dimension and cell count, a.e. partitions, empty cells allowed, and unnormalized first moments.

## Related prior literature mentioned by others
- [Steven Heilman, Aukosh Jagannath and Assaf Naor, *Solution of the propeller conjecture in ℝ³*](https://arxiv.org/abs/1112.2993) (Discrete & Computational Geometry 50, 263–305, 2013; arXiv:1112.2993). The [course's dependency list](https://kokunoyumeto.github.io/open-math-courses-public/courses/the-gaussian-propeller-bound/providers.html) identifies this computer-assisted three-dimensional theorem as the input handling extremizers with at most four active cells in the manuscript.

## Possibly relevant literature (found by the agent, not checked)
- [M. Isaksson and E. Mossel, *Maximally Stable Gaussian Partitions with Discrete Applications*](https://arxiv.org/abs/0903.3362) (arXiv:0903.3362, 2009; Israel J. Math. 2012). This is the origin of the equal-measure Gaussian noise-stability partition problem that the introduction contrasts with the unrestricted first-moment functional.
- [S. Heilman, *Euclidean Partitions Optimizing Noise Stability*](https://arxiv.org/abs/1211.7138) (arXiv:1211.7138, 2012). Earlier work on the three-cell standard simplex conjecture, relevant to the paper's comparison with Heilman's conditional route via noise-stability maximizers.
- [S. Heilman, E. Mossel and J. Neeman, *Standard Simplices and Pluralities are Not the Most Noise Stable*](https://arxiv.org/abs/1403.0885) (arXiv:1403.0885, 2014). This paper shows that the simplex partition is not noise-stability optimal when cell measures are unequal, which bears on the paper's remark that its result imposes no cell-mass constraint.
- [E. Milman and J. Neeman, *The Gaussian Double-Bubble and Multi-Bubble Conjectures*](https://arxiv.org/abs/1805.10961) (arXiv:1805.10961, 2018; Ann. of Math. 2022). This is a related sharp Gaussian partition problem with simplicial or tripod extremal clusters, relevant to the "related partition problems" discussion in the introduction.
- [Steven Heilman, *Stable Gaussian minimal bubbles*](https://link.springer.com/article/10.1007/s00526-026-03408-z) (Calculus of Variations and Partial Differential Equations 65, article 271, 13 October 2026). Section 1.4 studies a prescribed-mass, shifted first-moment variant of the propeller problem, related to the manuscript's distinction between its unrestricted first-moment bound and constrained Gaussian partition problems.

## Digests and expositions
- [Open Mathematics Courses / Claude Opus 5.5, *The Gaussian propeller bound*](https://kokunoyumeto.github.io/open-math-courses-public/courses/the-gaussian-propeller-bound/) (six-lesson online course, undated). The course develops the manuscript's Gaussian-maxima duality, rearrangement and deletion estimates, residual covariance bounds and kernel-clustering application, with exercises and an explicit notice that independent review is incomplete. [AI-generated per source]
- [heyprof, *Gaussian propeller — the best partition of space (3D)*](https://www.heyprof.app/en/demo/gauss-propeller) (interactive exposition, undated). The exposition illustrates the manuscript's unnormalized Gaussian first-moment objective with adjustable sectors and several spatial partitions, distinguishing numerical examples from the claimed universal bound.

## News and blogs
- None found.
