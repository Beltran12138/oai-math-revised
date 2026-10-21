# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Krzysztof Burdzy, *Removing Boundary Smoothness from the Hot-Spots Conclusion in the Simple-Eigenvalue Case*](https://arxiv.org/abs/2610.12622) (arXiv:2610.12622, 8 Oct 2026). Takes this paper's smooth-domain theorem as an unverified external input and, by exhaustion with conformal images of concentric disks, derives a non-strict hot-spots conclusion on bounded simply connected planar domains with compact Neumann resolvent and simple first positive eigenvalue. [AI-generated per source]
- [Haiyun Deng, Changfeng Gui, Xuyong Jiang, Xiaoping Yang, Ruofei Yao, Jun Zou, *Symmetry and critical points of second Neumann eigenfunctions on isosceles trapezoids and kites*](https://arxiv.org/abs/2604.19003) (arXiv:2604.19003v4, 11 Oct 2026). Proves absence of interior critical points on isosceles trapezoids and kites; a "Declaration" added in v4 compares this paper's scope (smooth boundary, excluding polygons with corners) and its Green-kernel multiplier method with the authors' own.
- [Jizhou Guo, *First Neumann eigenfunctions of convex planar domains attain their extrema on the boundary*](https://github.com/aster2024/openai-math-followups/blob/main/hot-spots-convex-planar/paper.pdf) (GitHub preprint, 2026-10-10). The author's repository describes a deduction from this paper's smooth-domain theorem of non-strict boundary extrema for every first-positive Neumann eigenfunction on bounded convex planar domains, allowing nonsmooth boundary and a double eigenvalue.
- [Rami Atar and Krzysztof Burdzy, *A starlike 3-dimensional counterexample to the hot spots conjecture*](https://arxiv.org/html/2610.19908v1) (arXiv:2610.19908v1, 2026-10-14). Cites this planar theorem in its introduction and constructs a bounded starlike Lipschitz domain in three dimensions with a simple first positive Neumann eigenvalue and an eigenfunction whose unique global maximum is at the origin.

## Expert comments and discussion
- [Krzysztof Burdzy, remarks in Section 1 of arXiv:2610.12622](https://arxiv.org/html/2610.12622) (arXiv, Oct 2026). Burdzy, who stated the simply connected conjecture in 2005, says he has not assessed this paper's proof and that "The OpenAI model that generated [3] missed the theorem presented in this note"; he also reports that Rodrigo Bañuelos used ChatGPT to generate an almost identical theorem and proof. [AI-generated per source]
- [Sugata Mondal, *Hot spots for a class of Lip-1 domains*](https://www.kth.se/en/2.82512/kalender/sugata-mondal-hot-spots-for-a-class-of-lip-1-domains-1.1501857?date=2026-10-28&length=1&orgdate=2026-01-15&orglength=351) (Stockholm Mathematics Centre seminar announcement, updated 2026-10-15; talk 2026-10-28). The abstract identifies OpenAI's claimed resolution for simply connected planar domains as recent context for a talk on lip domains and higher-dimensional analogues.

## Formalization
- [mathcommunity/oai-math-revised, *lean/docs/369.md*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/369.md) (OpenAI math release Lean scope notes, 2026-10-06). States that the Lean formalization proves nonvanishing interior gradient for every nonzero first positive Neumann eigenfunction on nonempty smooth bounded simply connected planar domains, including the multiple-eigenvalue case.
- [mathcommunity/oai-math-revised, *lean/ComparatorChallenges/HotSpots.lean*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/HotSpots.lean) (release comparator statement). Gives the Lean 4/Mathlib statement `OAI.StrictHotSpots.main_theorem`: nonzero gradient, plus strict bounds by the boundary infimum and supremum, for nonzero `u` in the first Neumann eigenspace of an `AdmissibleDomain`.

## Related prior literature mentioned by others
- [Jaume de Dios Pont, *Convex sets can have interior hot spots*](https://arxiv.org/abs/2412.06344) (arXiv:2412.06344, 2024-12-09). Cited by the follow-up works (Burdzy; Deng et al.; Atar–Burdzy) for its counterexamples on convex domains in sufficiently high dimensions, which is context for this paper's restriction to planar domains.

## Possibly relevant literature (found by the agent, not checked)
- [Jonathan Rohleder, *Inequalities between Neumann and Dirichlet Laplacian eigenvalues on planar domains*](https://arxiv.org/abs/2306.12922) (arXiv:2306.12922, v4 Jun 2025). Introduces a variational principle on simply connected planar Lipschitz domains of the same kind as the tangent-vector-field principle in Section 3 of this paper, whose bibliography cites only Rohleder's arXiv:2106.05224 and the 2024 extended abstract.

## Digests and expositions
- [Gradient Damage, *Boltzmann Equation, Hot Spots Conjecture and 7 More in Partial Differential Equations*](https://gradientdamage.com/videos/boltzmann-equation-hot-spots-conjecture-and-7-more-in-partial/) (video compilation, 2026-10-15). The chapter beginning at 1:24 illustrates the hot-spots claim and links this manuscript; the accompanying page distinguishes the animations from proofs.

## News and blogs
- None found.
