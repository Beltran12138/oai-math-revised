# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- [Kourovka Notebook (eds. E. I. Khukhro, V. D. Mazurov), *Unsolved Problems in Group Theory, 21st edition: updates file*, Problem 18.87](https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/10/21upd-3.pdf) (Kourovka Notebook update, 2026). Problem 18.87(a) (V. A. Roman'kov), the Kervaire–Laudenbach conjecture for independent systems over an arbitrary group, is marked "The conjecture is proved (AI solution confirmed by N. V. Bogachev: OpenAI, Preprint, 2026)". The entry links a [copy of this paper](https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/10/18-87.pdf); the nilpotent and solvable versions 18.87(b),(c) carry no solution mark.
- [Lvzhou Chen, reaction in *100+ reactions to 100+ solutions*, Proofs and Prompts](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/) (blog post, 8 Oct 2026, updated 19 Oct 2026). Chen, author of the cited Chen2026, writes "I spent a few years thinking about the Kervaire conjecture, Howie's conjecture (Problem 256) and related problems", and expresses interest in the new techniques while stating he has not understood the full details. [family-level]

## Formalization
- [OpenAI math release, *Lean scope notes for family 256* (`lean/docs/256.md`)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/256.md) (release Lean documentation, 6 Oct 2026). The notes describe a formalization of coefficient injectivity for a single unimodular relator in $A*\mathbb Z$, the companion Kervaire paper's theorem and a special case of this paper's claim; they list no formalization of the multi-relator nonsingular-system theorem. [family-level]
- [OpenAI, *lean/OAI/GroupTheory/Kervaire/Main.lean*](https://github.com/openai/math/blob/main/lean/OAI/GroupTheory/Kervaire/Main.lean) (github.com/openai/math, 2026). Proves `Kervaire.coefficient_injective` (one unimodular word) and `Kervaire.quotient_nontrivial`, i.e. the $m=n=1$ unimodular case that this paper extends. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [A. Klyachko and A. Thom, *New topological methods to solve equations over groups*](https://arxiv.org/abs/1509.01376) (arXiv:1509.01376; Algebr. Geom. Topol. 17 (2017), 331–353). Extends the Gerstenhaber–Rothaus compact-Lie-group method for equations over hyperlinear groups, which the paper's history section discusses via Pestov and Nitsche–Thom.
- [M. A. Mikheenko, *Infinite systems of equations in abelian and nilpotent groups*](https://arxiv.org/abs/2410.20729) (arXiv:2410.20729, 2024–2025). Studies infinite unimodular/nonsingular systems; may be relevant to the paper's Remark extending Theorem 1 to arbitrary sets of equations with independent exponent rows.

## Digests and expositions
- [Open Mathematics Courses, *Nonsingular systems of equations over groups*](https://kokunoyumeto.github.io/open-math-courses-public/courses/nonsingular-systems-over-groups/) (undated). Five-lesson exposition of the manuscript covering rational cohomology, simultaneous fixed spaces and the planar boundary obstruction; it identifies its author and self-checker as Claude Opus 5.5, with independent review incomplete. [AI-generated per source]

## News and blogs
- None found.
