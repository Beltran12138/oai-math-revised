# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note 098: Compact counterexamples to bi-Lipschitz dimension reduction*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/098.md) (lean/docs/098.md, 2026). The release's scope note says it formalizes Theorem 1 (a doubling subset of real ℓ₂ with constant at most 76800 and no embedding into any ℝ^k) and the compact Banach-space companion; it links the comparator statements `DoublingHilbert.lean` and `CompactBanach.lean`. [family-level]
- [OpenAI math release, *lean/OAI/Geometry/DoublingHilbert/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/DoublingHilbert/Main.lean) (openai/math commit adc7f12, 2026). The Lean proof file for the theorem `OAI.DoublingHilbert.main`, which states that some `S : Set RealL2` has `DoublingAtMost S 76800` and admits no bi-Lipschitz embedding into `EuclideanSpace ℝ (Fin k)` for any `k > 0`.
- [anxkhn, *Add the doubling Hilbert dimension-reduction counterexample*](https://github.com/google-deepmind/formal-conjectures/issues/6993) (google-deepmind/formal-conjectures issue #6993, 2026-10-08). The issue proposes adding Theorem 1 as a formal statement. It covers only the fixed Hilbert subset, leaves out the compact Banach-space companion, and makes no `formal_proof` claim.
- [anxkhn, *feat(Paper): add the doubling Hilbert counterexample*](https://github.com/google-deepmind/formal-conjectures/pull/6998) (google-deepmind/formal-conjectures PR #6998, opened 2026-10-08, open at time of collection). The pull request adds the statement of Theorem 1, pinned to a commit of the manuscript; reviewer bocowgill approved it on 2026-10-10 after checking it against Theorem 1 and Proposition 2, including the open-ball form of the 76800 bound.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [G. C. David, P. Pankka, J. T. Tyson, *The Heinonen-Semmes problems after thirty years*](https://arxiv.org/abs/2510.19179) (arXiv:2510.19179, 2025-10-22). Section 3.2 of this survey calls the Lang–Plaut problem "perhaps the most fundamental open problem in the area" and says it "remains open in full generality," the status the paper's main theorem addresses.
- [A. Naor, K. Ren, *A threshold phenomenon for embeddings of Euclidean snowflakes and impossibility of dimension reduction*](https://arxiv.org/abs/2609.01079) (arXiv:2609.01079, 2026-09-01). The introduction states the Lang–Plaut problem for K-doubling subsets of ℓ₂, discusses a "sharp Lang–Plaut problem" for snowflakes and treats ℓ_p analogues, relating to the paper's discussion of snowflake embeddings and of the p>2 obstructions.

## Digests and expositions
- [Latent Seminar, *A doubling Hilbert subset with no finite-dimensional embedding*](https://lowrank.github.io/latent-seminar/OpenAI-Math/098-doubling-hilbert-obstruction) (6 October 2026). This exposition discusses sparse orthogonal displacements, derivative extrema, the crossing argument and compact Banach-space transfer, explicitly distinguishing its reading of selected proof mechanisms from independent verification. [family-level]
- [Open Mathematics Courses / Claude Opus 5.5, *The Lang–Plaut problem*](https://kokunoyumeto.github.io/open-math-courses-public/courses/the-lang-plaut-problem/) (undated; accessed 21 October 2026). Four lessons with exercises develop the manuscript's coloured-strip construction, lexicographic derivative maximum, energy estimates and packing contradiction; the source states that independent review is incomplete. [AI-generated per source]
- [Gradient Damage, *Petty's Projection Conjecture, Log Brunn–Minkowski Conjecture and 8 More*](https://gradientdamage.com/videos/pettys-projection-conjecture-log-brunn-minkowski-conjecture-and-8-more/) (15 October 2026). The chapter beginning at 2:47 introduces the Lang–Plaut problem and the release's claimed counterexample, with a direct link to this manuscript. [family-level]

## News and blogs
- None found.
