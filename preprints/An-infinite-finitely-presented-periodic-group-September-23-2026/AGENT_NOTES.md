# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Kenta Kitamura, *Infinite finitely presented residually finite p-groups for every prime*](https://github.com/KitaKen1/all-prime-residually-finite-p-groups) (GitHub repository, October 2026). Claims an infinite finitely presented residually finite p-group for every prime p, building on this paper's construction; its Lean development reuses 63 unchanged modules from the openai/math repository, and the README states that ChatGPT, OpenAI Codex and Claude Code assisted. [AI-generated per source] [family-level]

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *Lean scope note for result family 247*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/247.md) (OpenAI Math Release, 2026-10-06). The scope note reports a Lean formalization of an infinite finitely presented periodic Steinberg group over a characteristic-two algebra, with no common exponent asserted, and explicitly excludes the separate nil- and radical-algebra conclusions.
- [OpenAI, *ComparatorChallenges/PeriodicGroup.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PeriodicGroup.lean) (openai/math). Comparator statement: there is a `ZMod 2`-algebra R such that `Steinberg 12 R` is infinite, finitely presented and periodic, and hence there is an infinite finitely presented periodic group; the proof is left as `sorry` in this challenge file. Comparator challenge files leave the proof as `sorry` by design; `PeriodicGroup.json` names the module `OAI.GroupTheory.PeriodicGroups.Main` as the release's proof of this statement.
- [OpenAI, *OAI/GroupTheory/PeriodicGroups/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/GroupTheory/PeriodicGroups/Main.lean) (openai/math). Solution module that proves `thm_main` (Theorem 1.1) from imported kernel-torsion and periodicity results.
- [Kenta Kitamura, *Formalize the finitely presented Burnside problem and its variants*](https://github.com/google-deepmind/formal-conjectures/pull/7412) (google-deepmind/formal-conjectures PR #7412, opened 2026-10-16, open). Adds Lean statements of Theorem 1.1 (citing this paper as [OAI26]) and two residually-finite variants, with `formal_proof` links to an external solution; the reviewer approved but wrote that they did not rerun the verification. [family-level]
- [Kenta Kitamura, *Add a conjecture: infinite finitely presented residually finite p-groups for every prime*](https://github.com/google-deepmind/formal-conjectures/issues/7284) (google-deepmind/formal-conjectures issue #7284, 2026-10-13). Issue proposing the all-primes strengthening for formal-conjectures; it links the proof note and repository listed under follow-up works. [family-level]

## Related prior literature mentioned by others
- [Efim Zelmanov, *Some open problems in the theory of infinite dimensional algebras*](https://paperzz.com/doc/7025423/some-open-problems-in-the-theory-of-infinite) (Journal of the Korean Mathematical Society 44(5), 1185–1195, September 2007; public text reproduction). Invoked by the AI Proved What? exposition; its Problems 1–3 concern finitely presented torsion groups and algebraic or nil algebras, and a subsequent paragraph considers whether residual finiteness might preclude such infinite torsion groups. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [*Unsolved Problems in Group Theory. The Kourovka Notebook*, Problem 8.52 (A. Yu. Olshanskii)](https://arxiv.org/html/1401.0300v47) (arXiv:1401.0300v47, 2026-09-30). Lists "Do there exist infinite finitely presented periodic groups?" as unsolved; Theorem 1.1 addresses this question (Problem 6.3 of R. Bieri, on periodic groups of type FP∞, is also related).
- [T. Adamczewski, B. Böhmler, R. Marczinzik, *A counterexample to Köthe's conjecture and a question of Rowen*](https://arxiv.org/abs/2609.07996) (arXiv:2609.07996, 2026-09-07). A counterexample to Köthe's conjecture yields nil rings with non-nil matrix rings; this bears on why the paper proves nilpotence of every matrix in M_d(I) separately from nilpotence of elements of I.

## Digests and expositions
- [AI Proved What?, *Finite rules, finite orders, still infinite?*](https://aiprovedwhat.com/episodes/247-finitely-presented-periodic-group/) (Episode 247, October 2026). This AI-assisted video and transcript outline both papers' ring construction and Steinberg-kernel arguments, distinguish the full periodic group from its 2-group subgroup, and discuss the limited formalization scope. [AI-generated per source] [family-level]

## News and blogs
- None found.
