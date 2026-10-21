# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [Nic Berkopec, *Crouzeix: Folie à Deux*](https://math.washu.edu/events/crouzeix-folie-deux) (Washington University in St. Louis analysis seminar, 2026-10-19). The seminar abstract notes that the earlier scalar proof methods do not extend directly to the completely bounded case and explicitly associates that case with the OpenAI release. [family-level]
- [trostaft on Hacker News, comment in the thread *Sharing AI progress in mathematics*](https://news.ycombinator.com/item?id=49986658) (Hacker News, 2026-10-07). Brief comment naming family 325 among the release items of interest; the commenter says they have attended talks on the Crouzeix conjecture and suggests a connection to convergence rates for Krylov methods. [family-level]

## Formalization
- [OpenAI / mathcommunity mirror, *Lean scope notes for family 325: The complete Crouzeix conjecture*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/325.md) (lean/docs/325.md, release of 2026-10-06). The release's own scope document; it lists comparator challenges for the complete polynomial inequality (`CompleteCrouzeix.lean`), the optimal similarity and boundary representation (`StructuralCrouzeix.lean`), the Hilbert-space version (`CrouzeixHilbert.lean`) and supporting numerical-range geometry (`HilbertCrouzeix.lean`), together with holomorphic and rational extensions. [family-level]
- [Beltran12138, *oai-math-recheck*](https://github.com/Beltran12138/oai-math-recheck) (GitHub repository, October 2026). Independent re-run of the release's Lean files for family 325, including rebuilds of the `CrouzeixHilbert`, `CompleteCrouzeix` and `StructuralCrouzeix` statements and a check that the `CompleteCrouzeix` proof closes the `DirectCrouzeix` challenge; the README stresses that this is agreement between two OpenAI formalizations and that statement faithfulness remains a human judgement. [family-level]

## Related prior literature mentioned by others
- [Emiel Lorist and Felix Schwenninger, *A solution to Crouzeix’s conjecture*](https://arxiv.org/abs/2608.03841v2) (arXiv:2608.03841v2, 2026-08-17). Xie’s survey, §9.4.6, identifies this scalar predecessor and its explicit limitation that the commutativity argument does not directly survive matrix amplification. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [R. Clouâtre, M. Ostermann, T. Ransford, *An abstract approach to the Crouzeix conjecture*](https://arxiv.org/abs/2011.10422) (arXiv:2011.10422, 2020/2022). Discusses a completely bounded version of their abstract conjecture via dilation theory; relevant to the paper's claim that the closure of $W(A)$ is a complete 2-spectral set and its use of Paulsen/Arveson, and not in its bibliography.
- [M. Hartz, J. E. McCarthy, *From Clouatre-Ostermann-Ransford to Okubo-Ando*](https://arxiv.org/abs/2606.02922) (arXiv:2606.02922, 2026-06-01). Proves a completely bounded norm estimate for unital homomorphisms of operator algebras in the COR setting; related to the paper's identification of the optimal similarity constant with a completely bounded norm (Theorem 1.2 and its Paulsen-similarity discussion).
- [K. R. Davidson, V. I. Paulsen, H. J. Woerdeman, *Complete spectral sets and numerical range*](https://arxiv.org/abs/1612.05683) (arXiv:1612.05683, 2016-12-17). Shows that a complete $C$-spectral set is a complete $(C+C^{-1})/2$-numerical radius set; with constant 2 this gives a numerical-radius consequence of the paper's complete 2-spectral-set claim.
- [C. Badea, R. O'Loughlin, J. Virtanen, *On the abstract approach to spectral constants: a proof of the Clouâtre–Ostermann–Ransford conjecture*](https://arxiv.org/abs/2609.03637) (arXiv:2609.03637, 2026-09-03). Proves the scalar-norm COR conjecture for homomorphisms into $B(H)$ via positivity of real parts and an operator-valued Herglotz theorem; comparable in method to the paper's positive boundary representation (Theorem 1.3).

## Digests and expositions
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*](https://arxiv.org/abs/2610.17090) (arXiv:2610.17090, 2026-10-12). Survey of 38 release families whose Section 9.4.6 compares both family-325 manuscripts, discussing this paper's optimal-metric theorem (Stein LMI, $\kappa\in[1,2]$) and noting that the structural theorem holds for each enclosing domain separately, with no limiting similarity on the closure of $W(A)$ asserted. [AI-generated per source] [family-level]
- [Latent Seminar, *The complete Crouzeix inequality*](https://lowrank.github.io/latent-seminar/OpenAI-Math/325-complete-crouzeix) (2026-10-06). This exposition explains both the direct Faber-coefficient argument and the structural metric-and-density argument, including their different scopes, and explicitly disclaims independent verification of the complete proofs. [family-level]

## News and blogs
- None found.
