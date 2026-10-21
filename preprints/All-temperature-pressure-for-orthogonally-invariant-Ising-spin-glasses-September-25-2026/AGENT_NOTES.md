# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *All-temperature pressure of orthogonally invariant Ising spin glasses: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/234.md) (lean/docs/234.md, OpenAI Math Release, 2026-10-06). The release's scope note covers zero-field and Wasserstein-field pressure limits at all positive temperatures, the ground-state limit, and random-spectrum and Gaussian-pattern specializations, and links the comparator statement `InvariantIsing.lean`. [family-level]
- [OpenAI, *InvariantIsing.lean (comparator statements)*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/InvariantIsing.lean) (openai/math, commit adc7f12). Lean 4 statements of 11 results matching the paper's theorems and corollaries, among them the Gaussian-pattern operator-norm limits; in this comparator file each one ends in `sorry`, as challenge statements do.
- [OpenAI, *Unconditional.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/InvariantIsing/Unconditional.lean) (openai/math, commit adc7f12). The solution module: it derives the unconditional theorems from conditional versions and from inputs proved in other files of the release, such as `haarConcentration_proved` and `panchenkoTalagrandFieldPair_proved`.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [G. Parisi and M. Potters, *Mean-Field Equations for Spin Models with Orthogonal Interaction Matrices*](https://arxiv.org/abs/cond-mat/9503009) (arXiv:cond-mat/9503009, J. Phys. A 28 (1995) 5267). Gives TAP equations and a replica count of metastable states for the random orthogonal Ising model, alongside the replica predictions the paper cites (Marinari–Parisi–Ritort; Cherrier–Dean–Lefèvre).
- [Zhou Fan, Yufan Li and Subhabrata Sen, *TAP equations for orthogonally invariant spin glasses at high temperature*](https://arxiv.org/abs/2202.09325) (arXiv:2202.09325, 2022-02-18; revised 2022-12-20). Characterizes the magnetization at high temperature through TAP equations and AMP convergence for the same orthogonally invariant Ising model, a possible comparison for the paper's external-field pressure formula.
- [A. Maillard, L. Foini, A. Lage Castellanos, F. Krzakala, M. Mézard and L. Zdeborová, *High-temperature Expansions and Message Passing Algorithms*](https://arxiv.org/abs/1906.08479) (arXiv:1906.08479, J. Stat. Mech. (2019) 113301). Derives free entropies for rotationally invariant couplings through Plefka-type expansions, which bears on how the paper's formula relates to replica-symmetric predictions expressed through the $R$-transform.

## Digests and expositions
- [Latent Seminar, *All-temperature pressure for invariant Ising spin glasses*](https://lowrank.github.io/latent-seminar/OpenAI-Math/234-invariant-spin-glasses) (2026-10-06). Explains the spectral transform, entropy functional, normalization conventions and selected upper-bound and cavity arguments, while explicitly stating that it does not independently verify the complete proofs. [family-level]

## News and blogs
- None found.
