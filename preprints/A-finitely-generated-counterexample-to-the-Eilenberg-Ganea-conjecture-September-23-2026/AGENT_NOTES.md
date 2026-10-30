# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- None found.

## Comments and discussion
- [Grigori Avramidi, *Comment #243 on “The Mathocalypse”*](https://scottaaronson.blog/?p=10169) (Shtetl-Optimized, 2026-10-10). Identifies result 249 as the longstanding Bestvina–Brady candidate and describes its small SU(2)-holonomy argument as an alternative to proving the epsilon-map conjecture or Whitehead’s conjecture.
- [Grigori Avramidi, *Comment on “The Curve Bends You”*](https://thezvi.substack.com/p/the-curve-bends-you/comment/355812478) (Substack, 2026-10-08). Discusses the finitely generated Bestvina–Brady example and suggests investigating other, finitely presented candidates.
- [Xiaolei Wu, quoted in *100+ reactions to 100+ solutions*](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/) (Proofs and Prompts, 2026-10-08). In a short reaction to the group theory section of the release, Wu writes: "Eilenberg–Ganea is false—not so surprising, perhaps, but how?", and distinguishes the result from the still-open Whitehead conjecture.

## Formalization
- [OpenAI math release, *A finitely generated Eilenberg–Ganea counterexample: Lean scope notes*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/249.md) (release Lean docs, 2026-10-06). Describes the formalization as constructing a finitely generated, residually finite group with integral cohomological dimension two that has a three-dimensional classifying space but no two-dimensional one, and links the comparator statement EilenbergGanea.lean. [family-level]
- [OpenAI math release, *ComparatorChallenges/EilenbergGanea.lean*](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/EilenbergGanea.lean) (openai/math, October 2026). This is the comparator statement `source_main`: the height kernel of the Artin group on `seedGraph` is finitely generated and residually finite, has `cohomologicalDimension = 2`, and has a 3-dimensional but no 2-dimensional `HasClassifyingSpace`, with no bound on the number of cells.
- [franzhusch, *Eilenberg-Ganea Conjecture* (issue #1794)](https://github.com/google-deepmind/formal-conjectures/issues/1794) (google-deepmind/formal-conjectures, opened 2026-01-20). An open request, written before the release, to add the conjecture's statement; it is labelled "needs-prerequisites" because Mathlib lacks group cohomological dimension and K(G,1) complexes, and it has no comments about this paper.
- [MathVet, *Formalization fidelity assessment, family 249*](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/fidelity-table.csv) (MathVet, October 2026). This model-assisted assessment records a sandboxed Comparator pass and judges the statement to cover the advertised result, explicitly examining the projective-dimension definition and the absence of a cell-cardinality restriction on classifying spaces. [family-level] [AI-generated per source]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Elton Pasku, *An answer to the Whitehead asphericity question*](https://arxiv.org/abs/2107.12293) (arXiv:2107.12293, v1 2021-07-26, v2 2026-10-05). Claims a positive answer to Whitehead's asphericity question; under the Bestvina–Brady alternative cited in the paper's history section (BB1997, Theorem 8.7), such an answer would bear on the same Eilenberg–Ganea/Whitehead dichotomy.
- [Noel Brady, Ian Leary, Brita Nucinkis, *On algebraic and geometric dimensions for groups with torsion*](https://pure.royalholloway.ac.uk/en/publications/on-algebraic-and-geometric-dimensions-for-groups-with-torsion) (J. London Math. Soc. 64(2), 489–500, 2001). Gives counterexamples to the proper-action (Bredon) analogue of the Eilenberg–Ganea conjecture, the variant that the paper's introduction explicitly sets aside ("no family of subgroups or proper-action variant is involved").
- [Ian J. Leary, Nansen Petrosyan, *On dimensions of groups with cocompact classifying spaces for proper actions*](https://arxiv.org/abs/1504.02704) (arXiv:1504.02704, 2015; revised 2017). Gives groups whose virtual and Bredon cohomological dimensions are both two but which have no 2-dimensional contractible proper G-CW-complex; this is background for the Coxeter candidates that the introduction compares with Bestvina–Brady groups via LP2026.
- [Laurent Bartholdi and Roman Mikhailov, *Finite Chains of Two-Complexes and Acyclic Covers*](https://arxiv.org/abs/2610.10074) (arXiv:2610.10074, 2026-10-07). This AI-assisted work on acyclic regular covers and finite chains of two-complexes, including an SL(2,5) presentation complex, offers a comparison for the manuscript’s acyclic seed and its discussion of Whitehead’s asphericity problem.
- [T. Tâm Nguyễn-Phan, *A remark on ε-maps in dimension 1*](https://arxiv.org/abs/1907.12063) (arXiv:1907.12063, 2019-07-28). Studies a one-dimensional version of the Bestvina–Brady ε-map conjecture and recalls that the conjecture for a spine of the Poincaré homology sphere would make Eilenberg–Ganea false, which is background for the paper's use of BB1997 Theorem 8.7 and its small-label transport in place of that conjecture.

## Digests and expositions
- [AI Proved What?, *Dimension two, or three? An AI preprint claims a counterexample to the Eilenberg–Ganea conjecture*](https://aiprovedwhat.com/episodes/249-eilenberg-ganea-counterexample/) (Episode 249, October 2026). Provides a short video and transcript explaining the claimed dimension gap, the Bestvina–Brady construction and the small quaternion-labeling obstruction. [AI-generated per source]
- [Open Mathematics Courses, *A finitely generated counterexample to the Eilenberg–Ganea conjecture*](https://kokunoyumeto.github.io/open-math-courses-public/courses/eilenberg-ganea-counterexample/) (undated). Offers eleven lessons with proofs and exercises covering the manuscript’s argument, explicitly described as written and self-checked by Claude Opus 5.5 with independent review incomplete. [AI-generated per source]

## News and blogs
- None found.
