# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [acprk (GitHub), *Remark R5: Thorp shuffle 1600d → 24d*](https://github.com/acprk/openai-math-remarks/blob/main/remarks/R5-thorp-24d) (openai-math-remarks, local draft, undated). Uses this paper's Theorem 1.1 (Hilbert–Schmidt transfer) with different block counts in the two factors to claim Thorp mixing after 24d shuffles; asymptotic, not formalized, reviewed only by AI. [AI-generated per source]
- [acprk (GitHub), *Remark R25: Swap-or-not constants C_u computed exactly*](https://github.com/acprk/openai-math-remarks/blob/main/remarks/R25-swapornot-cu-constants) (openai-math-remarks, 10 Oct 2026). Claims exact or numerical values of this paper's C_u = sup_m Σ_{λ⊢m} D_λ^{−u} for u = 1, 1/2, 3/10, 1/5, 3/20 (for example C₁ = 473/144) and a lower bound for u = 1/10, where the paper proves finiteness; computer-assisted, not formalized, reviewed only by AI. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 238*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/238.md) (lean/docs/238.md, 2026). States that the formalization covers the finite estimate turning coset-mass bounds for b blocks into Hilbert–Schmidt and operator-norm Fourier bounds (PartialPermutation.lean); the asymptotic statement about the product of two random permutations is outside its scope. [family-level]
- [Carlos Toledo, cert-machine, *OpenAI math statement audit: family 238*](https://raw.githubusercontent.com/carlostoledo1891/cert-machine/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-statements.json) (audit of release fd4aeeb, October 2026). Assesses the full-permutation mixing headline as matching ThorpRemaining’s statement, while checking the OccupiedOverlap and SpinAngle definition holes separately; this is a statement assessment, not a certificate of the manuscripts’ proofs. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Y. Jiang, *A subquadratic upper bound for the mixing time of the Thorp shuffle*](https://arxiv.org/abs/2610.18884) (arXiv:2610.18884, 3 Oct 2026). Independent preprint on Thorp-shuffle mixing that also uses representation-theoretic estimates, reaching order d^{5/3}; relevant to the family's application of this transfer. It does not mention the release. [family-level]

## Digests and expositions
- [Latent Seminar, *Optimal logarithmic mixing of the Thorp shuffle*](https://lowrank.github.io/latent-seminar/OpenAI-Math/238-thorp-shuffle) (expository notes, 2026-10-06). Outlines all twelve manuscripts’ proof methods and formalization boundaries, explicitly disclaiming independent full-proof verification. [family-level]
- [heyprof, *Thorp shuffle: how often until the deck is random?*](https://www.heyprof.app/en/demo/thorp-mischen) (interactive exposition, undated). Illustrates the family’s full-deck mixing question with small-deck distributions, single-card marginals, and the support bound. [family-level]

## News and blogs
- None found.
