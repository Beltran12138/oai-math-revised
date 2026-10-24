# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Zinan Wang, *A Four-by-Four Obstruction to Polynomial Removal for Ordered Binary Matrices*](https://arxiv.org/abs/2610.15370) (arXiv:2610.15370 [cs.DM], 2026-10-11). Cites this paper and, following its tree-propagation approach, reports a fixed $4\times4$ pattern with no polynomial removal bound, with exact induced-copy counts, unrestricted editing distance and a Lean formalization.
- [Zinan Wang and Xinhao Yang, *h4-ordered-matrix-removal*](https://github.com/wzn1118/h4-ordered-matrix-removal) (GitHub repository, announced 2026-10-11). Manuscript and Lean 4 package for the $4\times4$ obstruction, copy counts and edit distance, with reproduction scripts; the README says the construction "builds on the tree-propagation approach" of this paper.
- [Erebos Labs, *ordered-matrix-removal-4x4*, release v1.0.0](https://github.com/erebos-labs/ordered-matrix-removal-4x4/releases/tag/v1.0.0) (GitHub release, 2026-10-09; [v1.1.0](https://github.com/erebos-labs/ordered-matrix-removal-4x4/releases/tag/v1.1.0) claims the exact repair distance $m^2$). Lean-checked obstruction for the $4\times4$ pattern with rows 0110, 1001, 1010, 0111, crediting this paper's signed-tree construction; it says its reviews were AI-assisted.
- [Ryan Shea, *ordered-binary-matrix-removal*](https://github.com/shea256/ordered-binary-matrix-removal) (GitHub repository, README dated 2026-10-12; [PR #10](https://github.com/shea256/ordered-binary-matrix-removal/pull/10)). Claims the $3\times3$ pattern 011/101/110 has no polynomial removal bound, checked in Lean, with tree and propagation ideas credited to this paper's $66\times66$ construction; prepared "with Codex assistance", peer review pending. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 190*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/190.md) (lean/docs/190.md, 2026-10-06). States the formalized failure of every polynomial removal bound for an explicit $66\times66$ pattern, with independently increasing row and column indices and edits in both directions, and links the comparator statement.
- [OpenAI math release, *MatrixRemoval.lean* (comparator statement)](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/MatrixRemoval.lean) (openai/math, commit adc7f12). Lean statement `no_polynomial_removal_bound` for the fixed pattern `fixedH`; the proof is `sorry` here and supplied in a separate release module.

## Related prior literature mentioned by others
- [Henry Towsner, *A Removal Lemma for Ordered Hypergraphs*](https://arxiv.org/abs/2101.09769) (arXiv:2101.09769, 2021-01-24). The [follow-up manuscript's background discussion](https://raw.githubusercontent.com/wzn1118/h4-ordered-matrix-removal/main/paper/additions/context.tex) cites this qualitative removal theorem as a comparison for the quantitative failure studied in this paper.

## Possibly relevant literature (found by the agent, not checked)
- [Lior Gishboliner and Borna Šimić, *Polynomial removal lemma for ordered matchings*](https://arxiv.org/abs/2307.01652) (arXiv:2307.01652, 2023, rev. 2025). Proves polynomial removal for ordered matchings in ordered graphs, relevant to the paper's contrast with the ordered-graph model of Gishboliner–Tomon.

## Digests and expositions
- None found.

## News and blogs
- None found.
