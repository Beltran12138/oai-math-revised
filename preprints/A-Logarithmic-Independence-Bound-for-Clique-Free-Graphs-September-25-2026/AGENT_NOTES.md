# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Kaizhe Chen, *A note on the logarithmic exponent of Ramsey number r(4,t)*](https://arxiv.org/abs/2610.15293) (arXiv:2610.15293, 11 October 2026). Cites this paper for its Lemma 1.3, the bound α(G) ≥ c_s n log d/d for K_s-free graphs, and combines it with the release's r(s,t) preprints to derive r(4,t) = t³/(log t)^(2+o(1)); the note says it is for informal circulation only.
- [Ross J. Kang, *Ode to the Ajtai-Erdős-Komlós-Szemerédi conjecture*](https://zenodo.org/records/23351325) (Zenodo working paper, DOI 10.5281/zenodo.23351325, 13 October 2026). Its abstract bounds the mean size of a uniformly chosen independent set in K_r-free graphs, r ≥ 4, by an absolute constant multiple of n log d/(rd), and the erdosproblemaday review below describes it as adapting Sections 2–5 of this paper and reporting no error.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release (mirrored at mathcommunity/oai-math-revised), *lean/docs/184.md*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/184.md) (release Lean scope note, 2026-10-06). Gives the scope of the release's Lean formalization of Theorem 1.1, the c_r n log d/d bound for K_r-free graphs with r ≥ 4 and average degree d ≥ 2, with comparator statement [CliqueFreeLog.lean](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/CliqueFreeLog.lean).
- [google-deepmind/formal-conjectures, *ErdosProblems/802.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/802.lean) (added by [PR #7165](https://github.com/google-deepmind/formal-conjectures/pull/7165), merged 20 October 2026). An independent Lean statement of Erdős Problem 802, the conjecture Theorem 1.1 addresses, with AEKS, Shearer, r=3 and Alon variants; at the time of access the main statement is still tagged open and the PR does not mention this paper.
- [Erdős Problems (erdosproblems.ai), *OpenAI's logarithmic independence bound for clique-free graphs*](https://erdosproblems.ai/wiki/problems/extremal_graph_theory/E0802/claims/2026_09_25_openai) (updated 2026-10-08). Reports building the release's Lean theorem and comparator, checking axioms and statement fingerprints, and auditing the formulation against Problem 802, while explicitly recording no outside review or independent acceptance.
- [byclaude, *Erdős 802: OpenAI's Lean proof of the AEKS bound + a bridge to erdos_802 (every r, every average degree)*](https://github.com/google-deepmind/formal-conjectures/issues/7520) (google-deepmind/formal-conjectures issue #7520, 22 October 2026, with [bridge gist](https://gist.github.com/byclaude/d348622f40352075e0ab938994cfe4fc)). Reports a kernel replay of the release's 31 Lean modules with only standard axioms and a Lean bridge deriving a verbatim copy of the formal-conjectures `erdos_802` statements, including small clique sizes and average degrees below two, from this paper's formalized theorem. The bridge is proved in OpenAI's Lean environment rather than the formal-conjectures environment, and the issue states that no human has reviewed the mathematics. [AI-generated per source]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [N. Bansal, A. Gupta, G. Guruganesh, *On the Lovász Theta function for Independent Sets in Sparse Graphs*](https://arxiv.org/abs/1504.04767) (arXiv:1504.04767, STOC 2015). Gives an improved Ramsey-type bound on the independence number of K_r-free graphs for large r, made algorithmic via an SDP, which may be relevant to the paper's remark that its proof makes no claim of an efficient algorithm.

## Digests and expositions
- [Latent Seminar, *Forbidden subgraphs, independence, and correspondence coloring*](https://lowrank.github.io/latent-seminar/OpenAI-Math/184-forbidden-subgraph-coloring) (2026-10-07). Explains both manuscripts' weighted triangle estimates and vertex splitting, including the additional participation bound needed for correspondence coloring, while explicitly disclaiming independent verification of the complete proofs. [family-level]
- [AI Proved What?, *Forbid a clique, gain a log?*](https://aiprovedwhat.com/episodes/184-correspondence-coloring-fixed-forbidden-subgraph/) (Episode 184, October 2026). Provides an animated exposition and transcript covering both claimed bounds, examples distinguishing list and correspondence coloring, and the stated formalization scope. [AI-generated per source] [family-level]

## News and blogs
- [Thomas Bloom, *Erdős problems in the OpenAI proofs* (erdosproblems.com blog)](https://www.erdosproblems.com/forum/thread/blog:10) (8 October 2026). Its section on Problem 802 states the release's claimed bound for K_r-free graphs, r ≥ 4, says it would prove the Ajtai–Erdős–Komlós–Szemerédi conjecture and improve Shearer's bound, and notes "This proof has been formalised."
