# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note for family 373: Nonattainment of the three-marginal Coulomb Monge problem*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/373.md) (lean/docs/373.md, 6 October 2026). The scope note says the formalization covers smooth-density nonattainment for the three-dimensional Coulomb problem and equality of the Monge and Kantorovich infima, and it links the comparator statement. It states that the paper's inverse-power Riesz extensions in other dimensions are outside the formalized statement. [family-level]
- [OpenAI math release, *CoulombCounterexample.lean* (comparator challenge statement)](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/CoulombCounterexample.lean) (openai/math, 2026). This is the comparator statement `coulomb_counterexample_and_equal_infima`, which asserts a density with nonattainment, equal infima and finite-cost Monge approximation. In this challenge file the statement is left as `sorry`.
- [OpenAI math release, *OAI.Analysis.CoulombTransport.Main*](https://github.com/openai/math/blob/main/lean/OAI/Analysis/CoulombTransport/Main.lean) (openai/math, 2026). This is the entry module of the solution development, and it imports `CoulombTransport.All` and `CoulombTransport.Conclusion`.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [G. Friesecke, *A simple counterexample to the Monge ansatz in multi-marginal optimal transport, convex geometry of the set of Kantorovich plans, and the Frenkel-Kontorova model*](https://arxiv.org/abs/1808.04318) (arXiv:1808.04318, 13 August 2018). This paper shows that the Monge ansatz fails for three marginals with symmetric pairwise (Frenkel–Kontorova) costs in a finite-state setting, and its continuous superposition exhibits nonattainment through microstructure. It is a possible comparison for the paper's Coulomb nonattainment and approximating-map construction.
- [A. Moameni and B. Pass, *Solutions to multi-marginal optimal transport problems concentrated on several graphs*](https://arxiv.org/abs/1507.05923) (arXiv:1507.05923, 2015). This paper studies multi-marginal optimizers concentrated on several graphs over the first marginal, and its examples include the one-dimensional Coulomb cost. It is related to the paper's optimizer, which is supported on four branch families and their permutations.
- [B. Pass, *Multi-marginal optimal transport: theory and applications*](https://arxiv.org/abs/1406.0026) (arXiv:1406.0026, 2014). This survey covers the existence, uniqueness and structure (including Monge form) of multi-marginal optimizers, the setting of the paper's Monge-attainment question.

## Digests and expositions
- [Hal Tasaki (requester) / ChatGPT Astra, *Mathematical physics in the OpenAI math release*, entry 1.20](https://haltasaki.github.io/writings/pdf/OpenAI_Mathematical_Physics_Catalogue_2026-10-07.pdf) (research catalogue, 7 October 2026). This catalogue entry summarizes the paper's claim in one sentence and marks it as having its main Lean statement listed, with the inverse-power extensions not documented. [AI-generated per source]
- [Gradient Damage, *Boltzmann Equation, Hot Spots Conjecture and 7 More in Partial Differential Equations*](https://gradientdamage.com/videos/boltzmann-equation-hot-spots-conjecture-and-7-more-in-partial/) (video compilation, 15 October 2026). The chapter beginning at 2:06 introduces the three-particle Coulomb Monge problem and presents the release's nonattainment claim as an illustration rather than a proof. [family-level]

## News and blogs
- None found.
