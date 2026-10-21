# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Erik D. Demaine, Stefan Langerman, *Tiling 3D by Translates of a Single Polycube is Undecidable*](https://arxiv.org/abs/2610.12392) (arXiv:2610.12392, 8 Oct 2026). Proves that translational tiling of 3D space by a single face-connected polycube is undecidable (co-RE-complete), using "a cyclic encoding adapted from OpenAI's 3D aperiodic tile" with decorated two-prime Sudoku constraints; it cites this preprint as reference [15].

## Expert comments and discussion
- [Quanta Magazine "Transformation" (Konstantin Kakaes's column), *Cracks appear in OpenAI's wall of proofs*](https://www.quantamagazine.org/update/168049/) (Quanta Magazine, 9 Oct 2026). A short news item on early reactions to the release that links this preprint as its three-dimensional aperiodic tile example and quotes Chaim Goodman-Strauss (Museum of Mathematics) saying it has some novel ideas but is "unnecessarily difficult to read".

## Formalization
- [OpenAI math release, *Lean scope notes for family 155*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/155.md) (lean/docs/155.md, 2026-10-06). Describes the formalized statement: the ℤ³ tile with no complement invariant under a finite-index subgroup, the ℝ³ unit-cube thickening with no fully periodic a.e. tiling under arbitrary real translations, and minimality of dimension three; it links the comparator statement [PeriodicTilingThree.lean](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/PeriodicTilingThree.lean) (`periodic_tiling_counterexample_and_minimality`, with a `sorry` placeholder as comparator challenge files do).
- [OpenAI, *Counterexample.lean*](https://github.com/openai/math/blob/main/lean/OAI/Geometry/PeriodicTiling/Counterexample.lean) (openai/math, lean/OAI/Geometry/PeriodicTiling/). The release's proof file for `OAI.PeriodicTilingThree.periodic_tiling_counterexample_and_minimality`; the file itself has no `sorry`, and its imported lemmas were not inspected.
- [Erik D. Demaine and Stefan Langerman, *translation-tiling-paper: paper and Lean proof*](https://github.com/edemaine/translation-tiling-paper) (GitHub, accessed 2026-10-21). The follow-up's repository reports a complete Lean formalization of its Wang-to-polycube reduction, adapting and reproving OpenAI's cyclic gadgets and using Meyerovitch–Sanadhya–Solomon for arbitrary-tiling descent. [family-level]

## Related prior literature mentioned by others
- [Yoonhu Kim, *Undecidability of Translational Tiling with 2 Polycubes*](https://arxiv.org/abs/2508.11725v2) (arXiv:2508.11725v2, 2026-08-10). Demaine and Langerman's follow-up uses its Theorem 2.5 to make the tile from their adaptation of OpenAI's encoding face-connected while preserving dimension, tile count, and tileability. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [Abhishek Khetan, *A Periodicity Result for Tilings of ℤ³ by Clusters of Prime-Squared Cardinality*](https://arxiv.org/abs/2109.14179) (arXiv:2109.14179, v3 16 Jun 2026). Gives weak periodicity of tilings of ℤ³ for tiles of prime-squared cardinality, a weaker notion than the full periodicity the paper rules out.
- [Hu Tan, Ying Zhang, *Periodic Tilings of Cardinality Twice a Prime or Nine in Arbitrary Dimension*](https://arxiv.org/abs/2609.26576) (arXiv:2609.26576, 22 Sep 2026). Proves that every finite tile of ℤ^d with cardinality 2q (q an odd prime) or 9 admits a fully periodic tiling, restricting which cardinalities a ℤ³ counterexample such as Theorem 1.1's tile T can have.
- [Rachel Greenfeld, Terence Tao, *Some variants of the periodic tiling conjecture*](https://arxiv.org/abs/2505.06757) (arXiv:2505.06757, 10 May 2025). Proves periodicity-type variants of the conjecture, including in ℤ², bearing on the positive results used to argue that three is the least lattice dimension.
- [Jaume de Dios Pont, Jan Grebík, Rachel Greenfeld, José Madrid, *Translational tilings by axis-parallel polygonal sets*](https://arxiv.org/abs/2610.15785) (arXiv:2610.15785, 11 Oct 2026). Shows that sets bounded by axis-parallel segments that tile the plane admit quasi-periodic tilings, related to the paper's remark that planar positive results do not settle arbitrary bounded measurable tiles (it does not mention this paper).
- [Rachel Greenfeld, *Translational tilings: structured or wild?*](https://arxiv.org/abs/2509.25576) (arXiv:2509.25576, 29 Sep 2025). A survey of translational tilings and the periodic tiling conjecture, describing the state of the field just before this paper's dimension-three claim.

## Digests and expositions
- [Latent Seminar, *Translational tilings without full periodicity*](https://lowrank.github.io/latent-seminar/OpenAI-Math/155-translational-aperiodicity) (2026-10-07). Explains the Sudoku encoding, stacking, and Euclidean rigidity arguments, distinguishing full periodicity from individual periods; the page states it has not independently verified the complete proofs. [family-level]

## News and blogs
- None found.
