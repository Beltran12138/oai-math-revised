# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [mo271, *ErdosProblems/181: `erdos_181` is true*](https://github.com/google-deepmind/formal-conjectures/issues/6906) (google-deepmind/formal-conjectures issue #6906, opened 7 October 2026, closed 11 October 2026). Argues that Theorem 1.1 of this paper matches the Lean statement `erdos_181` and proposes marking it solved; the issue says the comparison was prepared with AI assistance.

## Formalization
- [Yao Xu (cadamcat), *hypercube-ramsey-lean4*](https://github.com/cadamcat/hypercube-ramsey-lean4) (GitHub repository, 2026). An independent Lean 4/Mathlib formalization of Theorem 1.1, stated as `Erdos181.erdos_181`, which takes the cube graph, Ramsey number, finite Ramsey bounds and Lemma 2.1 from OpenAI's Lean library and formalizes the rest of the paper (Sections 3–18); the README says it was "Developed with AI assistance; all proofs are verified by the Lean 4 kernel." [AI-generated per source]
- [cadamcat, *feat(ErdosProblems/181): mark solved and link the formal proof*](https://github.com/google-deepmind/formal-conjectures/pull/7128) (google-deepmind/formal-conjectures PR #7128, merged 11 October 2026). Marks the unchanged statement `erdos_181` as solved and links Xu's v1.0.0 proof, reporting a fresh build, full kernel replay, Comparator statement checks and an axiom check limited to `propext`, `Classical.choice` and `Quot.sound`.
- [google-deepmind/formal-conjectures, *FormalConjectures/ErdosProblems/181.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/181.lean) (Lean file, current main). States $R(Q_n)\le C2^n$ as `erdos_181`, tagged `research solved`, linking the cadamcat formal proof and citing this paper; the proof body in this file itself is `sorry`.

## Related prior literature mentioned by others
- [Thomas Bloom, erdosproblems.com, *Problem 181*](https://www.erdosproblems.com/181) (last edited 16 October 2026). Cites Erdős [Er93] ("Some of my favorite solved and unsolved problems in graph theory") and an Erdős–Sós remark on whether $R(Q_n)/2^n\to\infty$; the paper's bibliography includes neither.
- [Konstantin Tikhomirov, *A remark on the Ramsey number of the hypercube*](https://arxiv.org/abs/2208.14568) (arXiv:2208.14568, 2022; revised 2024-03-02). Referenced in the Formal Conjectures entry and the manuscript; establishes the earlier bound $R(Q_n)=O(2^{(2-c)n})$ for an absolute $c>0$.
- [Bernard Lidický and Florian Pfender, *Semidefinite Programming and Ramsey Numbers*](https://arxiv.org/abs/1704.03592) (arXiv:1704.03592, 2017; revised 2020-09-11). Cited in [Erdős Problem a Day's working report](https://erdosproblemaday.com/report/181); determines $R(Q_3,Q_3)=13$, giving small-dimensional context for the paper's asymptotic bound.

## Possibly relevant literature (found by the agent, not checked)
- [D. Conlon, J. Fox and B. Sudakov, *Recent developments in graph Ramsey theory*](https://arxiv.org/abs/1501.02474) (arXiv:1501.02474, 2015). A survey whose Section 2.3 states the cube conjecture $r(Q_n)=O(2^n)$ as Conjecture 2.14 and reviews the sequence of upper bounds recounted in the paper's introduction.

## Digests and expositions
- [Latent Seminar, *Linear-order Ramsey numbers for hypercubes*](https://lowrank.github.io/latent-seminar/OpenAI-Math/171-hypercube-ramsey) (2026-10-07). Explains the paper's patch decomposition, common-neighbor lists and final Hall-obstruction estimates, and states that its proof outlines are not an independent verification of the complete proof. [family-level]

## News and blogs
- None found.
