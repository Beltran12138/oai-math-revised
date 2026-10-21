# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Vojkan Jakšić, Yoram Last, *Extended States on the Bethe Lattice Revisited*](https://arxiv.org/abs/2610.11611) (arXiv:2610.11611, 8 Oct 2026). Gives a short proof of purely absolutely continuous spectrum on the Bethe lattice at weak disorder, and its Appendix B derives purity directly from the boundary-positivity assertion in equation (177) of this paper, leaving the finite-volume argument establishing that assertion unchanged.
- [Patrick Lopatto (listed contributor), *Mobility Edge for Sparse Complex Gaussian Matrices*](https://hexagonmath.org/abs/2610.00168v1) (hexagon:2610.00168v1, 12 Oct 2026). Claims a single mobility edge for the local limit of sparse complex Gaussian matrices (weighted Poisson–Galton–Watson trees) and cites both family papers in its introduction as recent lattice results. [AI-generated per source] [family-level]

## Expert comments and discussion
- None found.

## Formalization
- [Yao Xu (GitHub: cadamcat), *anderson-ac-lean4*](https://github.com/cadamcat/anderson-ac-lean4) (GitHub repository, Lean 4 v4.34.1 / Mathlib, builds on the OpenAI `OAI` library at commit adc7f12). An independent Lean 4 development whose README says it proves a statement matching Theorem 1.1, phrased for uniform disorder on [a,b] with b−a<δ, without `sorry` or added axioms, and "developed with AI assistance"; these claims are as stated by the README.
- [OpenAI math release, *Lean scope note for family 261* (mirror)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/261.md) (lean/docs/261.md). The family's linked formalization constructs the planar operator and identifies its almost-sure spectrum as $[-4-h,4+h]$, covering neither the planar pure-point claim nor this paper's higher-dimensional absolute-continuity claim. [family-level]

## Related prior literature mentioned by others
- [Vojkan Jakšić, Yoram Last, *Spectral Structure of Anderson Type Hamiltonians*](https://jaksic.xyz/papers_pdf/anderson.pdf) (Inventiones Mathematicae 141, 561–577, 2000). Jakšić and Last's 2026 follow-up invokes Corollaries 1.1.1 and 1.1.3 of this work, also cited in this paper's bibliography, to shorten the passage from boundary positivity to spectral purity.

## Possibly relevant literature (found by the agent, not checked)
- [Simon Becker, Izak Oltman, *Disorder on the hyperbolic square lattice I: Anderson delocalization and absolutely continuous spectrum*](https://arxiv.org/abs/2609.20798) (arXiv:2609.20798, 17 Sep 2026). Proves weak-disorder absolutely continuous spectrum, and the absence of singular spectrum on a set of positive measure, for the Anderson model on the product of Z^d with a hyperbolic square lattice, a non-tree setting relevant to the paper's comparison with earlier tree-only results.

## Digests and expositions
- [heyprof, *Anderson localisation: 2D vs. 3D (3D)*](https://www.heyprof.app/en/demo/anderson-lokalisierung) (interactive exposition, undated; accessed 2026-10-21). This family-specific visualization illustrates finite-lattice eigenstates and participation numbers, discusses finite-size limitations, and identifies the two manuscripts' spectral claims. [family-level]

## News and blogs
- [Azmat, *Anderson Localization OpenAI Proof: How Extended States Survive Weak Disorder in 3D*](https://binaryverseai.com/anderson-localization-openai-proof/) (Binary Verse AI, 2026-10-19). Outlines the claimed energy window, finite-volume certificate, adaptive potential revelations and spectral-averaging argument, distinguishing the spectral conclusion from a mobility-edge or diffusion theorem.
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (audit report, findings dated 2026-10-10). The report lists family 261 among cases where it classifies the formalized statements at audited commit fd4aeeb2 as narrower than the announced results. [family-level]
