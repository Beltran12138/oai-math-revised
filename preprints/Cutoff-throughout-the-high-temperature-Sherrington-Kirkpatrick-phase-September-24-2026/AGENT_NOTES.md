# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- None found.

## Comments and discussion
- [Hang Du, Brice Huang, Sidhanth Mohanty, Amit Rajaraman, *Sampling from the Sherrington-Kirkpatrick Model up to Criticality*](https://arxiv.org/abs/2610.17717) (arXiv:2610.17717, 13 Oct 2026). Section 1.2 ("Concurrent work by OpenAI") lists the worst-case-initialization cutoff for β < 1 among the OpenAI results concurrent with their simulated-annealing sampler.
- [Zhe Hou, Jingcheng Liu, Yixiao Yu, *Simulated annealing and Weak Poincaré inequalities with inverse-polynomial accuracy for the Sherrington-Kirkpatrick model*](https://arxiv.org/abs/2610.09882) (arXiv:2610.09882, 7 Oct 2026). Section 1.3 ("Concurrent work") notes the worst-case total-variation cutoff on the n log n scale for 0 ≤ β < 1 reported in this OpenAI preprint.
- [Alina Harbuzova, Saba Lepsveridze, Mahbod Majid, Ankur Moitra, *Color Coding for the Sherrington–Kirkpatrick Model*](https://arxiv.org/abs/2610.10443) (arXiv:2610.10443, 7 Oct 2026). Its concurrent-work passage cites this paper and the spectral-gap companion for worst-start O(n log n) mixing at every β < 1 with high probability over the disorder, and states that the authors' deterministic counting theorem does not establish a spectral gap or rapid mixing.
- [Carlos Toledo / cert-machine, *OpenAI math finite-certificate audit, F-426*](https://raw.githubusercontent.com/carlostoledo1891/cert-machine/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-finite.json) (cert-machine, accessed 2026-10-30). Reports independent exact recomputation of the quadrature enclosures, error budget and interval bounds in the appendix’s scalar certificate for the $\beta<1/2$ argument, with the analytic steps and full-temperature cutoff theorem outside this computation’s scope.

## Formalization
- [OpenAI, *Family 227 Lean scope*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/227.md) (lean/docs/227.md, 2026-10-06). The formalized statement is ratio cutoff, t_mix(ε)/t_mix(1−ε) → 1 in probability, for discrete heat-bath dynamics at $0\le\beta<1/2$ (comparator `SKRatio.lean`); the full range β < 1, the explicit cutoff location and the continuous-time statement are not formalized. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [David A. Levin, Malwina J. Luczak, Yuval Peres, *Glauber dynamics for the mean-field Ising model: cut-off, critical power law, and metastability*](https://arxiv.org/abs/0712.0790) (arXiv:0712.0790, 2007). Proves Glauber cutoff throughout the high-temperature phase of the Curie–Weiss model, the deterministic-coupling analogue of Theorem 1.1's cutoff for all β < 1.

## Digests and expositions
- [Latent Seminar, *SK dynamics across the temperature transition*](https://lowrank.github.io/latent-seminar/OpenAI-Math/227-sk-dynamics) (2026-10-06). Explains the eight companions and selected proof mechanisms without independently verifying their proofs. [family-level]

## News and blogs
- None found.
