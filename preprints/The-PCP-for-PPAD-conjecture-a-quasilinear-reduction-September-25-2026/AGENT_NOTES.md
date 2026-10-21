# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Anagnostides, Daskalakis, Farina, Golowich, Sandholm, Zhang, *Fixed Sets and the Hardness of Computing Correlated Equilibria*](https://arxiv.org/html/2610.28141) (arXiv:2610.28141, 20 October 2026). Main Theorem 4(ii) (polynomial-precision hardness) is stated under the PCP-for-PPAD conjecture (Assumption 2.3). Footnote 2 notes "OpenAI recently claimed a proof of the required PCP-for-PPAD theorem", linking this manuscript, but the authors do not treat it as established "until it has been verified by human experts".

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *Generalized-circuit smoothing, perturbation stability and rational meshes*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/OAI/Computability/GeneralizedCircuits/Mesh.lean) (Lean source, accessed 2026-10-21). This partial development supplies supporting lemmas and a goal proposition `QuasilinearPCPStatement`, while its scope comment explicitly leaves simultaneous totality, the uniform reduction, soundness, algorithm realization and complexity bounds unproved.

## Related prior literature mentioned by others
- [Yakov Babichenko, Christos Papadimitriou and Aviad Rubinstein, *Can Almost Everybody be Almost Happy? PCP for PPAD and the Inapproximability of Nash*](https://arxiv.org/abs/1504.02411) (arXiv:1504.02411, 2015; revised 2025-09-05). The [AI Proved What? exposition](https://aiprovedwhat.com/episodes/136-pcp-for-ppad/) identifies this work as the source of the conjecture that the manuscript claims to resolve.
- [Aviad Rubinstein, *Settling the complexity of computing approximate two-player Nash equilibria*](https://arxiv.org/abs/1606.04550) (arXiv:1606.04550, 2016; revised 2016-08-29). The [AI Proved What? exposition](https://aiprovedwhat.com/episodes/136-pcp-for-ppad/) identifies its encoded-path geometry and holographic proof system as predecessors of the manuscript's construction, distinguishing its conditional Nash lower bound from the PCP-for-PPAD conjecture.

## Possibly relevant literature (found by the agent, not checked)
- [Irit Dinur, *The PCP theorem by gap amplification*](https://eccc.weizmann.ac.il/report/2005/046/) (ECCC TR05-046, 2005; J. ACM 2007). Gives constant-query PCPs and locally testable codes of quasilinear length via expander-based gap amplification, the Boolean analogue of the paper's quasilinear-size bound $M\le AN\lceil\log_2(N+2)\rceil^b$.

## Digests and expositions
- [AI Proved What?, *PCP for PPAD? A quasilinear, gate-robust reduction from End-of-Line*](https://aiprovedwhat.com/episodes/136-pcp-for-ppad/) (episode 136, October 2026). This illustrated exposition and transcript explain the claimed reduction, its outer and inner constructions, robustness to failed gates, and the limited scope of the accompanying Lean development. [AI-generated per source]
- [Gradient Damage, *Every OpenAI Math Result, Part 2 of 4: PCP for PPAD, Birkhoff Conjecture and 82 More*](https://gradientdamage.com/videos/every-openai-math-result-part-2-of-4-pcp-for-ppad-birkhoff-conjecture/) (video, 14 October 2026). An animated overview of many release results that presents result 136 at 0:41, restating the release summary and calling it a preprint that has not been peer reviewed.

## News and blogs
- None found.
