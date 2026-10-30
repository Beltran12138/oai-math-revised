# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [P. M. Aronow, Patrick Lopatto, *Lower and Upper Bounds for Glauber Dynamics from Typical States of the Low-Temperature Sherrington–Kirkpatrick Model*](https://hexagonmath.org/abs/2610.00402v1) (hexagon:2610.00402v1, 20 Oct 2026). Follows this paper's proof structure and improves the typical-start lower bound from time exp(n^{1/10000}) to exp(A_β n^{7/30}) for every fixed β > 1, using a three-replica comparison with a cubic pressure deficit. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *Family 227 Lean scope*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/227.md) (lean/docs/227.md, 2026-10-06). States that the release's Lean development proves the main theorem for fixed $\beta>1$: at time $\exp(n^{1/10000})$, the expected Gibbs mass of starts still farther than 1/4 from equilibrium tends to one, for both per-site continuous time and discrete update attempts (comparator `SKBarriers.lean`). [family-level]
- [P. M. Aronow, Patrick Lopatto, *Lower and Upper Bounds for Glauber Dynamics from Typical States of the Low-Temperature Sherrington–Kirkpatrick Model*](https://hexagonmath.org/abs/2610.00402v1) (hexagon:2610.00402v1, 20 Oct 2026). Reports a Lean 4 formalization of the strengthened n^{7/30} barrier; the source says it uses a weaker form of the local expansion than the written proof. [AI-generated per source]
- [P. M. Aronow, *fluctuations-palomar*](https://github.com/pmaronow/fluctuations-palomar) (GitHub repository, registered in Palomar as PALOMAR-2026-10-21-000025, 21 Oct 2026). Lean 4 source for the Aronow–Lopatto strengthening of this paper's barrier: Theorem 1.1 gives exponent 7/30 for both clocks and thresholds below 1/2, and Corollary 1.2 gives coefficient one for every κ < 7/30, without the endpoint. The README reports that the replay for Corollary 1.7, a separate pressure statement, is still pending. [AI-generated per source]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- [Latent Seminar, *SK dynamics across the temperature transition*](https://lowrank.github.io/latent-seminar/OpenAI-Math/227-sk-dynamics) (2026-10-06). Explains the eight companions and selected proof mechanisms without independently verifying their proofs. [family-level]

## News and blogs
- None found.
