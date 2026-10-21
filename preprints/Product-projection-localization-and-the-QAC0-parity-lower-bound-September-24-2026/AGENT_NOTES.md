# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Minbo Gao, Zhengfeng Ji, Chenghua Liu, *A simplified proof of PARITY ∉ QAC⁰*](https://eccc.weizmann.ac.il/report/2026/258/) (ECCC TR26-258, 18 October 2026). Presents itself as a self-contained simplification of this paper's localization proof: it replaces the low-count enumeration and three-factor propagation of Lemmas 5–6 here with a direct layer-removal argument (citing the companion paper's Proposition 4.1), and keeps the zero-count polynomial, the inverse-circuit argument and the parity reduction. [family-level]
- [Shiva Kintali, *PARITY ∉ QAC⁰ (via Polarization and Direct Induction)*](https://shivakintali.github.io/papers/Parity.pdf) (preprint, dated 17 October 2026). Gives a self-contained simplification of this paper's proof: polarization writes the reflection expansion as a linear combination of product projections with coefficient cost 18^k, which replaces the intermediate low-count propagation while keeping the localization framework and the inverse-circuit bootstrap; the companion paper is cited as a different proof. [family-level]

## Expert comments and discussion
- [Scott Aaronson, *The Mathocalypse*](https://scottaaronson.blog/?p=10169) (Shtetl-Optimized, 7 October 2026). Names "Parity is not in QAC0" among the release's highlights and calls it "one of the great questions of quantum complexity theory since 1999 that many of my colleagues had been closing in on"; the post does not discuss the proofs. [family-level]

## Formalization
- [OpenAI math release, *Lean scope notes for family 274*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/274.md) (lean/docs/274.md, October 2026). Describes the release's Lean formalization of the measured-output parity lower bound for every fixed positive worst-case advantage and polynomial total-qubit bound (plus a specialization to success below 2/3) and the product-projection localization estimate, with comparator statements in QACParity.lean and RegularParity.lean. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Ashley Montanaro, Changpeng Shao, Dominic Verdon, *Low-degree approximation of QAC⁰ circuits*](https://arxiv.org/abs/2411.00976) (arXiv:2411.00976, v1 1 November 2024, withdrawn in v2 on 7 November 2024). An earlier claimed proof that parity is not in QAC⁰, together with a quantum LMN-type theorem (compare Theorem 1 and the quantum LMN corollary here); it was withdrawn with the comment "Lemma 2.1 is incorrect, and we need some time to fix it".
- [Daniel Grier, Jackson Morris, Kewen Wu, *QAC⁰ Contains TC⁰ (with Many Copies of the Input)*](https://arxiv.org/abs/2601.03243) (arXiv:2601.03243, 6 January 2026). Shows TC⁰ ⊆ QAC⁰ ∘ NC⁰ when many copies of the input are available; relevant context for this paper's corollaries on majority and symmetric functions, which concern a single copy of the input.
- [Yangjing Dong, Fengning Ou and Penghui Yao, *On the Computational Power of Geometrically Local QAC circuits*](https://arxiv.org/abs/2604.07178) (arXiv:2604.07178v2, 2026-09-30). Studies geometrically local versions of the circuit model and relates a stronger polynomial-size parity width lower bound to the parity exclusion claimed by this family. [family-level]

## Digests and expositions
- [AI Proved What?, *Shallow circuits, no parity, proved at last?*](https://aiprovedwhat.com/episodes/274-parity-not-qac0/) (episode 274, October 2026). Provides a short video and transcript outlining the measured-output claim, product-projection localization and the companion pruning argument. [AI-generated per source] [family-level]

## News and blogs
- None found.
