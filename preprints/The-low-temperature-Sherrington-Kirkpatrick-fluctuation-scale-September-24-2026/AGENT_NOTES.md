# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [P. M. Aronow and Patrick Lopatto, *Lower and Upper Bounds for Glauber Dynamics from Typical States of the Low-Temperature Sherrington–Kirkpatrick Model*](https://hexagonmath.org/abs/2610.00402v1) (hexagon:2610.00402v1, 2026-10-20). Restates this paper's main theorem as its Theorem 1.6, reproves the deduction from the positive-logarithmic-moment bound (its Section 20), and combines the variance exponent with a variance–bias inequality to get a mean-bias lower bound of order $n^{-5/6-\varepsilon}$ (its Corollary 1.7). [AI-generated per source]
- [P. M. Aronow and Patrick Lopatto, *An $N^{-7/10}$ Bound for the Finite-Size Bias of the Sherrington–Kirkpatrick Free Energy*](https://hexagonmath.org/abs/2610.00177v1) (hexagon:2610.00177v1, 2026-10-12). Section 1.6 conditionally derives a mean-bias lower bound of order $N^{-5/6-\varepsilon}$ from this paper's variance exponent and compares consequences of the limiting-law companion. [AI-generated per source] [cites earlier version] [family-level]

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, `lean/OAI/Probability/SKFluctuations` in the release repository](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/Probability/SKFluctuations) (openai/math, commit fd4aeeb). The release's Lean development for this result, whose theorem `main_of_positiveLaplaceWindow` deduces the standard-deviation, variance and typical-fluctuation exponents under the explicit hypothesis `PositiveLaplaceWindow` (the two-sided bound of this paper's Proposition 7.5, per hexagon:2610.00402v1, Section 1.5). [AI-generated per source] [family-level]
- [P. M. Aronow and Patrick Lopatto, *fluctuations-palomar*](https://github.com/pmaronow/fluctuations-palomar) (Lean package accompanying hexagon:2610.00402v1, 2026-10-20). Formalizes this paper's standard-deviation, variance and typical-magnitude exponents with the Proposition 7.5 hypothesis proved internally; the README reports an axiom audit passed at commit 2fd7036, with a Comparator replay for one other result still pending. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- [T. Aspelmeier, A. Billoire, E. Marinari, M. A. Moore, *Finite size corrections in the Sherrington-Kirkpatrick model*](https://arxiv.org/abs/0711.3445) (J. Phys. A 41 (2008) 324008). Cited in hexagon:2610.00402v1, Section 1.4, as a physics argument that about $n^{1/6}$ RSB levels are resolved, giving variance of order $n^{1/3}$; not in this paper's bibliography.
- [Elizabeth Collins-Woodfin and Han Gia Le, *Free energy fluctuations in SK and related spin glass models: A literature survey*](https://arxiv.org/abs/2510.26960v3) (arXiv:2510.26960v3, 2025-11-07). Aronow and Lopatto recommend this survey in Section 1.4 of hexagon:2610.00402v1 for background on fluctuation regimes, spin spaces and external fields. [family-level]
- [Partha S. Dey and Taegu Kang, *Fluctuations for the Sherrington–Kirkpatrick spin glass model near the critical temperature*](https://arxiv.org/abs/2603.05636v1) (arXiv:2603.05636, 2026-03-05). Near-critical variance asymptotics and a Gaussian CLT for $\beta_N\uparrow1$, cited in hexagon:2610.00402v1 next to this paper's fixed-$\beta>1$ result; not in this paper's bibliography.
- [Yan Ru Pei, *Upper deviations of the Sherrington-Kirkpatrick free energy: the fifth-order law and the onset of constrained Parisi measures*](https://arxiv.org/abs/2610.06480v2) (arXiv:2610.06480, 2026-10-05). Derives the fifth-order constrained-Parisi cost behind the Parisi–Rizzo upper-deviation rate that this paper's history section discusses; cited in hexagon:2610.00402v1, Section 1.4.
- [Jinho Baik and Ji Oon Lee, *Fluctuations of the free energy of the spherical Sherrington-Kirkpatrick model*](https://arxiv.org/abs/1505.07349) (arXiv:1505.07349v5, 2015-07-05). Section 1.4 of hexagon:2610.00402v1 contrasts its low-temperature spherical-model Tracy–Widom law and $n^{1/3}$ total-free-energy scale with the Ising family's $n^{1/6}$ scale. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [T. Aspelmeier, *Free energy fluctuations and chaos in the Sherrington-Kirkpatrick model*](https://arxiv.org/abs/0712.3586) (Phys. Rev. Lett. 100 (2008) 117205). A replica argument linking free-energy fluctuations to bond chaos that bounds the fluctuation exponent by 1/4, a physics bound that this paper's $n^{1/6+o(1)}$ theorem is consistent with; not in this paper's bibliography.

## Digests and expositions
- None found.

## News and blogs
- None found.
