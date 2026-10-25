# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [OpenAI, *Nonuniqueness with local conservation for the hard-sphere Boltzmann equation*](https://github.com/openai/math/blob/main/preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/paper.pdf) (OpenAI Math Release preprint, 5 October 2026). This companion reuses the September concentrating-jet mechanism and claims a new global continuation with exact local mass, momentum and energy conservation and polynomially weighted collision integrability on every bounded time interval. [AI-generated per source] [cites earlier version]

## Comments and discussion
- [John Evans, *Comment on Boltzmann nonuniqueness with exact local conservation*](https://www.linkedin.com/posts/johnaevans_github-openaimath-activity-7513546545980440576-SNmC) (LinkedIn, October 2026). In notes described as ChatGPT-assisted genealogy rather than an independent proof check, Evans compares the jet-and-seed construction and its later conservation refinement with instability methods and concentration/gluing strategies. [family-level]

## Formalization
- [OpenAI math release, *Lean scope note for family 363*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/363.md) (lean/docs/363.md, release of 2026-10-06). The scope note names this paper as the one the formalization accompanies, describing the formalized statement as nonuniqueness of global renormalized solutions with local mass and total momentum conservation, global energy and entropy-dissipation inequalities, and strong L^1 continuity on a common initial interval; it excludes the October local-conservation refinements. [family-level]
- [OpenAI math release, *OAI/MathematicalPhysics/Boltzmann/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/MathematicalPhysics/Boltzmann/Main.lean) (openai/math, commit adc7f12). States the theorem `BoltzmannNonuniqueness.nonuniqueness`: two `AdmissibleGlobal` evolutions from one datum with bounded velocity support, both satisfying `StrongEarly T`, which differ at some time in [0,T]; the proof is imported from `UnconditionalMainProof`. [family-level]
- [OpenAI math release, *ComparatorChallenges/BoltzmannNonuniqueness.lean*](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/BoltzmannNonuniqueness.lean) (openai/math). The comparator statement linked from the scope note: a self-contained Mathlib statement of the admissibility class and the nonuniqueness theorem, with the proof left as `sorry` in this file. Comparator challenge files leave the proof as `sorry` by design; `BoltzmannNonuniqueness.json` names the module `OAI.MathematicalPhysics.Boltzmann.Main` as the release's proof of this statement. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Lu, Wennberg, *Solutions with increasing energy for the spatially homogeneous Boltzmann equation*](https://research.chalmers.se/en/publication/21400) (Nonlinear Analysis: Real World Applications 3(2), 243–258, 2002). The paper contrasts its result with Wennberg's homogeneous nonuniqueness examples, which permit increasing energy; this later Lu–Wennberg work on energy-increasing homogeneous solutions is not in the bibliography.
- [Bodineau, Gallagher, Saint-Raymond, Simonella, *Derivation of the Boltzmann equation from hard-sphere dynamics (after Y. Deng, Z. Hani, and X. Ma)*](https://arxiv.org/abs/2602.04407) (arXiv:2602.04407, Séminaire Bourbaki Exposé 1247; v2 2026-10-14). This survey states that uniqueness of DiPerna–Lions renormalized solutions "is not known to date" and that it is unknown whether they satisfy the equation distributionally, which bears on the paper's framing and its remark that both solutions obey the unrenormalized equation on the early interval.
- [Modena, Székelyhidi, *Non-uniqueness for the transport equation with Sobolev vector fields*](https://arxiv.org/abs/1712.03867) (arXiv:1712.03867, 2017/2018). An analogous nonuniqueness result for linear transport with Sobolev fields, the other main DiPerna–Lions renormalized framework.

## Digests and expositions
- [Latent Seminar, *Boltzmann nonuniqueness and exact local conservation*](https://lowrank.github.io/latent-seminar/OpenAI-Math/363-boltzmann-nonuniqueness) (6 October 2026). This exposition explains the shared concentrating-jet, nonconcentration and branching mechanisms and the later bath-and-retirement continuation argument, while stating that it does not independently verify the complete proofs. [family-level]

## News and blogs
- None found.
