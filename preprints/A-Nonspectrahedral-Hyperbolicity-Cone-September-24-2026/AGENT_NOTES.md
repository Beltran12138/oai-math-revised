# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note 095: Hyperbolicity cones without semidefinite lifts*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/095.md) (lean/docs/095.md, release of 2026-10-06). The release's Lean scope note for the family; it covers this paper's Theorem 1.1, a degree-20 hyperbolic polynomial in 23 variables whose closed cone is not the PSD region of any finite real symmetric linear pencil.
- [OpenAI math release, *lean/OAI/Analysis/HyperbolicCones/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/HyperbolicCones/Main.lean) (commit adc7f12). Declares `OAI.Paper256.main_result` and `cone_not_spectrahedral`, stating the dimension, degree, normalization, real-rootedness and non-spectrahedrality claims of Theorem 1.1 (comparator statement in [HyperbolicCones.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/HyperbolicCones.lean)); the degree-16 reduced polynomial of Corollary 1.2 is not part of this statement.

## Related prior literature mentioned by others
- [Victor Vinnikov, *LMI Representations of Convex Semialgebraic Sets and Determinantal Representations of Algebraic Hypersurfaces: Past, Present, and Future*](https://arxiv.org/abs/1205.2286) (arXiv:1205.2286, 2012-05-10). Kevin Shu’s exposition cites this survey as background on earlier constructions of hyperbolic polynomials when introducing the manuscript’s nonspectrahedrality problem.

## Possibly relevant literature (found by the agent, not checked)
- [Nima Amini, Petter Brändén, *Non-representable hyperbolic matroids*](https://arxiv.org/abs/1512.05878) (arXiv:1512.05878, 2015). Discusses consequences for algebraic versions of the generalized Lax conjecture, bearing on the paper's distinction (Section 1.2) between determinantal representability of a polynomial and spectrahedrality of its cone.

## Digests and expositions
- [Kevin Shu, *A Digestion of A Counterexample to the Generalized Lax Conjecture*](https://www.quasicoherent.blog/posts/generalized_lax/) (Quasicoherent, 2026-10-12). Shu recasts the construction using quadratic families of positive maps and explains the nonspectrahedrality argument through extremal biquadratic forms and differentiated kernel-projection norm identities.
- [Latent Seminar, *Hyperbolicity cones: matrix descriptions, lifts, and obstructions*](https://lowrank.github.io/latent-seminar/OpenAI-Math/095-hyperbolicity-semidefinite-lifts) (2026-10-06). This exposition distinguishes the three manuscripts and outlines the nonspectrahedrality argument, the exact lift, and the separate local obstruction to all finite lifts, while disclaiming independent verification of the complete proofs. [family-level]
- [Claude Opus 5.5 / Open Mathematics Courses, *A nonspectrahedral hyperbolicity cone*](https://kokunoyumeto.github.io/open-math-courses-public/courses/a-nonspectrahedral-hyperbolicity-cone/index.html) (undated). Six lessons with proofs and exercises cover the Choi–Lam construction, the obstruction to spectrahedrality, and the companion exact lift of size 100 with 307 auxiliary variables. [AI-generated per source] [family-level]

## News and blogs
- [Carlos Toledo, *OpenAI’s math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (public audit report, finding G5 dated 2026-10-10). Finding G5 distinguishes the formalized nonspectrahedral cone, which the companion manuscript lifts, from the separate no-lift construction underlying the family’s Projected Lax claim. [family-level]
