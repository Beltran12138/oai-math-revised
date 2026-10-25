# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *Lean scope notes for family 150*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/150.md) (release repository, lean/docs/150.md, October 2026). States that the Lean development proves the ergodicity theorem of this paper, constructing the flow off a null set, proving uniqueness of the flight chain, measure preservation and the flow law a.e. [family-level]
- [OpenAI, *IrrationalTriangleBilliard.lean*](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/IrrationalTriangleBilliard.lean) (openai/math, lean/ComparatorChallenges, October 2026). Comparator statement `irrational_triangle_billiard` for a triangle with an angle irrational relative to π; its conclusion bundles a.e. flow construction, measure preservation and that invariant sets have measure 0 or 1 (the proof is left as `sorry` in this statement file). Comparator challenge files leave the proof as `sorry` by design; `IrrationalTriangleBilliard.json` names the module `OAI.Dynamics.TriangleBilliards.Main` as the release's proof of this statement. [family-level]

## Related prior literature mentioned by others
- [Giovanni Forni and Nelson Moll, *Cohomological equation for geodesic flows on flat surfaces*](https://arxiv.org/abs/2510.18128v1) (arXiv:2510.18128v1, 2025-10-20). [Azmat’s exposition](https://binaryverseai.com/irrational-triangular-billiards-openai-proof/) identifies this work as the analytic framework behind the family’s treatment of invariant functions and highlights the horizontal Sobolev regularity assumption that this manuscript seeks to remove. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [G. Casati, T. Prosen, *Mixing property of triangular billiards*](https://arxiv.org/abs/chao-dyn/9908022) (arXiv:chao-dyn/9908022; Phys. Rev. Lett. 83, 1999). Numerical evidence that triangles with all angles irrational are mixing; complements the numerical studies [WCP, ZSBJ] the paper cites as raising doubts about ergodicity.
- [J. Seaward, *Ergodicity in Golden Billiards*](https://arxiv.org/abs/1910.14350) (arXiv:1910.14350, 2019). Comment on the Wang–Casati–Prosen numerics (cited as [WCP]) arguing that "strongly irrational" right triangles are likely ergodic; directly relevant to the paper's discussion of [WCP].
- [Z. Hwang, C. A. Marx, J. Seaward, S. Jitomirskaya, M. Olshanii, *Growth of the Wang-Casati-Prosen counter in an integrable billiard*](https://arxiv.org/abs/2011.09467) (SciPost Phys. 14, 017 (2023); arXiv:2011.09467). Studies the counter underlying the Wang–Casati–Prosen non-ergodicity evidence for irrational right triangles, which the paper cites as [WCP].
- [S. Troubetzkoy, *Approximation and billiards*](https://arxiv.org/abs/math/0611599) (arXiv:math/0611599, 2006). Survey of ergodicity and weak-mixing results via the Katok–Zemlyakov approximation method, i.e. the genericity results (KMS, Vorobets) the paper contrasts with its every-triangle statement.
- [Č. Lozej, G. Casati, T. Prosen, *Quantum chaos in triangular billiards*](https://arxiv.org/abs/2110.04168) (arXiv:2110.04168; [Phys. Rev. Research 4, 013138, 2022](https://doi.org/10.1103/PhysRevResearch.4.013138)). Numerical study of eigenvalues, spectral statistics and eigenfunction localization in irrational and one-rational-angle triangles; related to the paper's quantum-ergodicity consequences in its spectral section.

## Digests and expositions
- [Azmat, *Irrational Triangular Billiards: How OpenAI’s Proof Tackles a Decades-Old Ergodicity Mystery*](https://binaryverseai.com/irrational-triangular-billiards-openai-proof/) (Binary Verse AI, 2026-10-15). Explains this manuscript’s Fourier-coefficient estimates, successive limits and quantum consequences, and identifies the October companion’s stronger weak-mixing claim while disclaiming independent verification of every analytic step. [family-level]
- [heyprof, *Triangular billiards — irrational angles mix (3D)*](https://www.heyprof.app/en/demo/dreiecksbillard) (interactive exposition, undated; accessed 2026-10-21). Illustrates family 150 using trajectories, direction distributions and paired trajectories, noting that floating-point simulation cannot distinguish exact rationality from irrationality. [family-level]

## News and blogs
- None found.
