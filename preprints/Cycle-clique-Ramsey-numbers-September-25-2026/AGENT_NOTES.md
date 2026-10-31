# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- None found.

## Comments and discussion
- [anxkhn, bocowgill, mo271 (formal-conjectures contributors and reviewers), *feat(ErdosProblems/551): record the full Ramsey formula*](https://github.com/google-deepmind/formal-conjectures/pull/6992) (google-deepmind/formal-conjectures PR #6992, 8–11 October 2026, open as of 2026-10-21). The PR cites the paper's main theorem to mark `erdos_551` as solved; reviewers discuss whether it covers the full parameter range and non-induced containment definitions and ask for a pinned `formal_proof` link with exactly matching statements, while the author notes the proof's axiom closure has not been checked.

## Formalization
- [OpenAI math release, *Lean scope notes for family 189: Cycle–clique Ramsey numbers*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/189.md) (lean/docs/189.md, 2026-10-06). The release's Lean formalization states $R(C_m,K_n)=(m-1)(n-1)+1$ for all $m\ge n\ge3$ except $(3,3)$, and $R(C_3,K_3)=6$, covering the paper's full main theorem; the comparator statement is in `CycleCliqueRamsey.lean`.
- [Google DeepMind formal-conjectures, *FormalConjectures/ErdosProblems/551.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/551.lean) (formal-conjectures, accessed 2026-10-21). An independent Lean statement of the Erdős–Faudree–Rousseau–Schelp conjecture (Erdős Problem 551), still tagged `research open` with `sorry`, which also contains a "sufficiently large $n$" variant attributed to Keevash–Long–Skokan.
- [byclaude, *Bridge551.lean*](https://gist.github.com/byclaude/6213323d9766ee5f4e036ecd8fbce9a3) (GitHub gist, 2026-10-22). Copies formal-conjectures' `graphRamsey` and both `erdos_551` statements verbatim and proves them from `OAI.CycleClique.main`, with `#print axioms` giving `propext`, `Classical.choice`, `Quot.sound`, two negative controls, and a `leanchecker --fresh` run over the 182-module closure; it was not compiled in formal-conjectures' own environment, so it "checks a verbatim copy of the statement, not FC's constant." [AI-generated per source]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Cheng, Chen, Zhang, Ng, *The Ramsey numbers for a cycle of length six or seven versus a clique of order seven*](https://research.polyu.edu.hk/en/publications/the-ramsey-numbers-for-a-cycle-of-length-six-or-seven-versus-a-cl/) (Discrete Math. 307 (2007) 1047–1053, doi:10.1016/j.disc.2006.07.036). Proves $R(C_7,K_7)=37$, the diagonal case of the $n=7$ range that the paper's introduction attributes to Chen–Cheng–Zhang (2008); not in the paper's bibliography.
- [Radziszowski, *Small Ramsey Numbers*](https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1) (Electron. J. Combin. Dynamic Survey DS1, revision #18, 2026-04-24). Section 4.2, "Cycles versus complete graphs," compiles known values and bounds of $R(C_m,K_n)$, relevant to the paper's account of earlier cases ($n\le7$ and $n=8$); not in the paper's bibliography.

## Digests and expositions
- [Latent Seminar, *Exact cycle–clique Ramsey numbers*](https://lowrank.github.io/latent-seminar/OpenAI-Math/189-cycle-clique-ramsey) (2026-10-07). Explains independent-set expansion, optimal path systems and the 3,099-pattern remainder, and states that it did not execute the finite checks, build Lean or verify manuscript-to-formal-statement equivalence.
- [Gradient Damage, *Circulant Hadamard Conjecture, Cycle–Clique Ramsey Numbers and 7 More in Combinatorics*](https://gradientdamage.com/videos/circulant-hadamard-conjecture-cycle-clique-ramsey-numbers-and-7-more/) (video compilation, 2026-10-15). The chapter beginning at 1:02 introduces this paper's cycle–clique result; the accompanying page describes the animations as illustrations rather than proofs.

## News and blogs
- [Thomas Bloom (erdosproblems.com), *Erdős problems in the OpenAI proofs*](https://www.erdosproblems.com/forum/thread/blog:10) (erdosproblems.com blog, 2026-10-08). The post has a section on Problem 551 that summarizes the paper's claimed result as the Erdős–Faudree–Rousseau–Schelp conjecture and notes that "This proof has been formalised."
