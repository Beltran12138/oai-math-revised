# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Jaehoon Kim, *A proof of the Erdős–Gallai cycle decomposition conjecture*](https://arxiv.org/abs/2610.07840) (arXiv:2610.07840, v1 6 Oct 2026, v2 9 Oct 2026). Contemporaneous independent proof of the same linear bound, developed with disclosed ChatGPT and Claude assistance; a v2 note acknowledges the OpenAI proof and contrasts its quotient-and-lifting induction with Kim's approach through light graphs and polynomial minimum degree.
- [Ryan Coffey, proof claim for Erdős Problem #184 on the erdosproblems.com forum](https://www.erdosproblems.com/forum/thread/184/proof-claims) (forum post, 1 Oct 2026). Separate claimed proof of the $O(n)$ bound, listed as made with Claude Opus 5.5 and building on the Bucić–Montgomery round structure, posted after this preprint's date and before the release. [AI-generated per source]

## Comments and discussion
- [Thomas Bloom (erdosproblems.com), *Erdős problems in the OpenAI proofs*](https://www.erdosproblems.com/forum/thread/blog:10) (blog post, 8 Oct 2026). The curator of the Erdős problems site lists this preprint under Problem 184, summarizes its claim and notes that "This proof has been formalised"; a comment in the thread points to the Coffey and Kim claimed solutions.

## Formalization
- [OpenAI, *The Erdős–Gallai cycle-decomposition conjecture: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/181.md) (OpenAI Math Release, lean/docs/181.md, 2026-10-06). The release's scope note: it formalizes one absolute constant $C>0$ with at most $Cn$ cycles or single edges for every finite simple graph, including edgeless and small graphs, and leaves the optimal $C$ undetermined.
- [OpenAI, *lean/OAI/Combinatorics/CycleDecomposition/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/CycleDecomposition/Main.lean) (openai/math, commit adc7f12). Lean proof of `OAI.ErdosGallai.erdos_gallai`, which proves the `MainStatement` from the comparator file [ComparatorChallenges/CycleDecomposition.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CycleDecomposition.lean) via an intermediate bound with the paper's inductive factor φ(n).
- [Google DeepMind formal-conjectures, *FormalConjectures/ErdosProblems/184.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/184.lean#L35) (formal-conjectures, main branch). Independent formal statement `erdos_184`, marked research solved, whose docstring credits this preprint and links to the OpenAI Lean proof.
- [Ryan Coffey, *erdos-gallai-lean*](https://github.com/steelwheel01/erdos-gallai-lean) (GitHub, release tag 2026-10-01). Separate Claude-assisted Lean 4 formalization of a different proof (Coffey's) of the same theorem, targeting `Erdos184.erdos_184` directly, with a manuscript, verification records and a trust-model discussion; it does not mention the OpenAI paper and its README states that "Nobody has checked the mathematics".

## Related prior literature mentioned by others
- [Matija Bucić and Richard Montgomery, *Towards the Erdős–Gallai Cycle Decomposition Conjecture*](https://arxiv.org/abs/2211.07689) (arXiv:2211.07689; Advances in Mathematics 437, 109434, 2024). Kim's paper and the Erdős Problem a Day comparison identify this earlier $O(n\log^* n)$ result and its expander methods as background to the linear-bound proofs; it is also in the paper's bibliography.
- [Richard Montgomery, *Recent progress in graph theory using expansion*](https://arxiv.org/abs/2607.26049) (arXiv:2607.26049, 2026-07-28; ICM survey). Coffey's repository recommends this survey as context for the expansion methods underlying progress on the cycle-decomposition conjecture.

## Possibly relevant literature (found by the agent, not checked)
- [Richard Montgomery, *Cycles and expansion in graphs*](https://ems.press/journals/mag/articles/14299467) (EMS Magazine 138, 2025, doi:10.4171/MAG/287). Expository survey of expansion-based methods for cycle problems, including the Erdős–Gallai problem and the Bucić–Montgomery sublinear-expansion approach that the paper says it builds on.

## Digests and expositions
- [Open Mathematics Courses / Claude Opus 5.5, *The Erdős–Gallai cycle decomposition theorem*](https://kokunoyumeto.github.io/open-math-courses-public/courses/erdos-gallai-cycle-decompositions/) (online course, undated). Eight lessons explain this manuscript's routing, reservoirs, pair folding, cycle lifting and final induction, with exercises and solutions; the source states that independent review is incomplete. [AI-generated per source]

## News and blogs
- [Patrick White with Claude, Erdős Problem a Day, *Erdős #184: three claimed proofs, two Lean replays and a bridge*](https://www.erdosproblemaday.com/day/184-erdos-gallai-three-proofs-two-lean-replays-and-a-bridge) (2026-10-20). Comparison of the OpenAI, Coffey and Kim proofs that reports local Lean kernel replays and a bridge from OpenAI's theorem to a copied Formal Conjectures statement, and labels its manuscript assessments as AI reviews rather than human referee verdicts. [AI-generated per source]
- [OfficeChai Team, *OpenAI Has Also Included Proofs For 23 Erdos Problems In Its Latest Math Proof Drop*](https://officechai.com/ai/openai-has-also-included-proofs-for-23-erdos-problems-in-its-latest-math-proof-drop/) (OfficeChai, 9 Oct 2026). News article that lists Problem 184 among the release's Erdős results, describes the claimed $O(n)$ improvement over the iterated-logarithm bound, and notes that Thomas Bloom has not yet verified the proofs.
