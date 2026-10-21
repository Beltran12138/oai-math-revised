# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [Hang Du, Brice Huang, Sidhanth Mohanty, Amit Rajaraman, *Sampling from the Sherrington-Kirkpatrick Model up to Criticality*](https://arxiv.org/abs/2610.17717) (arXiv:2610.17717, 13 Oct 2026). Section 1.2 ("Concurrent work by OpenAI") gives the authors' interpretation of this paper's proof (stochastic localization, a stability criterion for approximate TAP fixed points, a bad-event bound boosting to a full Poincaré inequality) and contrasts it with their own simulated-annealing approach; it does not state whether the proof was checked.
- [Zhe Hou, Jingcheng Liu, Yixiao Yu, *Simulated annealing and Weak Poincaré inequalities with inverse-polynomial accuracy for the Sherrington-Kirkpatrick model*](https://arxiv.org/abs/2610.09882) (arXiv:2610.09882, 7 Oct 2026). Section 1.3 ("Concurrent work") notes the Poincaré inequality with gap of order 1/n for Glauber dynamics at 0 ≤ β < 1 reported by OpenAI, and Section 1.4 says the authors deferred a separate result in view of OpenAI's announcements.

## Formalization
- [OpenAI, *Family 227 Lean scope*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/227.md) (lean/docs/227.md, 2026-10-06). States that the release's Lean development proves the dimension-free zero-field Gaussian SK Poincaré inequality of Theorem 1.1 for every fixed $0<\beta<1$ with probability tending to one, with uniform-site discrete gap at least $1/(C_\beta n)$ (comparator `SKHighTemperature.lean`). [family-level]

## Related prior literature mentioned by others
- [Almut Roedder, *Sampling from the Sherrington-Kirkpatrick Model (problem 15)*](https://randomstrasse101.math.ethz.ch/posts/SKModel-Glauber/) (Randomstrasse101 open problems of 2024, 20 Dec 2024). Open problem asking whether Glauber dynamics for SK with arbitrary external field mixes in polynomial time up to β = 1; this paper addresses the zero-field case.
- [David Jekel, Juspreet Singh Sandhu and Jonathan Shi, *Potential Hessian Ascent: The Sherrington-Kirkpatrick Model*](https://arxiv.org/abs/2408.02360) (arXiv:2408.02360, 2024; revised 2026-05-20). Finding F3 of the [AI-generated math-lineage review](https://raw.githubusercontent.com/jnshi/math-lineage/main/preprints/A-spectral-gap-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/README.md) identifies its adaptive-diagonal matrix estimates as antecedents of the spectral-gap paper’s deterministic equivalents.

## Possibly relevant literature (found by the agent, not checked)
- [Ewan Davies, Holden Lee, Juspreet Singh Sandhu, Jonathan Shi, *Weak Poincaré Inequalities via Approximate Stochastic Localization: Application to Sampling the Sherrington-Kirkpatrick Model*](https://arxiv.org/abs/2607.08160) (arXiv:2607.08160, 9 Jul 2026). Transfers a (weak) Poincaré inequality from approximations of the stochastic localization process to the SK Gibbs measure for β < 1/2, a strategy comparable to the transfer along Gaussian observations in Section 2 of this paper.

## Digests and expositions
- [Latent Seminar, *SK dynamics across the temperature transition*](https://lowrank.github.io/latent-seminar/OpenAI-Math/227-sk-dynamics) (2026-10-06). Explains the eight companions and selected proof mechanisms without independently verifying their proofs. [family-level]
- [math-lineage, *Precedence review: A spectral gap throughout the high-temperature Sherrington–Kirkpatrick phase*](https://raw.githubusercontent.com/jnshi/math-lineage/main/preprints/A-spectral-gap-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/README.md) (2026-10-13). This explicitly unvetted LLM report maps proposed antecedents for the localization, TAP stability, matrix estimates and terminal-gap arguments. [AI-generated per source]

## News and blogs
- None found.
