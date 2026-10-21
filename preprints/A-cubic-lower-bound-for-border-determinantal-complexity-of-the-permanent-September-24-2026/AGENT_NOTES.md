# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Karthik Sheshadri, *Conormal Lower Bounds for Determinantal Complexity: Fermat Slices, Tight Bounds, and a Ceiling*](https://arxiv.org/abs/2606.15970) (arXiv:2606.15970v2, revised 14 Oct 2026). The October revision cites this paper as [OAI26] and proves an $O(n^3)$ ceiling for polar/conormal (characteristic-cycle and kernel-system) arguments on the $n\times n$ permanent, stating that "the cubic lower bound of [OAI26] shows that this order is attained for the permanent".
- [Jizhou Guo, *An n^2 log log n Lower Bound for Permanent Circuits with Valid Division*](https://arxiv.org/abs/2609.29568) (arXiv:2609.29568v2, 8 Oct 2026). Version 2 cites this manuscript (release commit adc7f12) and uses twelve machine-checked declarations from its Lean development, deriving one weaker bound by "assuming Proposition 7.3 of that manuscript".
- [Ying Xie, *Smooth slices and superquadratic border determinantal complexity of the permanent*](https://zenodo.org/records/23108131) (Zenodo, doi:10.5281/zenodo.23108131, 2 Oct 2026). This preprint claims an Ω(n^2 log n) border determinantal complexity bound for the permanent, combining "the matching-polynomial restrictions of OpenAI with Sheshadri's determinantal kernel incidence".

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *A cubic permanent–determinant lower bound: Lean formalization scope*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/108.md) (release repository mirror, 6 Oct 2026). The scope note reports formalizations of the exact and border bounds $n\ge m^3/(5529600e)$ for $m\ge1408$ and the supporting smooth-initial-form bound (r−1)(d−1)/(4e), excluding the algebraic-branching-program consequences. [family-level]
- [OpenAI math release, *PermanentCubic.lean* comparator statement](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PermanentCubic.lean) (openai/math, commit adc7f12). Statement-only comparator file (proof left as `sorry`) for `permanent_cubic_lower_bounds`, with border and exact versions of the bound m^3/(5529600e) ≤ n.

## Related prior literature mentioned by others
- [OpenAI, *Ten Advances in Mathematics and Theoretical Computer Science*, Chapter 5 "Arithmetic circuit complexity"](https://cdn.openai.com/pdf/ten-proofs-oai.pdf) (OpenAI PDF, updated 6 Aug 2026). Guo (arXiv:2609.29568) cites this chapter alongside the present manuscript as the source of the permanent "block construction and critical-locus estimate". [AI-generated per source]
- [Joseph M. Landsberg, Laurent Manivel and Nicolas Ressayre, *Hypersurfaces with degenerate duals and the Geometric Complexity Theory Program*](https://ems.press/journals/cmh/articles/11963) (Commentarii Mathematici Helvetici 88(2), 2013). Sheshadri's October revision identifies this quadratic border determinantal lower bound as the predecessor to the paper's cubic bound.

## Possibly relevant literature (found by the agent, not checked)
- [Karthik Sheshadri, *A short proof of a quadratic lower bound on the border determinantal complexity of x_1^n+⋯+x_n^n over ℂ: A simple human exposition*](https://arxiv.org/abs/2606.11090) (arXiv:2606.11090v2, revised 18 Oct 2026). Proves a border bound of (n−1)^2/(4e) for the power sum via kernel equations and multihomogeneous Bézout counting, comparable to the paper's smooth-form border bound (r−1)(d−1)/(4e); not in the paper's bibliography.
- [Prerona Chatterjee, Mrinal Kumar, Adrian She, Ben Lee Volk, *A Quadratic Lower Bound for Algebraic Branching Programs and Formulas*](https://arxiv.org/abs/1911.11793) (arXiv:1911.11793, 2019/2020). Gives an earlier Ω(n^2) vertex lower bound for general ABPs, relevant to the paper's Ω(m^3) ABP consequence; not in the paper's bibliography.

## Digests and expositions
- [Latent Seminar, *Cubic lower bounds for permanent determinant representations*](https://lowrank.github.io/latent-seminar/OpenAI-Math/108-permanent-determinant-lower-bound) (2026-10-07). Exposition of the smooth-form obstruction, coefficient-selection construction and persistence under border limits; it states that it does not independently verify the proof or rebuild the Lean development. [family-level]

## News and blogs
- [Azmat, *Permanent vs Determinant Problem: How OpenAI's Proof Broke the Quadratic Barrier*](https://binaryverseai.com/permanent-vs-determinant-problem-openai-proof/) (BinaryVerse AI, 2026-10-16). Article outlining the characteristic-two geometry and polar-intersection argument, distinguishing the determinant-size bound from running-time bounds and superpolynomial separation.
