# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [mo271, *Paper/EisenbudGreenHarris: the conjecture holds in characteristic zero for degrees at least two*](https://github.com/google-deepmind/formal-conjectures/issues/6913) (google-deepmind/formal-conjectures issue #6913, 2026-10-07). Cites this paper and proposes adding a `char_zero` variant (characteristic zero, all degrees ≥ 2) tagged as solved, keeping the general statement open; no Lean proof, and the issue says its comparison was AI-assisted and needs checking. [AI-generated per source]
- [Formal Conjectures authors, *FormalConjectures/Paper/EisenbudGreenHarris.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Paper/EisenbudGreenHarris.lean) (google-deepmind/formal-conjectures, accessed 2026-10-21). Lean 4 statement of the conjecture over an arbitrary field, tagged `research open`, with no characteristic-zero variant and all proofs `sorry` at the time of access; its docstring lists quadratic sequences with c ≤ 5 (Güntürkün–Hochster) as a known case.

## Related prior literature mentioned by others
- [S. Gunturkun and M. Hochster, *The Eisenbud-Green-Harris Conjecture for Defect Two Quadratic Ideals*](https://arxiv.org/abs/1812.07539) (arXiv:1812.07539, 2018). Listed as a known case in the Formal Conjectures docstring and not in this paper's bibliography; proves EGH for five quadrics in five variables, related to the introduction's account of the quadratic cases.

## Possibly relevant literature (found by the agent, not checked)
- [S. Gunturkun, *A Survey on The Eisenbud-Green-Harris Conjecture*](https://arxiv.org/abs/2103.14106) (arXiv:2103.14106, 2021). A survey of earlier EGH results grouped by approach, alongside the account in the "Earlier results on EGH" subsection.
- [G. Caviglia and E. Sbarra, *Distractions of Shakin rings*](https://arxiv.org/abs/1308.4659) (arXiv:1308.4659, 2013). Extends Abedelfatah's EGH results to a wider class of ideals using Hilbert-function embeddings, related to the special cases listed in the introduction.
- [Benjamin P. Richert and Sindi Sabourin, *The residuals of lex plus powers ideals and the Eisenbud-Green-Harris conjecture*](https://arxiv.org/abs/math/0508334) (arXiv:math/0508334, 17 August 2005). Relates the family's Hilbert-function and Betti-number claims by proving an equivalence between EGH and extremality of the last graded Betti numbers of lex-plus-powers ideals. [family-level]

## Digests and expositions
- [AI Proved What?, *Count like monomials?*](https://aiprovedwhat.com/episodes/200-eisenbud-green-harris-lex-plus/) (episode 200, October 2026). Explains both manuscripts' characteristic-zero claims, the division-algebra construction and the transfer of resolutions, with examples and a distinction between its small-case checks and the unchecked geometric construction. [AI-generated per source] [family-level]
- [Orply, *One Monomial Ideal Matches the Entire Hilbert Function*](https://orply.com/articles/perplexity/200-2-commuting-division-coefficient-forms-and-the-artinian-eisenbud-green-harris-conjecture-5ad48b24) (11 October 2026). Summarizes the commuting-form construction and least-exponent extraction of a Hilbert-matching monomial ideal, distinguishing the Artinian construction over the complex numbers from the extension to characteristic-zero fields. [AI-generated per source]

## News and blogs
- [Cyber, *Cryptographic assumptions audit*](https://cyber.page/audit/cryptography-2026-10-08/) (public audit, 8 October 2026; release discussion dated 9 October 2026). Discusses family 200 as a possible source of degree-of-regularity bounds in Gröbner-basis cryptanalysis, noting that transfer from characteristic zero to finite-field systems would require an additional assumption. [family-level]
