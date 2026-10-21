# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note for family 236: The exact factor-of-IID threshold for free Ising spins on trees*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/236.md) (lean/docs/236.md, 6 October 2026). The scope note says the formalized statement is the full threshold, including equality, with almost-sure equivariance for each fixed automorphism of a factor of uniform labels; finitary coding and coding-radius bounds are excluded. [family-level]
- [OpenAI math release, *lean/OAI/Probability/FreeIsing/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/FreeIsing/Main.lean) (openai/math, commit adc7f12, 2026). This file states `OAI.Problem367.free_ising_factor_iff_threshold` (for `d ≥ 3`, `beta ≥ 0`: factor of IID iff `tanh beta ≤ 1/sqrt(d-1)`), the Lean counterpart of Theorem 1.1; the file has no `sorry`, but its supporting lemmas are imported from other modules.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Balázs Gerencsér and Viktor Harangi, *Mutual information decay for factors of IID*](https://arxiv.org/abs/1703.04387) (arXiv:1703.04387, 2017). It proves sharp bounds of order (d−1)^(−k/2) on normalized mutual information between vertices at distance k for factor-of-IID processes on d-regular trees, which bears on the obstruction side of the threshold; the paper derives that side from the Backhausz–Szegedy–Virág correlation bound.
- [Ágnes Backhausz and Bálint Virág, *Spectral measures of factor of i.i.d. processes on vertex-transitive graphs*](https://arxiv.org/abs/1505.07412) (arXiv:1505.07412, 2015). It characterizes spectral measures of factor-of-IID processes on transitive graphs, a tool related to the spectral bound for equivariant observables used in the spatial-cancellation step (Section 6).
- [Andrea Montanari, *Sampling, Diffusions, and Stochastic Localization*](https://arxiv.org/abs/2305.10690) (arXiv:2305.10690, 2023). An exposition of stochastic-localization and diffusion processes with posterior drift, background to the Gaussian-observation framework (X_v(t)=tσ_v+B_v(t) and its innovations) on which the construction is built.

## Digests and expositions
- [Latent Seminar, *The sharp IID-factor threshold for free tree Ising spins*](https://lowrank.github.io/latent-seminar/OpenAI-Math/236-tree-ising-factors) (6 October 2026). This exposition outlines the manuscript's innovations recovery, conditional-copy coupling, critical Osgood comparison, and everywhere-equivariant version, stating that it does not independently verify the complete proof. [family-level]
- [Gradient Damage, *Six-Vertex Model, Lipschitz Heights, The O(3) Model Continuum Limit and 6 More*](https://gradientdamage.com/videos/six-vertex-model-lipschitz-heights-the-o-3-model-continuum-limit/) (video compilation, 15 October 2026). The chapter beginning at 1:24 illustrates the free Ising factor-of-IID threshold claim and links the manuscript. [family-level]

## News and blogs
- None found.
