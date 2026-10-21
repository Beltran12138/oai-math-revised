# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Zixuan He, *The active entropy photon-number inequality: exact minima, energy budgets and input rigidity*](https://zenodo.org/records/23352232) (Zenodo preprint, doi:10.5281/zenodo.23352232, v1.3, 13 October 2026). Treats the amplifier-type ("active") entropy photon-number inequality for independent multimode inputs with arbitrary internal correlations, with constrained output-entropy minima for thermal amplifiers and stability bounds for near-optimal inputs; the [v1.2 PDF](https://zenodo.org/records/23228543) cites "OpenAI" and links to the openai/math repository at commit adc7f12.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, Lean scope note for family 273](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/273.md) (lean/docs/273.md, 6 October 2026). Says the Lean formalization covers the two-input inequality (Theorem 1.1) for finite-energy inputs in any finite positive number of modes, allowing internal entanglement, and excludes the thermal-attenuator minimum-output-entropy and broadcast-capacity consequences.
- [OpenAI, *Inequality.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/InformationTheory/PhotonNumber/Inequality.lean) (openai/math, commit adc7f12). Lean source containing the theorem `entropy_photon_number_inequality`, which states the beam-splitter inequality $\eta g^{-1}(S(\rho_A)/n)+(1-\eta)g^{-1}(S(\rho_B)/n)\le g^{-1}(S(\rho_C)/n)$.

## Related prior literature mentioned by others
- [Giacomo De Palma, Andrea Mari and Vittorio Giovannetti, *A generalization of the Entropy Power Inequality to Bosonic Quantum Systems*](https://arxiv.org/abs/1402.0404) (arXiv:1402.0404; Nature Photonics 8, 958–964, 2014). The [QIQCOP Zoo's discussion of the OpenAI claim](https://qiqc-op.com/problem/op_ba39e7a80122b256/) identifies this paper's exponential quantum entropy power inequality as a weaker predecessor to the claimed entropy photon-number inequality.
- [Giacomo De Palma, Dario Trevisan and Vittorio Giovannetti, *Gaussian states minimize the output entropy of one-mode quantum Gaussian channels*](https://arxiv.org/abs/1610.09970) (arXiv:1610.09970; Physical Review Letters 118, 160503, 2017). The [QIQCOP Zoo's discussion of the OpenAI claim](https://qiqc-op.com/problem/op_ba39e7a80122b256/) cites Theorem 4 as the sharp one-mode thermal-environment case preceding the manuscript's arbitrary two-input, multimode claim.

## Possibly relevant literature (found by the agent, not checked)
- [S. Guha, J. H. Shapiro, B. I. Erkmen, *Capacity of the Bosonic Wiretap Channel and the Entropy Photon-Number Inequality*](https://arxiv.org/abs/0801.0841) (arXiv:0801.0841, January 2008). Derives the wiretap-channel capacity, and with it the quantum capacity of the lossy bosonic channel, from a minimum output entropy conjecture that follows from the EPnI; the paper discusses only the attenuator and broadcast consequences.
- [M. M. Wilde, P. Hayden, S. Guha, *Quantum trade-off coding for bosonic communication*](https://arxiv.org/abs/1105.0119) (Phys. Rev. A 86, 062306 (2012); arXiv:1105.0119). Its arXiv comments say the optimality of its pure-loss trade-off region is proven if the EPnI holds, a further channel consequence of Theorem 1.1 beyond the paper's stated corollaries.
- [H. Qi, M. M. Wilde, S. Guha, *On the minimum output entropy of single-mode phase-insensitive Gaussian channels*](https://arxiv.org/abs/1607.05262) (arXiv:1607.05262, 2016/2017). Notes that a multimode version of the De Palma–Trevisan–Giovannetti constrained minimum-output-entropy result would give an important special case of the EPnI, which relates to the paper's Corollary 1.2 (constrained minimum for identical thermal attenuators).
- [G. De Palma, D. Trevisan, V. Giovannetti, L. Ambrosio, *Gaussian optimizers for entropic inequalities in quantum information*](https://arxiv.org/abs/1803.02360) (J. Math. Phys. 59, 081101 (2018); arXiv:1803.02360). A survey of the quantum Gaussian optimizer conjectures, including quantum counterparts of the entropy power inequality, giving background for the status of the conjecture summarised in the paper's introduction.

## Digests and expositions
- [Gradient Damage, *Spacetime Penrose Inequality, Strong Cosmic Censorship Near Kerr and 8 More*](https://gradientdamage.com/videos/spacetime-penrose-inequality-strong-cosmic-censorship-near-kerr-and-8/) (video compilation, 15 October 2026). The chapter beginning at 2:49 introduces the entropy photon-number inequality through beam-splitter mixing, with the accompanying page attributing the claim to OpenAI and distinguishing the animations from proofs. [family-level]

## News and blogs
- None found.
