# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [John Evans, *Comment on Boltzmann nonuniqueness with exact local conservation*](https://www.linkedin.com/posts/johnaevans_github-openaimath-activity-7513546545980440576-SNmC) (LinkedIn, October 2026). In notes described as ChatGPT-assisted genealogy rather than an independent proof check, Evans compares the jet-and-seed construction and its later conservation refinement with instability methods and concentration/gluing strategies. [family-level]

## Formalization
- [OpenAI math release, *Lean scope note for family 363*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/363.md) (lean/docs/363.md, release of 2026-10-06). The scope note covers only the September 23 companion paper and says that "later local-conservation refinements are outside" the formalized result, so this paper's Theorem 1.1 (exact local momentum and energy conservation) is not covered. [family-level]
- [OpenAI math release, *OAI/MathematicalPhysics/Boltzmann/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/MathematicalPhysics/Boltzmann/Main.lean) (openai/math, commit adc7f12). States the theorem `BoltzmannNonuniqueness.nonuniqueness`: two `AdmissibleGlobal` evolutions from one datum with bounded velocity support which differ at some time in an early interval, corresponding to the companion's weaker solution class. [family-level]
- [OpenAI math release, *ComparatorChallenges/BoltzmannNonuniqueness.lean*](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/BoltzmannNonuniqueness.lean) (openai/math). The comparator statement linked from the scope note: a self-contained Mathlib statement of the companion's admissibility class and nonuniqueness theorem, with the proof left as `sorry` in this file. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Lu, Wennberg, *Solutions with increasing energy for the spatially homogeneous Boltzmann equation*](https://research.chalmers.se/en/publication/21400) (Nonlinear Analysis: Real World Applications 3(2), 243–258, 2002). The paper contrasts its result with Wennberg's homogeneous nonuniqueness examples, which allow increasing energy; this later Lu–Wennberg work on energy-increasing homogeneous solutions is not in the bibliography.
- [Bodineau, Gallagher, Saint-Raymond, Simonella, *Derivation of the Boltzmann equation from hard-sphere dynamics (after Y. Deng, Z. Hani, and X. Ma)*](https://arxiv.org/abs/2602.04407) (arXiv:2602.04407, Séminaire Bourbaki Exposé 1247; v2 2026-10-14). This survey states that uniqueness of DiPerna–Lions renormalized solutions "is not known to date" and that it is unknown whether they satisfy the equation distributionally, which bears on the paper's framing and its strong collision integrability claim.
- [Modena, Székelyhidi, *Non-uniqueness for the transport equation with Sobolev vector fields*](https://arxiv.org/abs/1712.03867) (arXiv:1712.03867, 2017/2018). An analogous nonuniqueness result for linear transport with Sobolev fields, the other main DiPerna–Lions renormalized framework.

## Digests and expositions
- [Latent Seminar, *Boltzmann nonuniqueness and exact local conservation*](https://lowrank.github.io/latent-seminar/OpenAI-Math/363-boltzmann-nonuniqueness) (6 October 2026). This exposition explains the shared concentrating-jet, nonconcentration and branching mechanisms and the later bath-and-retirement continuation argument, while stating that it does not independently verify the complete proofs. [family-level]

## News and blogs
- None found.
