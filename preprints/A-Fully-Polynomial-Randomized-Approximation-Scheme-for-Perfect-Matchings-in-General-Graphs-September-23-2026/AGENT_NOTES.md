# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Chenghua Liu, Boning Meng, *A simplified proof of the FPRAS for counting perfect matchings*](https://arxiv.org/abs/2610.26803) (arXiv:2610.26803, 19 Oct 2026). Gives a simplified proof of this paper's FPRAS by establishing the comparison argument of its Sections 4–6 on the original vertex set without auxiliary vertices and tree constructions, while citing and reusing its encoding, replication and mixing/finite-precision results (Lemma 6.4, Lemma 7.2, Theorem 7.3, Section 9).

## Expert comments and discussion
- [microprediction, comment in *Add OpenAI results page with applied and difficulty scores* (microprediction/pure PR #20)](https://github.com/microprediction/pure/pull/20) (GitHub, 7 Oct 2026). A correction to a third-party catalogue note on item 113 that separates the earlier Jerrum–Sinclair FPRAS for the monomer–dimer partition function from the newly claimed FPRAS for perfect matchings in general graphs.

## Formalization
- [OpenAI, *Approximate counting and entropy of perfect matchings: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/113.md) (OpenAI math release, 2026-10-06). Describes the formalized FPRAS statement for every finite simple graph (a fixed randomized machine with worst-case polynomial bit time and exact zero detection), with comparator statement `MatchingFPRAS.lean`. [family-level]

## Related prior literature mentioned by others
- [Martin Dyer and Haiko Müller, *Counting Perfect Matchings and the Switch Chain*](https://doi.org/10.1137/18M1172910) (SIAM Journal on Discrete Mathematics 33(3), 1146–1174, 2019). Cited by Liu and Meng's follow-up for rapid mixing of the switch chain on quasimonotone graphs and slow-mixing examples in a larger hereditary class, explaining the limitations of two-edge switches for the general problem.

## Possibly relevant literature (found by the agent, not checked)
- [Farzam Ebrahimnejad, Ansh Nagda, Shayan Oveis Gharan, *Counting and Sampling Perfect Matchings in Regular Expanding Non-Bipartite Graphs*](https://arxiv.org/abs/2103.08683) (arXiv:2103.08683, ITCS 2022). Polynomial-time sampling and counting via the Jerrum–Sinclair chain for regular strong-expander non-bipartite graphs, relevant to the introduction's survey of non-bipartite special cases.
- [Alexander Barvinok, *Approximating permanents and hafnians*](https://arxiv.org/abs/1601.07518) (arXiv:1601.07518, Discrete Analysis 2017). Quasi-polynomial approximation of log-hafnians for matrices with entries in [δ,1], relevant to the paper's comparison with density-restricted earlier results.
- [Yeganeh Alimohammadi, Nima Anari, Kirankumar Shiragur, Thuy-Duong Vuong, *Fractionally Log-Concave and Sector-Stable Polynomials: Counting Planar Matchings and More*](https://arxiv.org/abs/2102.02708) (arXiv:2102.02708, 2021). FPRAS for counting matchings of a given size in planar, not necessarily bipartite graphs, relevant to the paper's corollary on fixed-cardinality matchings.

## Digests and expositions
- None found.

## News and blogs
- None found.
