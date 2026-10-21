# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *The critical dimension for the one-phase Bernoulli problem — Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/367.md) (OpenAI Math Release Lean docs, 2026-10-06). The release's own Lean development covers only the existence half of Theorem 1.1 (a nonflat one-homogeneous global minimizer in $\mathbb R^7$); flatness for $d\le6$ and the regularity and singular-set consequences are explicitly outside its scope. [family-level]
- [William M. Feldman, *one-phase-critical-dim: Lean 4 / Mathlib proof that one-homogeneous minimizers of the one-phase Bernoulli problem are flat in dimensions at most six*](https://github.com/willmfeldman/one-phase-critical-dim) (GitHub repository; Palomar entry [PALOMAR-2026-10-14-000010 v1](https://data.palomar-registry.org/entries/PALOMAR-2026-10-14-000010-v1.json), 2026-10-14). Independent formalization of the flatness half ($1\le d\le6$) of Theorem 1.1 following the paper's certificate method, with new certificates for $d=3,4$; the README reports no `sorry`, says the code was written by AI coding agents under the author's direction, and notes that no machine-checked bridge yet links it to the release's `GlobalMinimizer` and that the singular-set corollary is not formalized. [AI-generated per source]

## Related prior literature mentioned by others
- [D. Kriventsov and G. S. Weiss, *Rectifiability, finite Hausdorff measure, and compactness for non-minimizing Bernoulli free boundaries*](https://arxiv.org/abs/2306.10131) (arXiv:2306.10131, 2023). Cited in the README of the independent Lean formalization above as part of the background used there; not in the paper's bibliography.
- [F. Abedin, W. M. Feldman and K. Stinson, *Variational properties of Perron's extremal solutions in the Bernoulli one-phase problem*](https://arxiv.org/abs/2609.14981) (arXiv:2609.14981, 2026-09-14). Cited in the README of the independent Lean formalization above, one of whose pinned dependency libraries is a Perron/variational Bernoulli package by the same author.

## Possibly relevant literature (found by the agent, not checked)
- [N. Edelen and M. Engelstein, *Quantitative stratification for some free-boundary problems*](https://arxiv.org/abs/1702.04325v3) (arXiv:1702.04325, Trans. Amer. Math. Soc. 2019). Proves rectifiability and measure bounds for the singular set of Alt–Caffarelli minimizers, which bears on the singular-set statements of Corollary 1.2 (dimension bound $n-7$, local finiteness for $n=7$).
- [Giorgio Tortone and Bozhidar Velichkov, *Vectorial Bernoulli Problems and Free Boundary Systems*](https://link.springer.com/article/10.1007/s44007-026-00195-z) (La Matematica 5, article 16, 4 February 2026). Its Theorem 1.1 summarizes the dependence of one-phase singular-set bounds on the critical dimension, providing background for Corollary 1.2 and its specialization to critical dimension seven.
- [C. Hines, J. Kolesar and P. McGrath, *New Homogeneous Solutions for the One-Phase Free Boundary Problem*](https://arxiv.org/abs/2509.09409) (arXiv:2509.09409, 2025-09-11). Constructs new nonflat one-homogeneous solutions (including an infinite family in dimension four); Theorem 1.1 would imply none of these is a global minimizer in dimensions at most six.

## Digests and expositions
- [Expository note in the one-phase-critical-dim repository, *The critical dimension of the one-phase Bernoulli problem: an expository account*](https://github.com/willmfeldman/one-phase-critical-dim/blob/main/expository/note.typ) (Typst source with compiled `note.pdf`, October 2026). Explains the structure of the flatness proof for $d\le6$ (reduction to smooth links, suspension from dimension five to six, stability inequality, finite algebraic certificate); the README says the expository notes were only partly reviewed by the author. [AI-generated per source]
- [Latent Seminar, *The critical dimension of the one-phase Bernoulli problem*](https://lowrank.github.io/latent-seminar/OpenAI-Math/367-bernoulli-critical-dimension) (6 October 2026). Outlines the spherical Hessian, stability, exact tensor certificate and cutoff arguments, and states that it does not independently verify the complete proof or run the certificate engines. [family-level]

## News and blogs
- None found.
