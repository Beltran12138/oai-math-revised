# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 337: Sharp Cartan–Hadamard isoperimetry and rigidity*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/337.md) (release Lean docs, 2026). According to these notes, the Lean development proves the sharp filling bound $\mathbf M(S)\le C_n\mathbf M(T)^{(n+1)/n}$ for compactly supported integral $n$-cycles ($n\ge2$) in proper CAT(0) spaces (comparator `SharpCAT0Filling.lean`), and the optimality of the coefficient via a Euclidean example (comparator `FillingCoefficient.lean`).

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Cornelia Druţu, Urs Lang, Panos Papasoglu, Stephan Stadler, *Minimal tetrahedra and an isoperimetric gap theorem in non-positive curvature*](https://arxiv.org/abs/2502.03389) (arXiv:2502.03389, 5 Feb 2025). Treats Lipschitz 2-spheres filled by 3-balls in proper CAT(0) spaces, identifying $1/(6\sqrt\pi)$ (the paper's $c_2$) as the sharp gap-theorem threshold and proving a non-sharp Euclidean inequality for 2-spheres; both bear on the $n=2$ case of Theorem 1.1, and it is not in the bibliography.
- [Stefan Wenger, *Gromov hyperbolic spaces and the sharp isoperimetric constant*](https://arxiv.org/abs/math/0609310) (arXiv:math/0609310, 2006–2007). Establishes the sharp quadratic constant for 1-cycles and its relation to Gromov hyperbolicity, the $n=1$ counterpart of the sharp-coefficient question the paper settles for $n\ge2$; it is not in the bibliography (only Wenger 2005 and 2007 are).
- [Shibing Chen, Mohammad Ghomi, Peng Wang, *The Cartan-Hadamard conjecture in dimension five*](https://arxiv.org/abs/2609.11005) (arXiv:2609.11005, 10 Sep 2026). This preprint proves the Euclidean Cartan–Hadamard inequality in dimension 5 and so overlaps with Corollary 1.2; it is not in the bibliography, which cites only the authors' later arXiv:2609.20517.

## Digests and expositions
- [Latent Seminar, *Cartan–Hadamard isoperimetry and sharp integral fillings*](https://lowrank.github.io/latent-seminar/OpenAI-Math/337-cartan-hadamard-isoperimetry) (7 October 2026). This exposition outlines both manuscripts' claimed proof mechanisms, including the hypersurface Sobolev estimate, confined profiles, equality rigidity and the CAT(0) variance argument, while explicitly disclaiming independent verification of the complete proofs. [family-level]

## News and blogs
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (audit report, 10 October 2026). The report lists family 337 among families whose headline includes a result from a manuscript outside the scope note's linked formalization, specifically identifying the generalized smooth isoperimetric comparison. [family-level]
