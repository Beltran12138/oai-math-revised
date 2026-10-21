# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *Sharp finite-matrix Lieb–Thirring inequalities and all equality cases: Lean scope notes*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/262.md) (`lean/docs/262.md`, OpenAI Math Release, 2026-10-06). The scope note says the formalized statement is this paper's Theorem 1.1 (sharp constant for $1/2<\gamma<3/2$, attained by $(r+1)\mathrm{sech}^2(rx)$, no finite spectral cutoff), and links the comparator statement [`LiebThirring.lean`](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/LiebThirring.lean), where `OAI.SharpLiebThirring.sharp_lieb_thirring` is stated with `sorry` as the challenge statement. [AI-generated per source] [family-level]
- [OpenAI math release, *`lean/OAI/Analysis/LiebThirring/Main.lean`*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/LiebThirring/Main.lean) (openai/math, commit adc7f12, October 2026). The release's Lean proof of `sharp_lieb_thirring`, identifying the optimal constant, the one-state constant and the sharp constant, and giving equality at the explicit potential.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Rupert L. Frank, David Gontier, Mathieu Lewin, *The nonlinear Schrödinger equation for orthonormal functions: II. Application to Lieb-Thirring inequalities*](https://arxiv.org/abs/2002.04964) (arXiv:2002.04964, 2020). Shows that the best constant is never attained in the one-bound-state case for $\gamma>\max(0,2-d/2)$, i.e. $\gamma>3/2$ in $d=1$, the complement of the range in which this paper proves the one-bound-state constant is sharp. Not in the bibliography.
- [Rupert L. Frank, David Gontier, Mathieu Lewin, *Optimizers for the finite-rank Lieb-Thirring inequality*](https://arxiv.org/abs/2109.05984) (arXiv:2109.05984, 2021; to appear in Amer. J. Math. per arXiv comments). Studies existence and compactness of finite-rank optimizers and identifies KdV $N$-solitons at $\gamma=3/2$ in 1D, relevant to the paper's remark that it exhibits an equality potential "without classifying all optimizers". Not in the bibliography.
- [Lukas Schimmer, *The state of the Lieb--Thirring conjecture*](https://arxiv.org/abs/2203.06051) (arXiv:2203.06051, 2022). A survey of known results on the conjectured optimal constants, which gives the pre-2026 status of the cases this paper claims to resolve. Not in the bibliography.
- [Rupert L. Frank, *The Lieb-Thirring inequalities: Recent results and open problems*](https://arxiv.org/abs/2007.09326) (arXiv:2007.09326, 2020-07-18). A survey of open problems that include the one-dimensional sharp-constant conjecture for $1/2<\gamma<3/2$ and the one-particle comparison addressed in Theorem 1.1. Not in the bibliography.
- [Rupert L. Frank, Ari Laptev, Timo Weidl, *Schrödinger Operators: Eigenvalues and Lieb–Thirring Inequalities*](https://www.cambridge.org/core/books/schrodinger-operators-eigenvalues-and-liebthirring-inequalities/519F8E15C1B7E9DCF96C491F97257CC4) (Cambridge Studies in Advanced Mathematics 200, 2022). A monograph on the sharp-constant results that the history section reviews (Hundertmark–Lieb–Thomas, Laptev–Weidl, Hundertmark–Laptev–Weidl). Not in the bibliography.

## Digests and expositions
- [Latent Seminar, *Sharp Lieb–Thirring bounds: one state, matrix channels, and equality*](https://lowrank.github.io/latent-seminar/OpenAI-Math/262-sharp-lieb-thirring-inequalities) (2026-10-07). This exposition distinguishes the three manuscripts and outlines the action inequality, arbitrary-rank trace comparison, and fixed-channel equality argument, explicitly limiting its verification scope. [family-level]
- [Gradient Damage, *Spacetime Penrose Inequality, Strong Cosmic Censorship Near Kerr and 8 More*](https://gradientdamage.com/videos/spacetime-penrose-inequality-strong-cosmic-censorship-near-kerr-and-8/) (video compilation, 2026-10-15). The chapter at 0:22 introduces the family's spectral bound through potential wells and bound-state energies as an illustration of the reported result. [family-level]

## News and blogs
- None found.
