# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Ryan Shea, *Sharper One-Sample Matroid Prophet Inequalities*](https://github.com/shea256/matroid-prophet-inequality) (GitHub repository and [manuscript](https://github.com/shea256/matroid-prophet-inequality/blob/master/manuscript.md), 2026-10-11). Claims a refinement of this paper's construction with reward fraction greater than $(35/32)2^{-31}$ under the same one-sample, full-seed adversary model; it states that independent mathematical review and formalization remain pending. [AI-generated per source]
- [bottlebrushes, *MatroidProphet (#111): one-sample ratio 2^-310 → 2^-38, Lean-verified*](https://github.com/bottlebrushes/math/pull/1) (GitHub pull request, merged 2026-10-10). Keeps this paper's rule and proof architecture, re-tunes parameters and tightens estimates, and reports a sorry-free Lean theorem `one_sample_sharp` with ratio 2^-38 built on the release's Lean development.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *One-sample matroid prophet inequalities against an almighty adversary — Lean scope*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/111.md) (OpenAI math release, 2026-10-06). The scope note records the $2^{-310}$ one-sample guarantee against an order depending measurably on samples, values, and the entire seed, together with a supporting $2^{-293}$ hidden-vector worst-order guarantee and feasibility after every prefix. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Jack Wang, *The Prophet Inequality Can Be Solved Optimally with a Single Set of Samples*](https://arxiv.org/abs/1812.10563) (arXiv:1812.10563, 2018). A single-choice, single-sample 1/2 guarantee stated to hold "against even an almighty adversary", the rank-one analogue of the adversary model in Theorem 1.1.
- [Shaddin Dughmi, *Matroid Secretary Is Equivalent to Contention Resolution*](https://arxiv.org/abs/2103.04205) (arXiv:2103.04205, 2021). Relates matroid secretary to prophet secretary and contention resolution, bearing on the paper's secretary corollary and its use of the OCRS almighty-adversary framework.
- [Andrés Cristi and Bruno Ziliotto, *Prophet Inequalities Require Only a Constant Number of Samples*](https://arxiv.org/abs/2311.09141) (arXiv:2311.09141, 2023). Shows a constant number of samples per distribution suffices in single-choice variants, relevant to the paper's discussion of one sample versus growing sample budgets.
- [Sina Kalantarzadeh and Kanstantin Pashkovich, *Simple and Almost Non-Adaptive $\frac{1}{2}$-Approximation for Matroid Prophet Inequalities*](https://arxiv.org/abs/2607.20269) (arXiv:2607.20269, revised 2026-09-05). Uses a direct sum of matroid minors and fixed thresholds for an ex-ante $1/2$ guarantee, a comparison point for the paper's use of matroid layers.

## Digests and expositions
- [Latent Seminar, *One-sample matroid prophet inequalities and informed adversaries*](https://lowrank.github.io/latent-seminar/OpenAI-Math/111-one-sample-matroid-prophets) (2026-10-07). Explains the expected minimum over arrival orders, the guarded-flat construction, and the three principal losses in the proof, stating that it does not independently verify the complete proofs. [family-level]

## News and blogs
- None found.
