# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Arpan Sadhukhan, Sagnik Sen, *Locating a Seymour vertex in oriented graphs having minimum outdegree at most 7*](https://arxiv.org/abs/2606.30588) (arXiv:2606.30588v2, 13 Oct 2026). Revised version of the minimum-outdegree-7 preprint that this paper cites as v1, now under a new title and without computational assistance. Its introduction notes the OpenAI preprint "presenting a proof of Seymour's Second Neighborhood Conjecture" and calls its own result "a work in parallel".

## Expert comments and discussion
- [Anonymous research release, *Seymour's second neighbourhood conjecture at order 2δ+3: structure of counterexamples, a certified 18-vertex lower bound, and a refutation of DeVos's conjecture as recorded in Sullivan's survey*](https://evidencepress.org/releases/seymour-second-neighbourhood-2delta3/) (evidencepress.org, 24 Sep 2026; note added 7 Oct 2026). An unrefereed counterexample-structure study whose "External development" note says the release "includes a claimed proof of the full conjecture". It reports that a local build and a statement check of the Lean formalization passed, while a hardened Comparator run was not performed.

## Formalization
- [OpenAI math release, *Lean scope notes for family 173*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/173.md) (lean/docs/173.md, 2026-10-06). The release's own Lean formalization of Theorem 1.1, the unweighted assertion for every nonempty finite oriented graph, with Comparator statement `exists_goodVertex` in `ComparatorChallenges/SeymourSecondNeighborhood.lean`. There the second neighborhood is the set of vertices at directed distance exactly two, and sinks are included. [AI-generated per source] [family-level]
- [GitHub user henrykmichalewski, *Add Seymour's second neighbourhood conjecture*](https://github.com/google-deepmind/formal-conjectures/pull/5188) (google-deepmind/formal-conjectures PR #5188, opened 27 Aug 2026, open). An independent Lean statement of the conjecture with variants (tournaments, minimum outdegree at most six, Chen–Shen–Yuster). In an approving review on 10 Oct 2026, reviewer mo271 links the OpenAI Lean file, suggests comparing the two formalizations, and asks whether the entry should be marked `research solved`.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Yandong Bai, Binlong Li, Boram Park, *Towards a strengthening of the second neighborhood conjecture*](https://arxiv.org/abs/2607.18047) (arXiv:2607.18047, Jul 2026). Studies a stronger form asking for a complete matching from $N^+(v)$ to $N^{++}(v)$, proved for minimum outdegree at most 5; Theorem 1.1 gives only the cardinality inequality.
- [Krystal Guo, Ross J. Kang, Gabriëlle Zwaneveld, *Seymour-tight orientations*](https://arxiv.org/abs/2603.29626) (arXiv:2603.29626, Mar 2026). Constructs orientations in which every vertex has equality $|N^+(v)|=|N^{++}(v)|$, the extremal cases for the inequality of Theorem 1.1.
- [Jiangdong Ai, Stefanie Gerke, Gregory Gutin, Shujing Wang, Anders Yeo, Yacong Zhou, *On Seymour's and Sullivan's Second Neighbourhood Conjectures*](https://arxiv.org/abs/2306.03493) (arXiv:2306.03493, v2 Jul 2026). Treats Sullivan's in-degree variant alongside Seymour's conjecture, relevant to the scope of the consequences in Sections 4–5, which concern Seymour's out-degree form.

## Digests and expositions
- [Latent Seminar, *First and second out-neighborhoods in oriented graphs*](https://lowrank.github.io/latent-seminar/OpenAI-Math/173-second-neighborhoods) (2026-10-07). Explains the manuscript's subset reduction, matching-and-rank pruning argument, and extremal objective; it states that it does not independently verify the complete proof or audit the Lean development. [family-level]
- [Open Mathematics Courses / Claude Opus 5.5, *Seymour's second neighborhood conjecture*](https://kokunoyumeto.github.io/open-math-courses-public/courses/seymours-second-neighborhood-conjecture/) (undated). Four lessons with exercises and solutions develop the minimal-counterexample reduction, tournament blow-ups, pruning theorem, and extremal argument; the course identifies itself as AI-written and self-checked, with independent review incomplete. [AI-generated per source] [family-level]
- [Gradient Damage, *Seymour's second-neighborhood conjecture*](https://gradientdamage.com/openai-math/seymours-second-neighborhood-conjecture/) (gradientdamage.com, video compilation dated 14 Oct 2026). A summary page with a video chapter that, per the page, "illustrates the statement; it is not the proof" and does not discuss the method.

## News and blogs
- None found.
