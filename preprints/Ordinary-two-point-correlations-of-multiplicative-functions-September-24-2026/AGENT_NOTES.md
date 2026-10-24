# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Biao Wang and Shaoyun Yi, *Dynamical generalizations of the two-point Chowla conjecture*](https://arxiv.org/abs/2610.16394) (arXiv:2610.16394, 12 October 2026). Proves the two-point case of a Charamaras–Richter generalization concerning prime Omega functions along fixed nonproportional affine forms; it cites this manuscript as resolving the two-point case, and Section 3 adapts its progression-correlation argument, using several of its lemmas and Proposition 8.4.
- [Jizhou Guo, *Rough numbers at a fixed distance with prescribed Liouville signs*](https://github.com/aster2024/openai-math-followups/blob/main/rough-pairs-fixed-distance/paper.pdf) (GitHub preprint, 10 October 2026). The author's repository describes an adaptation of family 007's graph operator that retains sieve density to obtain equidistribution of the four Liouville sign patterns on rough-number pairs at a fixed even distance. [AI-generated per source]

## Comments and discussion
- [Jared Duker Lichtman, comments on two-point Chowla as reported by Post-Cutoff](https://postcutoff.com/p/2026-10-06-jdlichtman-zero-free-strip-hodge/) (account of an X thread, 6–7 October 2026). This AI-written secondary account attributes to Lichtman an assessment of the quantitative ordinary two-point result as especially significant while describing its methods as lying within existing approaches. [AI-generated per source]

## Formalization
- [OpenAI, *Ordinary two-point correlations and the corrected Elliott conjecture: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/007.md) (lean/docs/007.md, 6 October 2026). Describes the scope of the release's Lean formalization: the absolute-exponent logarithmic saving for affine Liouville correlations and qualitative shifted and affine Elliott cancellation under uniform nonpretentiousness, with links to the comparator statements. [AI-generated per source] [family-level]
- [OpenAI, *TwoPointCorrelations/FinalMain.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/TwoPointCorrelations/FinalMain.lean) (openai/math, commit adc7f12). Release Lean file that states the main theorems `liouville_log_saving`, `binary_corrected_elliott` and `affine_corrected_elliott`.
- [OpenAI, *OrdinaryCorrelations/Elliott/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/OrdinaryCorrelations/Elliott/Main.lean) (openai/math, commit adc7f12). Release Lean development for the ordinary-average Elliott part (Part II of the paper).

## Related prior literature mentioned by others
- [Dimitrios Charamaras and Florian K. Richter, *Asymptotic independence of Ω(n) and Ω(n+1) along logarithmic averages*](https://arxiv.org/abs/2412.17583v3) (arXiv:2412.17583v3, 17 August 2026; first version 2024). Wang and Yi cite this logarithmically averaged generalization of two-point Chowla and its ordinary-average conjecture as the starting point for their extension of the OpenAI result.
- [Jizhou Guo, *Logarithmic Chowla Correlations Across All Shift Scales*](https://arxiv.org/abs/2608.23500) (arXiv:2608.23500v4, 1 September 2026; first version 24 August 2026). The AI Proved What? exposition cites this pre-release work as context; its abstract concerns power-logarithmic bounds for logarithmically weighted correlations outside a sparse exceptional set of shifts, whereas the OpenAI manuscript concerns ordinary averages at each fixed shift.

## Possibly relevant literature (found by the agent, not checked)
- [Scott D. Hughes, *Effective logarithmic two-point Chowla bounds in every window*](https://arxiv.org/abs/2609.28526) (arXiv:2609.28526, 22 September 2026). Gives effective logarithmically averaged two-point Chowla bounds that are uniform in the affine forms, whereas Theorem 1.1 of this paper concerns ordinary averages and states no uniformity in the coefficients.
- [Thomas Renard, *Truncated pretentious distances of multiplicative arithmetic functions*](https://arxiv.org/abs/2609.37332) (arXiv:2609.37332, 29 September 2026). Identifies a class of non-pretentious functions for which Elliott's conjecture holds in its original formulation, building on Klurman–Mangerel–Teräväinen; this is relevant to the nonpretentiousness hypothesis (1.2) used in Theorem 1.2.

## Digests and expositions
- [AI Proved What?, *Even or odd: the two-point Chowla conjecture*](https://aiprovedwhat.com/episodes/007-ordinary-two-point-correlations-corrected/) (episode 007, October 2026). The video and published script explain the ordinary-versus-logarithmic distinction, outline the divisor-graph arguments, and distinguish the published Lean material from independently reproduced checks. [AI-generated per source] [family-level]

## News and blogs
- [Azmat, *Two-Point Chowla Conjecture: OpenAI’s Proof Breaks a 61-Year Averaging Deadlock*](https://binaryverseai.com/two-point-chowla-conjecture-openai-proof/) (Binary Verse AI, 12 October 2026). This paper-specific article discusses the two theorem statements, residue comparisons and graph estimates, and explicitly says it does not report a fresh Lean compilation or completed independent review.
