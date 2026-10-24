# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 205: Saxl's conjecture and universal tensor squares*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/205.md) (lean/docs/205.md, 2026-10-06). The release's Lean development proves $g(\rho_m,\rho_m,\mu)>0$ for all $m\ge1$; the stronger claim that every constituent lies in the cyclic module of one prescribed tensor is stated as not formalized. [family-level]
- [OpenAI, *Saxl/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/RepresentationTheory/Saxl/Main.lean) (openai/math, pinned commit adc7f12). The Lean proof file for Theorem 1.1, checked against the comparator statement [ComparatorChallenges/Saxl.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Saxl.lean).
- [Shuze Chen, *The cyclic staircase module inside the tensor square of the staircase Specht module*](https://beta.prove2.me/theorems/7f2eaf67-9448-4efe-bf18-30eb8b5e1563) (Prove2Me, 2026-10-18). A Lean definitions bundle extracted from OpenAI's `Saxl/CyclicTensor.lean` that constructs the cyclic module's map into the staircase tensor square and states the stronger cyclic conjecture used by both papers; the page does not supply a proof of that conjecture. [family-level]
- [Shuze Chen, *Content orbits of words, orbit projections and the letter-sum map on word spaces*](https://beta.prove2.me/theorems/9afe5ff9-102d-41a8-b930-2024f0ffc344) (Prove2Me, 2026-10-18). A definitions bundle extracted from OpenAI's `Saxl/RepeatedProjection.lean` with Lean constructions of the content-orbit projection and letter-sum intertwiner used to detect permutation-module generators in the staircase square.
- [Keith Adler (with Claude), *saxl-lean*](https://github.com/keithadler/saxl-lean) (GitHub, status dated 2026-10-07). An independent Lean 4/Mathlib project on this paper that re-derives roughly the first half of the argument, proves the staircases (1) through (4,3,2,1) independently, and vendors OpenAI's own complete Lean proof; marked as concluded. [AI-generated per source]
- [Keith Adler, *mathlib4 PR #44612: conjugacy classes of Perm α are partitions of Nat.card α*](https://github.com/leanprover-community/mathlib4/pull/44612) (mathlib4, opened 2026-10-07, closed unmerged 2026-10-16). A supporting Mathlib contribution from the saxl-lean project, motivated as a counting input for "every irreducible representation of S_n is a Specht module". [AI-generated per source]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Soong Kyum Lee, *Staircase Minimality and a Proof of Saxl's Conjecture*](https://arxiv.org/abs/2512.15035) (arXiv:2512.15035, Dec 2025). An earlier claimed unconditional proof of the same statement (Theorem 1.1); the arXiv comment says the paper is withdrawn because the claimed proof is not justified in its current form.
- [Yutong Chen, Felix Gu, Will Osborne, *Spin Representations of Finite Coxeter Groups and Generalisations of Saxl's Conjecture*](https://arxiv.org/abs/2409.17540) (arXiv:2409.17540, Sep 2024). Proposes generalisations of Saxl's conjecture to Weyl and finite Coxeter groups, giving context for the paper's "History and significance" discussion of the broader covering problem.

## Digests and expositions
- None found.

## News and blogs
- None found.
