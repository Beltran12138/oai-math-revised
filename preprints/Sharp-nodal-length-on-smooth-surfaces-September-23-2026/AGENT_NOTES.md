# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Guiyu Xie, Cheng Zhang, *Sharp Bounds for Nodal Sets of Steklov Eigenfunctions on Smooth Surfaces*](https://arxiv.org/abs/2610.28391) (arXiv:2610.28391, 2026-10-20). Proves a sharp linear upper bound for the interior nodal length of Steklov eigenfunctions on smooth compact surfaces with boundary; it lists this preprint as reference [26] among works on nodal sets of Laplace eigenfunctions on closed manifolds.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note: Yau's nodal bounds: surfaces and higher dimensions*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/350.md) (lean/docs/350.md, 6 October 2026). The release's scope note says the formalization covers the upper bound $\mathcal H^1(Z_u)\le C\sqrt\lambda$ for every nonzero real positive-eigenvalue eigenfunction on a fixed smooth closed connected surface, and that the known lower bound is not part of the formalized statement. [family-level]
- [OpenAI math release, *NodalLength.lean (comparator statement)*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/NodalLength.lean) (openai/math, lean/ComparatorChallenges, 2026). Comparator file with the Lean statement of the surface bound: there is $C\ge0$ such that every nonzero smooth eigenfunction with $\lambda>0$ has nodal length at most $C\sqrt\lambda$.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [A. Logunov, E. Malinnikova, N. Nadirashvili, F. Nazarov, *The sharp upper bound for the area of the nodal sets of Dirichlet Laplace eigenfunctions*](https://arxiv.org/abs/2104.09012) (arXiv:2104.09012, 2021). Proves the sharp $C\sqrt\lambda$ nodal upper bound for Dirichlet eigenfunctions on bounded $C^1$ domains in $\mathbb R^n$, a comparable sharp upper bound in a different setting from the closed-surface Theorem 1.1; not in the paper's bibliography.
- [A. Logunov, E. Malinnikova, *Review of Yau's conjecture on zero sets of Laplace eigenfunctions*](https://arxiv.org/abs/1908.01639) (arXiv:1908.01639, 5 August 2019; CDM 2018 lectures). Survey of the smooth-case results, growth estimates and two-dimensional methods for zero sets, i.e. the state of the art that the introduction summarises before Theorem 1.1.

## Digests and expositions
- [heyprof, *Yau’s nodal lines — Chladni on sphere and torus (3D)*](https://www.heyprof.app/en/demo/yau-knotenlinien) (VisuApp, undated). This interactive exposition illustrates nodal length on the round sphere and flat torus and places the family’s claimed surface bound alongside its higher-dimensional counterexamples. [family-level]

## News and blogs
- None found.
