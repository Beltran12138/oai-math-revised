# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [P. M. Aronow and Patrick Lopatto, *Lower and Upper Bounds for Glauber Dynamics from Typical States of the Low-Temperature Sherrington–Kirkpatrick Model*](https://hexagonmath.org/abs/2610.00402v1) (hexagon:2610.00402v1, 2026-10-20). Cites this paper's Theorems 1.1–1.2 (variance prefactor $a_2(\beta)>0$ and limiting law), notes these would sharpen its mean-bias lower bound to $c_\beta n^{-5/6}$, and states that it does not use this paper. [AI-generated per source]
- [P. M. Aronow and Patrick Lopatto, *An $N^{-7/10}$ Bound for the Finite-Size Bias of the Sherrington–Kirkpatrick Free Energy*](https://hexagonmath.org/abs/2610.00177v1) (hexagon:2610.00177v1, 2026-10-12). Section 1.6 derives conditional mean-bias bounds from both manuscripts of this family, including an $N^{-5/6}$ lower bound from the positive variance prefactor and an upper bound from this paper's uncentered comparison. [AI-generated per source] [cites earlier version] [family-level]
- [Hang Du, Shuyang Gong, Brice Huang, Zhangsong Li, *Free energy fluctuations of symmetric perceptron models up to and including criticality*](https://arxiv.org/html/2610.31736v1) (arXiv:2610.31736v1, 2026-10-22). Section 1.3 lists "fluctuations of order $N^{1/6}$ at low temperature" for the SK free energy as now known, citing Chatterjee 2009 and this paper (reference [Ope26c]); the paper's own results concern perceptron models and do not use this result.

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *SKFluctuations/EventuallyNatPos.lean*](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/Probability/SKFluctuations/EventuallyNatPos.lean) (OpenAI math release, 2026). The companion-scale theorem `main_of_positiveLaplaceWindow` explicitly assumes `PositiveLaplaceWindow`; its conclusion concerns fluctuation exponents, not this paper's variance prefactor or limiting law. [AI-generated per source] [family-level]
- [P. M. Aronow and Patrick Lopatto, *fluctuations-palomar*](https://github.com/pmaronow/fluctuations-palomar) (Lean package accompanying hexagon:2610.00402v1, 2026-10-20). Formalizes the companion paper's exponent $\mathrm{sd}(F_n)=n^{1/6+o(1)}$, which this paper uses as an input, with the positive-Laplace-window input proved internally; it does not formalize the limiting law or the $n^{1/3}$ variance prefactor. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- [T. Aspelmeier, A. Billoire, E. Marinari, M. A. Moore, *Finite size corrections in the Sherrington-Kirkpatrick model*](https://arxiv.org/abs/0711.3445) (J. Phys. A 41 (2008) 324008). Cited in hexagon:2610.00402v1, Section 1.4, as a physics derivation of variance of order $n^{1/3}$ for the total free energy, the scale whose prefactor this paper proves positive; not in this paper's bibliography.
- [Elizabeth Collins-Woodfin and Han Gia Le, *Free energy fluctuations in SK and related spin glass models: A literature survey*](https://arxiv.org/abs/2510.26960v3) (arXiv:2510.26960v3, 2025-11-07). Aronow and Lopatto recommend this survey in Section 1.4 of hexagon:2610.00402v1 for background on fluctuation regimes, spin spaces and external fields. [family-level]
- [Partha S. Dey and Taegu Kang, *Fluctuations for the Sherrington–Kirkpatrick spin glass model near the critical temperature*](https://arxiv.org/abs/2603.05636v1) (arXiv:2603.05636, 2026-03-05). Near-critical variance asymptotics and a Gaussian limit for $\beta_N\uparrow1$, a regime this paper's fixed-$\beta$ law does not cover; cited in hexagon:2610.00402v1, and different from the Dey–Kang ferromagnetic paper in this paper's bibliography.
- [Yan Ru Pei, *Upper deviations of the Sherrington-Kirkpatrick free energy: the fifth-order law and the onset of constrained Parisi measures*](https://arxiv.org/abs/2610.06480v2) (arXiv:2610.06480, 2026-10-05). Treats the fifth-order upper-deviation law behind the Parisi–Rizzo tail-matching heuristic, which this paper's introduction contrasts with its limiting law; cited in hexagon:2610.00402v1.
- [Jinho Baik and Ji Oon Lee, *Fluctuations of the free energy of the spherical Sherrington-Kirkpatrick model*](https://arxiv.org/abs/1505.07349) (arXiv:1505.07349v5, 2015-07-05). Section 1.4 of hexagon:2610.00402v1 contrasts its low-temperature spherical-model Tracy–Widom law and $n^{1/3}$ total-free-energy scale with the Ising family's $n^{1/6}$ scale. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [T. Aspelmeier, *Free energy fluctuations and chaos in the Sherrington-Kirkpatrick model*](https://arxiv.org/abs/0712.3586) (Phys. Rev. Lett. 100 (2008) 117205). Links free-energy sample-to-sample fluctuations to bond chaos, which bears on this paper's corollary deriving upper disorder-chaos scales from the variance asymptotic; not in this paper's bibliography.
- [Cécile Monthus and Thomas Garel, *Matching between typical fluctuations and large deviations in disordered systems: application to the statistics of the ground state energy in the SK spin-glass model*](https://arxiv.org/abs/0912.2875) (J. Stat. Mech. (2010) P02023). Relates the tail exponents of the rescaled SK ground-state energy law to the fluctuation exponent, which bears on this paper's introduction contrasting tail matching with a limiting law and on the exponential moment of $\nu_\beta$, though at zero rather than fixed positive temperature; not in this paper's bibliography.

## Digests and expositions
- None found.

## News and blogs
- [Hong A-reum, *OpenAI floods math with 719 AI papers; Korea hails speed, flags clarity strain*](https://biz.chosun.com/en/en-science/2026/10/12/ZF43Y2FTRZH4BIKNWISTHSGJMU/?outputType=amp) (ChosunBiz, 2026-10-12). Reports Ji-woon Lee's account that OpenAI's low-temperature SK fluctuation claim develops an approach that first appeared in July 2026, placing this family's claim in the context of recent human research. [family-level]
