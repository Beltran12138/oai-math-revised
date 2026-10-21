# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 119: The Courtade–Kumar and Hellinger conjectures*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/119.md) (lean/docs/119.md, 2026). Describes the release's own Lean development for this paper: sharp soft-channel contraction, the bias-refined Boolean bound, the mean-dependent entropy-production inequality and the Courtade–Kumar inequality, with comparator files `CourtadeKumar.lean` and `SoftChannel204.lean`.
- [D. P. Woodruff et al., *general-courtade-kumar-lean*](https://github.com/dpwoodru/general-courtade-kumar-lean) (GitHub, release v1.2 dated 2026-10-01). An independent Lean 4 proof of the Courtade–Kumar inequality $I(f(X);Y)\le 1-H(p)$, i.e. the universal bound in Corollary 1.2; it accompanies Chen–Gohari–Javanmard–Lin–Mirrokni–Nair–Woodruff (arXiv:2609.24931) rather than this paper.
- [Google DeepMind formal-conjectures, *FormalConjectures/Paper/CourtadeKumar.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Paper/CourtadeKumar.lean) (added by [PR #6688](https://github.com/google-deepmind/formal-conjectures/pull/6688), merged 2026-10-15). A formal statement of the Courtade–Kumar conjecture tagged "research solved", whose `formal_proof` link points to the Woodruff et al. Lean project; it does not reference the OpenAI papers.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Y. Polyanskiy and Y. Wu, *Strong data-processing inequalities for channels and Bayesian networks*](https://arxiv.org/abs/1508.06025) (arXiv:1508.06025, 2015/2016). Introduces the $F_I$-curve as the best possible non-linear SDPI for a channel, a statement of the same kind as Theorem 1.1's bound on $I(U;Y)$ in terms of $I(U;X)$ for the uniform-input product BSC.
- [V. K. Ky and T. Tran, *Stability of the Courtade-Kumar inequality*](https://arxiv.org/abs/2609.31797) (arXiv:2609.31797, 25 Sep 2026). Proves dimension-independent stability: functions whose information is close to the dictator value are close to signed dictators, which relates to the equality and strict-improvement statements in Corollary 1.2.

## Digests and expositions
- [AI Proved What?, *The best bit? The Courtade–Kumar and Hellinger conjectures*](https://aiprovedwhat.com/episodes/119-courtade-kumar-hellinger-conjectures/) (Episode 119, October 2026). This AI-assisted video and transcript explain both manuscripts’ claims and proof strategies and distinguish the contraction paper’s Lean scope from the Hellinger paper’s exact-arithmetic certificates. [AI-generated per source] [family-level]

## News and blogs
- None found.
