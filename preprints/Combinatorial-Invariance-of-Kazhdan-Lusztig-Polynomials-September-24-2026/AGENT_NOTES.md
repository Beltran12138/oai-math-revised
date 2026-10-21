# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [F. Caselli and M. Marietti, *A simple classification of the special matchings in the symmetric group*](https://arxiv.org/abs/2610.21647) (arXiv:2610.21647, 15 Oct 2026). Gives a combinatorial algorithm for Kazhdan–Lusztig polynomials on an isomorphism-closed family of type-A Bruhat intervals; its Remark 1.2 cites this manuscript as [28] and notes that it "claims to prove the Combinatorial Invariance Conjecture".
- [Nicolás Libedinsky, *Polytopal invariance for Lusztig’s q-weight multiplicities*](https://arxiv.org/html/2610.14275v1) (arXiv:2610.14275v1, 2026-10-09). Cites the OpenAI manuscript as an announced proof, establishes a metric spherical analogue, and proposes in §6.1 a conjecture connecting polytope isometries to Bruhat interval isomorphisms; the AI-use disclosure describes an AI-produced initial argument subsequently corrected and expanded by the author.

## Comments and discussion
- [Sara Billey, *OpenAI publishes new math research on GitHub*](https://www.linkedin.com/posts/sara-billey-85440a159_openai-posted-a-lot-of-new-math-research-activity-7513431670612557824-mW4j) (LinkedIn, undated). Highlights the claimed proof of the Kazhdan–Lusztig combinatorial invariance conjecture and asks how to approach the volume of released work, without offering a technical assessment.

## Formalization
- [OpenAI, *Combinatorial invariance of Kazhdan–Lusztig polynomials: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/168.md) (OpenAI math release, 2026-10-06). States that the formalization proves that every order isomorphism between Bruhat intervals in arbitrary, possibly different Coxeter systems preserves the equal-parameter Kazhdan–Lusztig polynomial, and links the comparator statement `KLInvariance.lean`.
- [OpenAI math release, comparator statement `KLInvariance.lean`](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/KLInvariance.lean) (release Lean comparator challenge, 2026). Statement-only file: theorem `combinatorial_invariance` takes an order isomorphism `Interval cs u b ≃o Interval cs' u' b'` and concludes `klPolynomial cs u b = klPolynomial cs' u' b'`.
- [OpenAI math release, `Invariance.lean`](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean) (release Lean development, 2026). Contains the proof of `KLInvariance.combinatorial_invariance`, which imports `OAI.RepresentationTheory.KazhdanLusztig.SimultaneousInvariance`.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [G. Burrull, N. Libedinsky, and D. Plaza, *Combinatorial invariance conjecture for $\widetilde{A}_2$*](https://arxiv.org/abs/2105.04609) (arXiv:2105.04609, 2021; IMRN, doi:10.1093/imrn/rnac105). Proves the conjecture for the affine Weyl group $\widetilde{A}_2$, a previously known infinite case of the statement the paper says includes infinite groups.
- [G. T. Barkley and C. Gaetz, *On combinatorial invariance of parabolic Kazhdan–Lusztig polynomials*](https://arxiv.org/abs/2404.04246) (arXiv:2404.04246, 2024; Selecta Math. 31 (2025), 51). Shows that the Lusztig–Dyer conjecture is equivalent to Marietti's parabolic analogue and a refined parabolic version, which bears on what Theorem 1.1 would imply in the parabolic setting.
- [F. Esposito and M. Marietti, *Flipclasses and Combinatorial Invariance for Kazhdan–Lusztig polynomials*](https://arxiv.org/abs/2402.13097) (arXiv:2402.13097, 2024). Introduces the flipclass approach that the introduction cites only through the later Esposito–Marietti–Stella paper.
- [F. Esposito, M. Marietti, G. T. Barkley, and C. Gaetz, *A note on Combinatorial Invariance of Kazhdan–Lusztig polynomials*](https://arxiv.org/abs/2404.12834) (arXiv:2404.12834, 2024). Formulates a hypercube-decomposition conjecture that implies type-A combinatorial invariance, related to the hypercube approach surveyed in the introduction.

## Digests and expositions
- None found.

## News and blogs
- [Gil Kalai, *Updates: Sharing AI progress on mathematics (amazing!); and my lecture plans*](https://gilkalai.wordpress.com/2026/10/07/updates-sharing-ai-progress-on-mathematics-amazing-and-my-lecture-plans/) (Combinatorics and more, 7 Oct 2026). Item 14 lists this result, notes it was "Problem 11 in my discussions of the G-programme", and restates the theorem.
