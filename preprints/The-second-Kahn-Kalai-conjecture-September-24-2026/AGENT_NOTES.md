# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [acprk, *R13: Second Kahn–Kalai conjecture: constant 2048e^50 ≈ 10^25 → 10^5*](https://github.com/acprk/openai-math-remarks/blob/main/remarks/R13-kahn-kalai-constant) (GitHub repository acprk/openai-math-remarks, undated draft). A remark that re-tunes the parameters of this paper's proof and claims computer-certified constants of about 10^5 and 2·10^5 in place of 2048e^50 and 6144e^50, assuming the manuscript's lemmas. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 176: The second Kahn–Kalai conjecture with an edge-count bound*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/176.md) (lean/docs/176.md, 2026). The scope note reports formalization of both bounds of Theorem 1.1 using the actual containment and expectation thresholds, with a universal factor times $1+\log_2|E(H)|$ and the consequent $\log_2 n$ bound. [AI-generated per source]
- [OpenAI math release, *SecondKahnKalai.lean* (comparator statement)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/SecondKahnKalai.lean) (lean/ComparatorChallenges). The Lean statement `OAI.LeanBlast.SecondKahnKalai.secondKahnKalaiBounds` of both bounds of Theorem 1.1 with the constants 2048e^50 and 6144e^50; the challenge file leaves the proof as `sorry`, to be supplied separately. Comparator challenge files leave the proof as `sorry` by design; `SecondKahnKalai.json` names the module `OAI.Combinatorics.GraphThreshold.Main` as the release's proof of this statement.

## Related prior literature mentioned by others
- [Jinyoung Park, *Thresholds*](https://gilkalai.wordpress.com/wp-content/uploads/2026/07/25m1806466.pdf) (Proceedings of the ICM 2026, vol. 6, pp. 199–211, 2026). Park surveys the two Kahn–Kalai conjectures and fractional expectation thresholds; Kalai's October 7 post on the release points readers to his account of this lecture.

## Possibly relevant literature (found by the agent, not checked)
- [Q. Dubroff, *Thresholds vs. expectation thresholds for non-spanning graphs*](https://arxiv.org/abs/2602.00278) (arXiv:2602.00278, January 2026). Constructs graphs H on m vertices whose threshold exceeds q_f(H) by a factor of order √(log m), bearing on how far the factor (1+log₂ h) in Theorem 1.1 can be reduced for small targets.
- [J. Park, *A dimension-free comparison between expectation thresholds and fractional expectation thresholds*](https://arxiv.org/abs/2609.14681) (arXiv:2609.14681, September 2026). A comparison of q and q_f with a log log loss, related to the integral-versus-fractional comparison the introduction cites as context.
- [R. Ascoli, X. He, J. Park, M. Talagrand, *A reformulation of the discrete Convexity Conjecture via k-thresholds*](https://arxiv.org/abs/2608.11183) (arXiv:2608.11183, August 2026). Bounds thresholds of graph-containment properties through decompositions into graphs with known thresholds, a parallel graph-specific comparison with expectation thresholds.

## Digests and expositions
- [Claude Opus 5.5 / Open Mathematics Courses, *The second Kahn–Kalai conjecture*](https://kokunoyumeto.github.io/open-math-courses-public/courses/thresholds-and-expectation-thresholds/the-second-kahn-kalai-conjecture.html) (October 2026). A lesson reconstructing the graph hierarchy and conditional spread argument leading to the paper's explicit edge-count bound, with preceding lessons on resampling and tree covering. [AI-generated per source]

## News and blogs
- None found.
