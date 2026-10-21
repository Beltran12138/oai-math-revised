# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Zero entropy does not guarantee a smooth positive-volume model* (Lean scope note)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/152.md) (lean/docs/152.md, release of 6 October 2026). The release's scope note says the formalized statement covers a finite-entropy system with no smooth positive-volume model, and that the paper's stronger zero-entropy conclusion is outside it. [family-level]
- [OpenAI, *SmoothObstruction.lean* (comparator statement)](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/SmoothObstruction.lean) (openai/math, October 2026). This is the comparator statement `SmoothObstruction.main`: there is a standard nonatomic ergodic system with `FiniteKSEntropy` and `¬ HasSmoothPositiveVolumeModel`, stated with a `sorry` body as a challenge.
- [OpenAI, *OAI/Dynamics/SmoothObstruction/Main.lean*](https://github.com/openai/math/blob/main/lean/OAI/Dynamics/SmoothObstruction/Main.lean) (openai/math, October 2026). This module states and proves the finite-entropy theorem `main` using imported modules (`Counting`, `BoundaryDensity`, `Obstruction`), and zero entropy is not part of the formal statement.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [B. Fayad, M. Saprykina, A. Windsor, *Nonstandard smooth realizations of Liouville rotations*](https://arxiv.org/abs/math/0608322) (arXiv:math/0608322, August 2006). Its introduction states the general question "whether every finite entropy automorphism of a Lebesgue space has a smooth realization", which is the question Theorem 1.1 answers negatively for smooth positive densities.
- [B. Fayad, A. Katok, *Constructions in elliptic dynamics*](https://arxiv.org/abs/math/0501362) (arXiv:math/0501362, January 2005). This is a survey of the Anosov–Katok approximation-by-conjugation method for building smooth volume-preserving systems with prescribed ergodic properties, which is background for the paper's zero-entropy obstruction.

## Digests and expositions
- [Latent Seminar, *Zero entropy and the obstruction to smooth positive-volume models*](https://lowrank.github.io/latent-seminar/OpenAI-Math/152-smooth-realization-obstruction) (2026-10-06). This exposition explains the smooth-density requirement, the switching estimate and symbolic compatibility obstruction, and the finite-entropy formalization scope, explicitly disclaiming independent verification of the complete proofs. [family-level]

## News and blogs
- None found.
