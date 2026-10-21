# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Ricardo Pinho, *An explicit finite cylinder cover of the regular tetrahedron saving $3.86\times10^{-4}$ below the half-area bound*](https://hexagonmath.org/abs/2610.00304v2) (hexagon:2610.00304v2, v1 17 Oct 2026, v2 18 Oct 2026). Uses a finite tilt in this paper's angular-sector framework, with rational radial cutoffs, to give a 4096-cylinder triangular-base cover of normalized area about 0.499613830783714, certified by exact LP dual witnesses; it cites all four family preprints. The source states that the text is primarily AI-generated and that no optimality is claimed. [AI-generated per source]
- [Ricardo Pinho (with contributions by Alexander Richard Towell), *tetrahedron-cylinder-cover* (GitHub)](https://github.com/rpinho/tetrahedron-cylinder-cover) (code repository, October 2026). Certificates and two independent exact checkers for the 4096-cylinder cover; the README compares it with this paper's small-tilt example (saving about 5.4×10⁻¹⁰ with 16,000,000 cylinders). The README also states that the release's `TriangularCovering.lean` encodes the quantities but is not by itself a checked proof of the paper, its final comparator theorem containing `sorry`. [AI-generated per source]

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 100: Cylinder coverings below the half-area bound*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/100.md) (lean/docs/100.md, 2026). Describes the release's Lean statements for this paper: finite triangular-base covers of the regular tetrahedron with the $1/2-(13/6000)\varepsilon^2+O(\varepsilon^4)$ expansion, and the directionwise counterexample, linking the aggregate and triangular-cover comparator statements; the affine extension to all tetrahedra lies outside the selected statements. [family-level]
- [Erdős Problems library, *Openai 2026 finite angular cylinder covers below half area bound*](https://erdosproblems.ai/wiki/library/discrete_geometry/openai_2026_finite_angular_cylinder_covers_below_half_area_bound) (verification report, 8 October 2026). Reports rebuilding the release's aggregate and triangular-cover declarations and checking their axioms, distinguishing the aggregate's explicit constants from the qualitative triangular statement and excluding the all-tetrahedra affine extension.

## Related prior literature mentioned by others
- [Károly Bezdek and Alexander E. Litvak, *Packing convex bodies by cylinders*](https://arxiv.org/abs/1507.05115v2) (arXiv:1507.05115v2, 21 November 2015; Discrete Comput. Geom. 55 (2016) 725–738). The Erdős Problems library's angular-cover discussion connects this paper's multiple-cover lower bounds to the surviving directionwise one-third bound.

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- [Latent Seminar, *Finite cylinder coverings below the tetrahedral half-area bound*](https://lowrank.github.io/latent-seminar/OpenAI-Math/100-cylinder-coverings) (6 October 2026). Explains the four manuscripts' constructions, approximation hypotheses and two area normalizations, while expressly disclaiming independent verification of the complete proofs. [family-level]
- [heyprof, *Cylinders below the half-area bound (3D)*](https://www.heyprof.app/en/demo/zylinder-tetraeder) (interactive exposition, undated; accessed 21 October 2026). Illustrates the angular construction with adjustable tilt and sector count, distinguishing sampled gap tests at larger tilts from the theorem's small-parameter range.

## News and blogs
- None found.
