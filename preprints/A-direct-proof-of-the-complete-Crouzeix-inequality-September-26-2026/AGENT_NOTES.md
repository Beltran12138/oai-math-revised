# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- [Nic Berkopec, *Crouzeix: Folie à Deux*](https://math.washu.edu/events/crouzeix-folie-deux) (Washington University in St. Louis analysis seminar, 2026-10-19). The seminar abstract notes that the earlier scalar proof methods do not extend directly to the completely bounded case and explicitly associates that case with the OpenAI release. [family-level]
- [trostaft on Hacker News, comment in the thread *Sharing AI progress in mathematics*](https://news.ycombinator.com/item?id=49986658) (Hacker News, 2026-10-07). Brief comment naming family 325 among the release items of interest; the commenter says they have attended talks on the Crouzeix conjecture and suggests a connection to convergence rates for Krylov methods. [family-level]

## Formalization
- [OpenAI / mathcommunity mirror, *Lean scope notes for family 325: The complete Crouzeix conjecture*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/325.md) (lean/docs/325.md, release of 2026-10-06). The release's own scope document, listing five comparator statements; this paper's statement (complete inequality and sharpness) corresponds to the challenge `DirectCrouzeix.lean`, with further challenges for the Hilbert-space and structural versions. [family-level]
- [Beltran12138, *oai-math-recheck*](https://github.com/Beltran12138/oai-math-recheck) (GitHub repository, October 2026). Independent re-run of the release's Lean files for family 325: reports compilation, an axiom audit (only `propext`, `Classical.choice`, `Quot.sound`), a statement-equivalence check against `DirectCrouzeix`, and a negative control; the README stresses that faithfulness of the formal statement to the paper remains a human judgement. [family-level]

## Related prior literature mentioned by others
- [Emiel Lorist and Felix Schwenninger, *A solution to Crouzeix’s conjecture*](https://arxiv.org/abs/2608.03841v2) (arXiv:2608.03841v2, 2026-08-17). Xie’s survey, §9.4.6, identifies this scalar predecessor and its explicit limitation that the commutativity argument does not directly survive matrix amplification. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [R. Clouâtre, M. Ostermann, T. Ransford, *An abstract approach to the Crouzeix conjecture*](https://arxiv.org/abs/2011.10422) (arXiv:2011.10422, 2020/2022). Formulates the abstract (COR) conjecture and discusses a completely bounded version via dilation theory; relevant to the paper's uniformity-in-coefficient-dimension claim (Theorem 1.1) and not in its bibliography, although the cited Åhag–Czyż–Virtanen paper treats this conjecture.
- [C. Badea, R. O'Loughlin, J. Virtanen, *On the abstract approach to spectral constants: a proof of the Clouâtre–Ostermann–Ransford conjecture*](https://arxiv.org/abs/2609.03637) (arXiv:2609.03637, 2026-09-03). Proves the scalar-norm COR conjecture using positivity of real parts, an operator-valued Herglotz theorem and the Lorist–Schwenninger perturbation lemma; comparable to the positivity of $R+R^*$ used in the paper's block comparison (Section 3).
- [K. R. Davidson, V. I. Paulsen, H. J. Woerdeman, *Complete spectral sets and numerical range*](https://arxiv.org/abs/1612.05683) (arXiv:1612.05683, 2016-12-17). Shows that a complete $C$-spectral set is a complete $(C+C^{-1})/2$-numerical radius set; with constant 2 this gives a numerical-radius consequence of the paper's main theorem.

## Digests and expositions
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*](https://arxiv.org/abs/2610.17090) (arXiv:2610.17090, 2026-10-12). Survey of 38 release families whose Section 9.4.6 compares both family-325 manuscripts, describing this paper's "ordered density comparison" (top-singular-pair compression of the Crouzeix–Palencia kernel with Hilbert–Schmidt/Faber-coefficient bounds) as "combination leaning new" and noting that its novelty comparison with Luo 2026 is incomplete. [AI-generated per source] [family-level]
- [Latent Seminar, *The complete Crouzeix inequality*](https://lowrank.github.io/latent-seminar/OpenAI-Math/325-complete-crouzeix) (2026-10-06). This exposition explains both the direct Faber-coefficient argument and the structural metric-and-density argument, including their different scopes, and explicitly disclaims independent verification of the complete proofs. [family-level]

## News and blogs
- None found.
