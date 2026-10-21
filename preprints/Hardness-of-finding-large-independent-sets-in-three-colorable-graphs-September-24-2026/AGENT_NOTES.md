# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *Hardness of coloring three-colorable graphs: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/106.md) (OpenAI Math Release, lean/docs/106.md, 2026). The scope note describes a formalized deterministic polynomial-time reduction from binary 3SAT with three-colorable completeness and independent-set density below each fixed 0 < δ < 1/3 in the unsatisfiable case, including the full adjacency-matrix output in the runtime bound, and points to a comparator file `IndependentSets.lean`.

## Related prior literature mentioned by others
- [Yumou Fei, Dor Minzer, Shuo Wang, *On the Hardness of 4-to-1 Games with Perfect Completeness*](https://arxiv.org/abs/2610.12378) (arXiv:2610.12378, 8 October 2026; also [ECCC TR26-179](https://eccc.weizmann.ac.il/report/2026/179/), 14 September 2026, revised 8 October 2026). Independent human proof of the 4-to-1 Games Conjecture; its Corollary 1.7 gives the 3-colorable vs. not k-colorable gap, and Corollary 1.9 gives small independent-set density with an 8-colorable completeness promise. The paper cites the ECCC version, and secondary coverage of family 106 mentions it alongside this result.

## Possibly relevant literature (found by the agent, not checked)
- [Marcin Wrochna, Stanislav Živný, *Improved hardness for H-colourings of G-colourable graphs*](https://arxiv.org/abs/1907.00872) (arXiv:1907.00872, SODA 2020). Proves NP-hardness of coloring k-colorable graphs with C(k,⌊k/2⌋)−1 colors for k ≥ 4, which is prior work on Corollary 1.2 (all fixed 3 ≤ k ≤ c) beyond the k = 3 results the introduction surveys.
- [Sangxia Huang, *Improved Hardness of Approximating Chromatic Number*](https://arxiv.org/abs/1301.5216) (arXiv:1301.5216, 2013). Proves NP-hardness of coloring K-colorable graphs with fewer than 2^{K^{1/3}} colors for large K, more prior unconditional work on the general-k case of Corollary 1.2.
- [David Karger, Rajeev Motwani, Madhu Sudan, *Approximate Graph Coloring by Semidefinite Programming*](https://arxiv.org/abs/cs/9812008) (arXiv:cs/9812008, JACM 1998). The original SDP coloring algorithm for 3-colorable graphs, from which the 2024–2026 algorithms cited in the paper's "algorithmic work" paragraph descend.

## Digests and expositions
- [Open Mathematics Courses / Claude Opus 5.5, *Large independent sets in three-colorable graphs*](https://kokunoyumeto.github.io/open-math-courses-public/courses/large-independent-sets-in-three-colorable-graphs/) (Open Mathematics Courses, undated). Six lessons with exercises explain this paper's phase-space construction, Lipschitz-function and answer-list arguments, alignment theorem, and coefficient test, explicitly retaining PCP and parallel repetition as external inputs and stating that independent review is incomplete. [AI-generated per source]

## News and blogs
- [postcutoff.com, *OpenAI model claims a proof of Khot's Unique Games Conjecture, with Lean formalization*](https://postcutoff.com/e/2026-10-06-unique-games-conjecture-openai/) (filed 7 October 2026). A release overview that lists result 106 as "NP-hardness of colouring 3-colourable graphs with any constant number of colours" and points to the Fei–Minzer–Wang ECCC report as stating a related consequence. [AI-generated per source]
