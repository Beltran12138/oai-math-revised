# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 301*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/301.md) (release, 2026-10-06). The release's Lean development covers only the ideal-transport step: a trace-cone isomorphism induces an order isomorphism of closed ideals (with each trace's finite and zero ideals), and the zero/infinity ideal traces are exactly the additive idempotents; spatial classification, existence, uniqueness and intertwining are not formalized. [family-level]
- [OpenAI math release, *TraceIdealTransportSupport.lean*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/TraceIdealTransportSupport.lean) (release, 2026-10-06). The comparator statement for the ideal-transport result described in the scope notes.

## Related prior literature mentioned by others
- [Luis Santiago, *Reduction of the dimension of nuclear C\*-algebras*](https://arxiv.org/abs/1211.7159) (arXiv:1211.7159, 30 November 2012). Linked as background by the AI Proved What? episode; it states Robert's question as Conjecture 1.1 (T(A) ≅ T(B) iff A⊗W⊗K ≅ B⊗W⊗K), noting it was known for AF and O_2-absorbing algebras, and proves stable rank one after tensoring with the Razak–Jacelon algebra for a class containing limits of separable type I algebras.
- [Christopher Schafhauser, Aaron Tikuisis and Stuart White, *Nuclear C\*-algebras: 99 problems*](https://arxiv.org/abs/2506.10902) (arXiv:2506.10902, 2025; revised 8 May 2026). The AI Proved What? episode identifies Problem LXVIII in this survey as the trace-cone classification question addressed by the manuscript.

## Possibly relevant literature (found by the agent, not checked)
- [George A. Elliott and Jeffrey Im, *Colored isomorphism of classifiable C\*-algebras*](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/colored-isomorphism-of-classifiable-calgebras/B5EAC065FFC00F002214D7343FA55493) (Canadian Journal of Mathematics 76, 216–245, 2024; published online 12 December 2022). Remark 4.2 recovers ideal lattices from the additive idempotents of the lower-semicontinuous trace cone, a comparison for the manuscript's ideal-recovery step.
- [Laurent Cantier, *Tracially reflexive C\*-algebras*](https://arxiv.org/abs/2605.22683) (arXiv:2605.22683, May 2026). States Robert's conjecture for the scaled cone up to W-tensorisation, says it should otherwise be stated up to stable isomorphism, and notes that the idempotents of T(A) encode the ideal lattice; this bears on the paper's stabilization by K and its ideal-weight encoding.
- [Leonel Robert, *Classification of inductive limits of 1-dimensional NCCW complexes*](https://arxiv.org/abs/1007.1964) (arXiv:1007.1964, 2010–2012). Santiago's paper reduces the conjecture for limits of homogeneous algebras to this classification, giving an earlier non-simple case against which Theorem 1.1 can be compared.
- [Mark Moodie and Leonel Robert, *Cones of traces arising from AF C\*-algebras*](https://arxiv.org/abs/2009.09033) (arXiv:2009.09033, 2020). Characterizes the non-cancellative cones arising as extended trace cones of AF algebras via a duality with Cuntz semigroups with real multiplication; relevant to the paper's use of the full extended-trace cone, including ideal weights.

## Digests and expositions
- [AI Proved What?, *The cone decides? Robert’s trace-cone question*](https://aiprovedwhat.com/episodes/301-trace-cones/) (episode 301, October 2026). This AI-assisted video and transcript illustrate extended traces and ideal recovery, outline the claimed existence-and-uniqueness argument, and distinguish the supporting Lean development from the classification theorem. [AI-generated per source] [family-level]
- [Gradient Damage, *Kaplansky's Quasitrace Conjecture, Naimark's Problem and 7 More in Operator Algebras*](https://gradientdamage.com/videos/kaplanskys-quasitrace-conjecture-naimarks-problem-and-7-more/) (video compilation, 15 October 2026). The chapter beginning at 2:46 introduces this paper's trace-cone classification claim, with the source describing the animations as illustrations rather than proofs. [family-level]

## News and blogs
- None found.
