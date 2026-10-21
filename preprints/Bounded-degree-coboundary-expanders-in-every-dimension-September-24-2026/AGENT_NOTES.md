# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 177: Bounded-degree coboundary expanders*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/177.md) (lean/docs/177.md). Describes the formalization's scope: for every d ≥ 3, pure connected d-complexes with growing vertex counts, uniformly bounded vertex degree and uniform 𝔽₂ coboundary expansion in all degrees below d; the graph and two-dimensional cases are not part of it. [family-level]
- [OpenAI math release, *Comparator statement CoboundaryExpanders.lean*](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/CoboundaryExpanders.lean) (openai/math, Lean 4/Mathlib). Self-contained Lean statement `MainStatement` of Theorem 1.1, covering weighted norms, the coboundary map and distance to coboundaries; in this challenge file the theorem itself is left as `sorry`.
- [OpenAI math release, *Main.lean, Combinatorics/Coboundary*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Coboundary/Main.lean) (openai/math, commit adc7f12). Contains the theorem `main : MainStatement`, described in its docstring as the manuscript's full theorem; the proof fixes a large odd prime and reduces the statement to group-homology vanishing inputs.

## Related prior literature mentioned by others
- [Izhar Oppenheim and Inga Valentiner-Branth, *New cosystolic high-dimensional expanders from KMS groups*](https://arxiv.org/abs/2504.05823v2) (arXiv:2504.05823v2, 9 September 2026). The [AI-written Open Mathematics Courses exposition](https://kokunoyumeto.github.io/open-math-courses-public/courses/coboundary-expanders-of-bounded-degree/providers.html) identifies this work as the expansion input used alongside the manuscript's cohomology-vanishing argument.

## Possibly relevant literature (found by the agent, not checked)
- [M. Hopkins and A. Ray, *A Simple Sub-Polynomial Degree Coboundary Expander*](https://arxiv.org/abs/2605.22173) (arXiv:2605.22173, 2026-05-21). A recent combinatorial coboundary-expander construction with sub-polynomial rather than bounded degree, relevant to the paper's account of the state of the art before Theorem 1.1.
- [Y. Dikstein, S. Liu and A. Wigderson, *Sparser Abelian High Dimensional Expanders*](https://arxiv.org/abs/2411.08839) (arXiv:2411.08839, 2024-11-13). Gives a two-dimensional complex that is both a spectral and a coboundary expander, with unbounded degree, relevant to the paper's "Prior work" comparison of degree conditions.
- [R. O'Donnell and N. G. Singer, *Coboundary expansion inside Chevalley coset complex HDXs*](https://arxiv.org/abs/2411.05916) (arXiv:2411.05916, 2024-11-08). Proves 1-coboundary expansion in the links of B₃ coset complexes over 𝔽_{5^k}[x] using unipotent-group cohomology vanishing, which parallels the paper's coset-complex and cohomology-vanishing approach.

## Digests and expositions
- [Latent Seminar, *Bounded-degree coboundary expansion*](https://lowrank.github.io/latent-seminar/OpenAI-Math/177-coboundary-expanders) (7 October 2026). Explains the distinction between cocycles and coboundaries, the congruence-tower vanishing strategy and the skeleton-weight comparison, while explicitly disclaiming complete proof verification or a Lean audit.
- [Open Mathematics Courses, *Coboundary expanders of bounded degree*](https://kokunoyumeto.github.io/open-math-courses-public/courses/coboundary-expanders-of-bounded-degree/) (undated). Three lessons develop weighted coboundary expansion and the polynomial-matrix coset construction, deriving the headline theorem conditionally on two explicitly unproved inputs: expansion relative to cocycles and cohomology vanishing. [AI-generated per source]

## News and blogs
- [Gil Kalai, *Updates: Sharing AI progress on mathematics (amazing!); and my lecture plans*](https://gilkalai.wordpress.com/2026/10/07/updates-sharing-ai-progress-on-mathematics-amazing-and-my-lecture-plans/) (Combinatorics and more, 2026-10-07). A section on Ramanujan graphs and higher-dimensional expanders mentions this paper's bounded-degree 𝔽₂ coboundary expanders for d ≥ 3 and links the result to Kalai's earlier introductory posts on high-dimensional expanders.
