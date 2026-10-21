# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [maximusrufus, bocowgill, mo271 (GitHub), *Add reference note: claimed proof of intersectionMultiplicity_pos (unrefereed; status unchanged)*](https://github.com/google-deepmind/formal-conjectures/pull/7215) (google-deepmind/formal-conjectures PR #7215, opened 2026-10-12, open). A docstring-only PR that records Theorem 1.1 as an unrefereed claim and leaves `intersectionMultiplicity_pos` as research open; in a 2026-10-19 reply the PR author says they reviewed the proof in detail and found no errors, but that it should stay labelled "claimed, unrefereed".

## Formalization
- [unaoya (GitHub), *SerrePositivity*](https://github.com/unaoya/SerrePositivity) (GitHub repository, accessed 2026-10-21). An early-stage independent Lean 4 project to formalize this paper, with Theorem 1.1 stated with `sorry` and the paper's Theorems 3.1 and 4.7 planned as named axioms; a `sorry`-free core step derives $\chi>0$ only from an assumed input bundle.
- [mo271 (GitHub), *Wikipedia/SerreMultiplicityConjectures: the positivity conjecture is true*](https://github.com/google-deepmind/formal-conjectures/issues/6911) (google-deepmind/formal-conjectures issue #6911, 2026-10-07, open, label "solution found"). Proposes marking `intersectionMultiplicity_pos` and `intersectionMultiplicity_pos_quotient` as solved on the basis of this paper; the author says the comparison was prepared with AI assistance and should be checked against the Lean statements.
- [j2d9w5xtjn-png, *feat: add Serre's multiplicity conjectures*](https://github.com/google-deepmind/formal-conjectures/pull/5382) (google-deepmind/formal-conjectures PR #5382, merged 2026-09-23). This independent, AI-assisted contribution defines intersection multiplicity and states the module and prime-quotient positivity conjectures, without formalizing the manuscript's proof. [AI-generated per source]
- [Formal Conjectures authors, *FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/SerreMultiplicityConjectures.lean) (google-deepmind/formal-conjectures, accessed 2026-10-21). Lean statements of Serre's conjectures, all with `sorry` proofs; the general positivity statements that Theorem 1.1 addresses are still tagged research open, and the equicharacteristic and unramified cases are tagged solved.

## Related prior literature mentioned by others
- [Andrei Suslin and Vladimir Voevodsky, *Singular homology of abstract algebraic varieties*](https://www.math.ias.edu/vladimir/sites/math.ias.edu.vladimir/files/singular_homology_published.pdf) (Inventiones Mathematicae 123, 61–94, 1996). Ying Xie's survey (§7.7, §9.1.5) identifies its pseudo-Galois covering and orbit argument as an uncited antecedent of the manuscript's supported rational descent construction; no Suslin–Voevodsky work appears in the paper's bibliography.
- [Editan, Copilot and Gemini, *Θ：セールの正値性予想の構造的始原による完結：交叉多重度による代数幾何学的存在証明*](https://note.com/editan/n/n35dec2c1ddbe) (note.com, 2025-12-09). The manuscript's introductory footnote and Xie's survey mention this earlier assertion of the prime-quotient positivity conjecture as a claim, rather than an established theorem. [AI-generated per source]

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*, Section 9.1.5 "193 · Serre's positivity conjecture"](https://arxiv.org/html/2610.17090) (arXiv:2610.17090 [math.HO], 2026-10-12). An AI-assisted survey of the whole release whose section on this paper extracts three "instruments": supported rational descent, the rank quotient with supported asymptotic complexes, and the two Galois-norm comparisons. Its caveats say the Verdier-quotient identification (perfect modules over a connective algebra, base change, spectral sequences on idempotent summands, ultralimits) needs checking and that the argument depends on 2022–2026 results. [AI-generated per source] [family-level]

## News and blogs
- None found.
