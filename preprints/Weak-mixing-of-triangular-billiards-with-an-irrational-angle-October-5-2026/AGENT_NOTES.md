# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *Lean scope notes for family 150*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/150.md) (release repository, lean/docs/150.md, October 2026). Describes a formalization of the September ergodicity theorem (a.e. flow construction, flight-chain uniqueness, measure preservation); it does not state that weak mixing, the main theorem of this paper, is formalized. [family-level]
- [OpenAI, *IrrationalTriangleBilliard.lean*](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/IrrationalTriangleBilliard.lean) (openai/math, lean/ComparatorChallenges, October 2026). Comparator statement `irrational_triangle_billiard` (flow construction a.e., measure preservation, and invariant sets of measure 0 or 1); this file states the ergodicity theorem only, with the proof left as `sorry`. [family-level]

## Related prior literature mentioned by others
- [Giovanni Forni and Nelson Moll, *Cohomological equation for geodesic flows on flat surfaces*](https://arxiv.org/abs/2510.18128v1) (arXiv:2510.18128v1, 2025-10-20). [Azmat’s exposition](https://binaryverseai.com/irrational-triangular-billiards-openai-proof/) identifies this work as the analytic framework behind the family’s treatment of invariant functions and highlights the horizontal Sobolev regularity assumption that the September manuscript seeks to remove. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [Č. Lozej, G. Casati, T. Prosen, *Quantum chaos in triangular billiards*](https://arxiv.org/abs/2110.04168) (arXiv:2110.04168, 2021). Large numerical study treating generic irrational triangles as presumed mixing and one-rational-angle triangles as presumed weakly mixing or non-ergodic; relevant to the paper's discussion of numerical evidence on weak mixing.
- [J. Seaward, *Ergodicity in Golden Billiards*](https://arxiv.org/abs/1910.14350) (arXiv:1910.14350, 2019). Comment on the Wang–Casati–Prosen numerics (cited as [WCP]) arguing that "strongly irrational" right triangles are likely ergodic; bears on the paper's remark on conflicting numerical observations.
- [Z. Hwang, C. A. Marx, J. Seaward, S. Jitomirskaya, M. Olshanii, *Growth of the Wang-Casati-Prosen counter in an integrable billiard*](https://arxiv.org/abs/2011.09467) (SciPost Phys. 14, 017 (2023); arXiv:2011.09467). Studies the counter on which the Wang–Casati–Prosen non-ergodicity evidence for irrational right triangles rests; related to the numerics the paper cites as [WCP].
- [S. Troubetzkoy, *Approximation and billiards*](https://arxiv.org/abs/math/0611599) (arXiv:math/0611599, 2006). Survey of transitivity, ergodicity and weak-mixing results for polygonal billiards obtained by the Katok–Zemlyakov approximation method, the genericity-type results the paper contrasts with its every-triangle statement.

## Digests and expositions
- [Azmat, *Irrational Triangular Billiards: How OpenAI’s Proof Tackles a Decades-Old Ergodicity Mystery*](https://binaryverseai.com/irrational-triangular-billiards-openai-proof/) (Binary Verse AI, 2026-10-15). Explains the September manuscript’s Fourier-coefficient estimates, successive limits and quantum consequences, and identifies the October companion’s stronger weak-mixing claim while disclaiming independent verification of every analytic step. [family-level]
- [heyprof, *Triangular billiards — irrational angles mix (3D)*](https://www.heyprof.app/en/demo/dreiecksbillard) (interactive exposition, undated; accessed 2026-10-21). Illustrates family 150 using trajectories, direction distributions and paired trajectories, noting that floating-point simulation cannot distinguish exact rationality from irrationality. [family-level]

## News and blogs
- [Orply, *AI-Generated Proofs Expand Mathematical Results but Leave Questions of Understanding*](https://orply.com/articles/two-minute-papers/openai-just-changed-what-it-means-to-do-math-3db4d2fc) (2026-10-13). This AI-assisted rendering of a Two Minute Papers video uses irrational triangular billiards as a specific example of the release’s claimed equidistribution results. [AI-generated per source] [family-level]
