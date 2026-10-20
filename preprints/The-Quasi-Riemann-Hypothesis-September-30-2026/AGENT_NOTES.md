# Automatically collected context

Collected by an AI agent (Claude Opus 5.5) on 2026-10-20. Not reviewed by a human; may be incomplete or wrong. Corrections: open an issue.

## Follow-up works
- [Baiying Liu, *Improved zero-free half-planes for the quasi-Riemann hypothesis*](https://arxiv.org/abs/2610.12234) (arXiv:2610.12234, v1 2026-10-08, v2 2026-10-12). Retunes three parameters of this paper's argument to lower the constant from 7/8 to about 0.874957, and states the result is formalized in Lean.
- [Yuanda Xu, Hejian Sang, *Amplified moments and a refinement of the quasi-Riemann hypothesis*](https://arxiv.org/abs/2610.15291) (arXiv:2610.15291, v1 2026-10-11, v2 2026-10-15). Assuming this paper's analytic inputs, improves the boundary to 0.8748867 via an amplified first moment.
- [Dean Cureton, Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind zeta functions*](https://hexagonmath.org/2610.00200) (hexagon:2610.00200, v2 2026-10-14). Proves a zero-free half-plane Re s > 31/32 for all Dedekind zeta functions, citing this paper and its 11/12 companion; proofs and Lean formalization attributed to AxiomProver.
- [Sayed Barez, *Ramanujan's prime counting inequality holds for all x ≥ 38,358,837,683*](https://hexagonmath.org/2610.00375v1) (hexagon:2610.00375, 2026-10-19). Uses this paper's 7/8 zero-free half-plane as an input to its main theorem.
- [Manjul Bhargava, *Rational points on elliptic curves that are primitive modulo a positive proportion of primes*](https://hexagonmath.org/2610.00294v1) (hexagon:2610.00294, 2026-10-17). Cites this paper; its key zero-free input is the Cureton–Thorner Dedekind half-plane.
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release*](https://arxiv.org/abs/2610.17090) (arXiv:2610.17090, 2026-10-12). Survey that describes the sextic-twist/cubic-Gauss-sum device of family 003 and classes it as a combination "leaning new".

## Expert comments and discussion
- [Persiflage (galoisrepresentations.org), *A Brief Digest of Some New OpenAI Results*](https://galoisrepresentations.org/2026/10/08/a-brief-digest-of-some-new-openai-results/) (2026-10-08). Calls quasi-RH for Dirichlet L-functions a very strong intermediate result and notes that the Dedekind-zeta version (needed for Stark–Odlyzko-type applications) is not proved.
- [DH, comment on the same post](https://galoisrepresentations.org/2026/10/08/a-brief-digest-of-some-new-openai-results/#comment-28529) (2026-10-09). Points out that a sibling Artin-conjecture manuscript contains a more general quasi-RH for some cyclotomic Hecke characters.
- [Harald Helfgott, comment on the same post](https://galoisrepresentations.org/2026/10/08/a-brief-digest-of-some-new-openai-results/#comment-28563) (2026-10-11). Says he looks forward to studying the proof and mentions its convex-hull idea and use of theta functions.
- [Andrei, comment on the same post](https://galoisrepresentations.org/2026/10/08/a-brief-digest-of-some-new-openai-results/#comment-28598) (2026-10-14). Links the Cureton–Thorner Dedekind-zeta preprint.
- [Hector Pasten, quoted in Scientific American](https://www.scientificamerican.com/article/the-most-exciting-claims-from-openais-heap-of-new-proofs/) (2026-10-08). Says the result is "way more than enough for many applications" while it is unclear whether it is progress toward full RH.
- [Tim Santens, Ben Green, Jakob Glas, Álvaro Lozano-Robledo, Phillip Harris, quoted in the Proofs and Prompts reactions roundup](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/) (2026-10-08). Several express surprise that a 7/8 zero-free region was obtained; Harris notes that no one has fully digested it yet.
- [Alex Kontorovich and Jared Duker Lichtman, X posts as quoted on Emergent Mind](https://www.emergentmind.com/openai-math-explorer/results/003) (2026-10-06). Kontorovich reacts to the result as a major breakthrough; Lichtman notes the cubic family of L-functions appears essential to the proof.
- [Abhishek Saha, X posts as compiled by Hraness](https://hraness.com/reading/mathematician-reactions-to-openais-372-math-results) (2026-10-07). Places quasi-RH alone in his top "shock breakthrough" tier of the release.
- [Terence Tao, *A sketch of the proof of non-existence of Siegel zeroes*](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/) (2026-10-19). Remarks in passing that the QRH papers rely on an "automorphic miracle" to break the parity barrier.

## Formalization
- [OpenAI, Lean scope note for family 003](https://github.com/openai/math/blob/main/lean/docs/003.md) (openai/math, 2026-10). Formalizes the 7/8 half-plane for ζ, all Dirichlet L-functions and finite-order Hecke L-functions over Q(√−3); later applications are not included.
- [whataifound.org, quasi-Riemann hypothesis entry](https://whataifound.org/finding/2026-10-06-quasi-riemann-hypothesis) (2026-10-07). Reports the Lean development size and that no outside party had been recorded running the Comparator challenges.

## Related prior literature mentioned by others
- [Hooley (Artin's conjecture), Stark and Odlyzko (discriminant bounds), Vinogradov–Korobov zero-free regions, named in Persiflage's post and comments](https://galoisrepresentations.org/2026/10/08/a-brief-digest-of-some-new-openai-results/) (2026-10-08). Discussed as the classical context for applications and for prior zero-free regions.

## News and blogs
- [Peter Hall and Joseph Howlett, Scientific American](https://www.scientificamerican.com/article/the-most-exciting-claims-from-openais-heap-of-new-proofs/) (2026-10-08). News overview leading with the quasi-RH claim.
- [David H. Bailey, *OpenAI stuns mathematicians with 722 new papers*, Math Scholar](https://mathscholar.org/2026/10/openai-stuns-mathematicians-with-722-new-papers/) (2026-10-07, updated 2026-10-19). Blog coverage describing the 7/8 and 11/12 results.
- [Zvi, *New Math from OpenAI*, LessWrong](https://www.lesswrong.com/posts/eyqxBuxXCaamNSxBB/new-math-from-openai) (2026-10-09). Roundup explaining quasi-RH applications and collecting reactions.
