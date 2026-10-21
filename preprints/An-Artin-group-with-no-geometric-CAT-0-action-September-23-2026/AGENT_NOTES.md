# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [frogscooper (GitHub handle), *artin-cat0-29*](https://github.com/frogscooper/artin-cat0-29) (GitHub repository, accessed 2026-10-21). Presents an edited version of this paper's argument with 11-strand instead of 40-strand braid blocks, reducing the example from 116 to 29 generators, with an adapted copy of the release's Lean project reported as axiom-clean, plus an 11-generator variant that the author says assumes a special case of van der Lek's theorem; the author says the new argument and Lean port were worked out with help from Claude. [AI-generated per source]

## Comments and discussion
- [Giulio Tiozzo, contribution to *100+ reactions to 100+ solutions*](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/) (Proofs and Prompts, 8 October 2026; updated 19 October 2026). Writes "I took their example #254 (an Artin group with no CAT(0) action): their group has 116 generators" and reports that Astra produced a 12-generator example in about ten minutes, which he uses to argue the papers were not reviewed by a human.

## Formalization
- [OpenAI math release, *Lean scope notes for family 254: Classifying spaces and geometric obstructions for Artin groups*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/254.md) (lean/docs/254.md, undated). States that the formalized result is the 116-generator example with off-diagonal labels in {2, 3, ∞}, admitting no proper cocompact isometric action on any nonempty proper CAT(0) space in any dimension. [family-level]
- [OpenAI math release, *ArtinCAT0.lean* comparator statement](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/ArtinCAT0.lean) (lean/ComparatorChallenges). The comparator statement file for this paper's main theorem (`main`), giving the explicit matrix and the non-existence of a geometric action.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [T. Haettel, *Virtually cocompactly cubulated Artin-Tits groups*](https://arxiv.org/abs/1509.08711) (arXiv:1509.08711; IMRN 2021). Proves that braid groups on n ≥ 4 strands are not virtually cocompactly cubulated; this is an obstruction to a restricted class of geometric CAT(0) actions, relevant to the paper's dimension-free obstruction and its use of braid-group blocks.
- [J. Huang, K. Jankiewicz, P. Przytycki, *Cocompactly cubulated 2-dimensional Artin groups*](https://arxiv.org/abs/1510.08493) (arXiv:1510.08493; Comment. Math. Helv. 91, 2016). Characterizes 2-dimensional and three-generator Artin groups that act geometrically on CAT(0) cube complexes; this is an earlier cubical-case obstruction for triangle-type subgroups like the paper's group T.

## Digests and expositions
- None found.

## News and blogs
- [David Roberts, *What even is mathematical output?*](https://thehighergeometer.wordpress.com/2026/10/12/what-even-is-mathematical-output/) (theHigherGeometer, 12 October 2026). Discusses Tiozzo's reported reduction of the CAT(0) example from 116 to 12 generators as part of a criticism of the release's exposition and refinement process.
