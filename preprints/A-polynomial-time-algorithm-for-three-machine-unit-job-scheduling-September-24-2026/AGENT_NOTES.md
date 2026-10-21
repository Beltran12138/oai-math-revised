# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- [NotOscarWilde (Hacker News), comment in the thread *Sharing AI progress in mathematics*](https://news.ycombinator.com/item?id=49985622) (HN item 49985622, 2026-10-06). The commenter, a self-described "TCS/scheduling person", says the paper addresses the three-machine problem open since Garey and Johnson (1979), remarks on the exponent 150020, and says they cannot check its correctness.

## Formalization
- [OpenAI math release, *Lean scope notes for family 124* (lean/docs/124.md)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/124.md) (release Lean documentation, 2026-10-06). Describes the scope of the Lean formalization: one fixed deterministic machine that constructs minimum-makespan schedules and decides deadline feasibility for nonempty unit-job instances with arbitrary acyclic precedence constraints on three identical machines, in time polynomial in the binary input length. [family-level]
- [OpenAI math release, *ThreeMachine.lean* comparator statement](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/ThreeMachine.lean) (release Lean comparator challenge, 2026-10-06). States the target theorem: a fixed Turing machine and a constant C give a correct schedule or a "none" answer within C·(input length + 2)^150020 steps.

## Related prior literature mentioned by others
- [Christina Büsing, Maurice Draeger and Corinna Mathwieser, *Parameterized Complexity of Scheduling Unit-Time Jobs with Generalized Precedence Constraints*](https://doi.org/10.4230/LIPIcs.IPEC.2025.7) (IPEC 2025, 7:1–7:16, 2025-12-15). Cited in [AIM’s entry on this scheduling problem](https://github.com/MColbrook/AIM/blob/main/problems/301-three-processor-unit-scheduling.md); it studies parameterized tractability and hardness for Boolean precedence constraints, context for the paper's restriction to ordinary DAG precedence.

## Possibly relevant literature (found by the agent, not checked)
- [Mnich and van Bevern, *Parameterized complexity of machine scheduling: 15 open problems*](https://arxiv.org/abs/1709.01670) (arXiv:1709.01670; Computers & Operations Research 100 (2018) 254–261). Section 4.2 records P3|prec,p_j=1|Cmax as open and asks, as Open Problem 6, whether it is FPT parameterized by the width of the partial order; it is not in the paper's bibliography.
- [Nederlof, Swennenhuis and Węgrzycki, *Makespan Scheduling of Unit Jobs with Precedence Constraints in O(1.995^n) time*](https://arxiv.org/abs/2208.02664) (arXiv:2208.02664, 2022). An earlier exact-algorithm paper by these authors, noting that even for m=3 the best previous algorithms ran in O*(2^n) time; relevant to the paper's survey of exact algorithms, which cites only their SODA 2025 subexponential paper.
- [Bodlaender, Groenland, Nederlof and Swennenhuis, *Parameterized Problems Complete for Nondeterministic FPT time and Logarithmic Space*](https://arxiv.org/abs/2105.14882) (arXiv:2105.14882, 2021/2023). Lists scheduling with precedence constraints, parameterized by the number of machines together with the partial-order width, among its XNLP-complete problems; context for the paper's claim of a polynomial algorithm for fixed m=3.
- [Lenstra and Rinnooy Kan, *Complexity of Scheduling under Precedence Constraints*](https://ideas.repec.org/a/inm/oropre/v26y1978i1p22-35.html) (Operations Research 26(1) (1978) 22–35, doi:10.1287/opre.26.1.22). A classical NP-completeness paper on precedence-constrained scheduling, relevant to the paper's statement of hardness when m is part of the input, which it attributes only to Ullman (1975).

## Digests and expositions
- [AI Proved What?, *Three machines, polynomial? Scheduling unit jobs with precedence*](https://aiprovedwhat.com/episodes/124-three-machine-scheduling/) (Episode 124, October 2026; status updated 2026-10-19). Video and transcript explaining the claimed bounded-description decomposition and dynamic program, reporting small-instance experiments, and distinguishing inspection of the published Lean statements from running the checker. [AI-generated per source] [family-level]

## News and blogs
- [explainx.ai blog, *OpenAI Math Results: 8 Claims, Lean Status, Expert Views*](https://explainx.ai/blog/openai-math-results-that-matter-expert-reactions-2026) (blog post, 2026). Summarizes this paper's claim, its O((L+2)^150020) bound and its Lean status (doc and comparator file present, absent from lean/formalization.yaml), and points to the Hacker News comment above.
