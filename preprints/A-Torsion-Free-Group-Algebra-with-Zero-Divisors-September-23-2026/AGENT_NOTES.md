# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [acprk/openai-math-remarks, *R14: Kaplansky zero-divisor counterexample over PG(2,16)*](https://github.com/acprk/openai-math-remarks/blob/main/remarks/R14-kaplansky-zero-divisor-q16) (GitHub remark, undated; literature search stated up to 2026-10-09). Argues that the paper's construction and proof also work with projective-plane parameter q = 16 instead of q = 128, and reports a spectral-radius computation indicating the key lemma fails for q = 8; the remark states it assumes the q = 128 manuscript and was reviewed by AI sessions, not human peer review. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *A counterexample to Kaplansky’s zero-divisor conjecture — Lean scope note* (lean/docs/196.md)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/196.md) (OpenAI math release, 6 October 2026). Describes the scope of the release's Lean formalization: a finitely presented torsion-free group with a finite two-dimensional K(G,1) and nonzero α, β ∈ F₂[G] with αβ = 0. [AI-generated per source]
- [OpenAI, *lean/OAI/Algebra/GroupRing/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/GroupRing/Main.lean) (openai/math, commit adc7f12). The release's top-level Lean file, which proves `theorem main : MainTheorem` for a concrete group built from imported sampling, torsion-freeness, model and factor modules.
- [OpenAI, *lean/ComparatorChallenges/TorsionFreeZeroDivisors.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/TorsionFreeZeroDivisors.lean) (openai/math, commit adc7f12). The comparator statement of the main theorem: ordinary torsion-freeness, Mathlib's `Group.IsFinitelyPresented`, a finite 2-dimensional CW model with contractible cover, and nonzero zero divisors in `MonoidAlgebra (ZMod 2) G`.
- [Google DeepMind formal-conjectures, *FormalConjectures/Wikipedia/Kaplansky.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/Kaplansky.lean#L27) (formal-conjectures). Restates the zero-divisor conjecture as its negation, tags it as solved and cites this paper; proof bodies in the file are `sorry` placeholders linking to the OpenAI Lean proof.
- [mo271, *feat: mark problems solved in the OpenAI math release and link formal proofs*](https://github.com/google-deepmind/formal-conjectures/pull/6898) (formal-conjectures PR #6898, merged 2026-10-11). Lists the Kaplansky zero-divisor conjecture among the refuted statements, restates it as a negation and adds `counter_zero_divisor_conjecture` with a proof link. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Pascal Schweitzer, *On Zero Divisors with Small Support in Group Rings of Torsion-Free Groups*](https://arxiv.org/abs/1202.6645) (arXiv:1202.6645, 2012). Studies the zero-divisor conjecture through a reduction to the field with two elements, relevant to what a counterexample over F₂ such as the paper's main theorem implies for other fields.
- [Alireza Abdollahi and Zahra Taheri, *Kaplansky's zero divisor and unit conjectures on elements with supports of size 3*](https://arxiv.org/abs/1612.00934) (arXiv:1612.00934, 2016). Proves lower bounds on the support size of β when αβ = 0 and |supp(α)| = 3 (at least 20 over F₂), constraining supports of factors like the paper's α and β.
- [Moe Tabei, *Least sizes of non-unique-product sets: the Promislow group and a Heisenberg-type candidate*](https://arxiv.org/abs/2607.18346) (arXiv:2607.18346, 2026). Studies minimal non-unique-product sets in torsion-free groups, the combinatorial obstruction the paper discusses alongside Rips–Segev, Steenbock and Mian–Siddique.

## Digests and expositions
- [Claude Opus 5.5 / Open Mathematics Courses, *A torsion-free group algebra with zero divisors*](https://kokunoyumeto.github.io/open-math-courses-public/courses/torsion-free-group-algebra-with-zero-divisors/index.html) (Open Mathematics Courses, undated). Ten lessons explain the paper’s prescribed graph types, probabilistic estimates, planar separation, cone pictures and cancellation argument, with examples and exercises; the source states that independent review is incomplete. [AI-generated per source]
- [AI Proved What?, *Torsion-free, yet zero? Kaplansky’s zero-divisor conjecture*](https://aiprovedwhat.com/episodes/196-counterexample-kaplanskys-zero-divisor-conjecture/) (episode 196, October 2026). Video and transcript explain the parity mechanism and the separate nonvanishing and torsion-freeness arguments, illustrate a small toy construction, and report a source inspection of the Lean files without running the proof checker. [AI-generated per source]

## News and blogs
- [Azmat, *Kaplansky Zero-Divisor Conjecture: Inside OpenAI’s Remarkable Counterexample*](https://binaryverseai.com/kaplansky-zero-divisor-conjecture/) (BinaryVerse AI, 10 October 2026; [video version](https://www.youtube.com/watch?v=IxFs-Q4yO50)). Explains the manuscript’s characteristic-two cancellation, root separation and asphericity arguments and distinguishes its claim from the related unit conjecture.
