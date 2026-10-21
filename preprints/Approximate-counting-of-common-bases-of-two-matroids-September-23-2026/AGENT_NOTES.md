# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [gavenren (GitHub), *Attempt: TOP-30007447*](https://github.com/We-Solve/research/issues/129) (We-Solve/research issue #129, 2026-10-18). A partial result giving an exact reduction and an FPRAS for two partition matroids whose nonloop blocks all have capacity one; it cites this paper's general claim as context and says the claim was not audited. [AI-generated per source]

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 114*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/114.md) (lean/docs/114.md). Describes the formalized statement: an FPRAS for common bases of two equal-rank independence-oracle matroids, with polynomial bounds on every random tape and zero output for a zero count, with the comparator statement in CommonBasesFPRAS.lean. [family-level]
- [OpenAI, *CommonBases.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/MatroidCounting/CommonBases.lean) (openai/math, lean/OAI/Combinatorics/MatroidCounting). The release's Lean development for this theorem, about 26,000 lines.

## Related prior literature mentioned by others
- [Nima Anari, Shayan Oveis Gharan and Cynthia Vinzant, *Log-Concave Polynomials I: Entropy and a Deterministic Approximation Algorithm for Counting Bases of Matroids*](https://arxiv.org/abs/1807.00929) (arXiv:1807.00929, 2018; Duke Mathematical Journal, 2021). The BinaryVerse AI post cites its deterministic $2^{O(r)}$ approximation and exponential-rank dependence as background to this paper's unrestricted-rank FPRAS claim.

## Possibly relevant literature (found by the agent, not checked)
- [Xiaoyu Chen and Kuikui Liu, *An FPRAS for Counting Common Bases of Two Matroids*](https://arxiv.org/abs/2610.06724) (arXiv:2610.06724, 2026-10-05). An independent paper claiming the same main result via a "soft intersection" with an overlap penalty, a Poincaré inequality and a dual maximum-entropy program, with stated running time $\widetilde O(n^{13}/\varepsilon^2)$. It does not cite the OpenAI release and says GPT models "were heavily used to develop the ideas in this paper."

## Digests and expositions
- [Latent Seminar, *Counting common matroid and integer polymatroid bases*](https://lowrank.github.io/latent-seminar/OpenAI-Math/114-common-bases-counting) (October 7, 2026). An exposition of both family manuscripts' defect states, trace-chain estimates, multiplicity corrections and binary-capacity reduction, limited by its own account to statements and selected proof mechanisms. [family-level]

## News and blogs
- [Azmat, *Counting Common Bases of Two Matroids: How OpenAI’s Proof Breaks the Approximation Barrier*](https://binaryverseai.com/counting-common-bases-of-two-matroids/) (BinaryVerse AI, October 14, 2026). Explains this paper's paired-ground-set reduction, defect multipliers, transport estimates and trace-chain annealing, and distinguishes its oracle complexity guarantee from demonstrated practical speedups.
