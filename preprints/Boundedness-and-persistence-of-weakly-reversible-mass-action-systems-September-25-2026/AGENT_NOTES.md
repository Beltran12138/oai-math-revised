# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Michael Mislan, *Endotactic permanence and quantitative recovery with vanishing reverse rates*](https://hexagonmath.org/abs/2610.00321v1) (hexagon:2610.00321, October 2026). Cites this paper and the companion uniform-permanence paper and uses "the finite affine construction of OpenAI" to prove classwise permanence for ordinary endotactic networks with measurable rates in a fixed positive rate box; it also gives quantitative concentration bounds and recovery times for weakly reversible networks whose rates scale as powers of a small parameter. [AI-generated per source] [family-level]
- [Haoran Lv, Chengjin Ni, Manqin Wang, Shenli He, *Global Convergence of Detailed Balanced Mass Action Systems*](https://arxiv.org/abs/2610.30808) (arXiv:2610.30808, 22 October 2026). Cites this paper for the "barrier argument of OpenAI (2026)", which supplies global solutions and logarithmic confinement (its Theorem 3.1), and adds uniqueness of the equilibrium in each class and convergence of every positive trajectory for detailed balanced systems; its Section 5.4 says the entropy and equilibrium-identification arguments extend to complex balanced systems. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, Lean scope note *Classwise permanence for weakly reversible mass-action systems* (`lean/docs/149.md`)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/149.md) (openai/math release, October 2026). Lists this paper as the accompanying paper. Its scope is Theorem 1.1: global existence and an ε bound that depends on the network, the rates and the initial state; the comparator statement is in `lean/ComparatorChallenges/MassAction.lean`. [family-level]
- [Michael Mislan, *palomar-endotactic-permanence* (Lean repository)](https://github.com/mmislan/palomar-endotactic-permanence) (GitHub; registered as Palomar record PALOMAR-2026-10-09-000015 per hexagon:2610.00321, 2026). A Lean development of uniform permanence for endotactic networks with measurable rates; its README says the finite affine barrier construction is adapted from OpenAI's mass-action development. [AI-generated per source] [family-level]
- [BitMiracle AI Lab, *detailed-balance-gac* (Lean 4 repository)](https://github.com/BitMiracle-AI/detailed-balance-gac) (GitHub, tag v1.0; accompanies arXiv:2610.30808, October 2026). The README says the 71 modules in `lean/GAC/Persistence/` cover boundedness and persistence of weakly reversible systems and are "adapted from openai/math"; the paper reports about 7,900 of about 9,300 lines come from this adapted work and that the main results depend only on `propext`, `Classical.choice` and `Quot.sound`. [AI-generated per source]

## Related prior literature mentioned by others
- [Matthew D. Johnston, Casian Pantea, Pete Donnell, *A computational approach to persistence, permanence, and endotacticity of biochemical reaction systems*](https://arxiv.org/abs/1412.4662) (arXiv:1412.4662, 2014; [Journal of Mathematical Biology 72, 2016](https://researchportal.port.ac.uk/en/publications/a-computational-approach-to-persistence-permanence-and-endotactic/)). Cited by hexagon:2610.00321 as the source of the endotactic permanence conjecture (its Conjecture 1.3), which that follow-up proves using the affine construction from this family. [family-level]
- [Gheorghe Craciun, Abhishek Deshpande, *Endotactic networks and toric differential inclusions*](https://arxiv.org/abs/1906.08384) (arXiv:1906.08384, 2019). Cited by hexagon:2610.00321 alongside Boros–Hofbauer as related work on endotactic networks. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [David Angeli, Patrick De Leenheer, Eduardo Sontag, *A Petri Net approach to the study of persistence in chemical reaction networks*](https://arxiv.org/abs/q-bio/0608019) (arXiv:q-bio/0608019, 2006; Math. Biosci. 2007). Gives Petri-net (siphon) sufficient conditions for persistence, an earlier, structurally different route to the persistence half of Theorem 1.1.
- [Polly Y. Yu, Gheorghe Craciun, *Mathematical Analysis of Chemical Reaction Systems*](https://arxiv.org/abs/1805.10371) (arXiv:1805.10371, 2018). A survey stating the persistence and permanence conjectures for weakly reversible mass-action systems, which the introduction's history section discusses.
- [James D. Brunner and Gheorghe Craciun, *Robust persistence and permanence of polynomial and power law dynamical systems*](https://arxiv.org/abs/1705.06785) (arXiv:1705.06785, 2017). Its two-dimensional tropically endotactic permanence theorem provides a comparison for the family's all-dimensional weakly reversible claims and treatment of fixed versus time-dependent parameters. [family-level]
- [Carsten Wiuf, *A Proof of the Global Attractor Conjecture in a Special Case*](https://arxiv.org/abs/2609.24553) (arXiv:2609.24553, 21 September 2026). Proves convergence for complex balanced networks whose reachable siphons meet structural conditions, using a Chetaev function, which offers a comparison for the complex-balanced convergence deduced in this paper's Remark on that application.

## Digests and expositions
- [Latent Seminar, *Weakly reversible mass-action systems: persistence and permanence*](https://lowrank.github.io/latent-seminar/OpenAI-Math/149-mass-action-permanence) (6 October 2026). Explains both manuscripts' affine barriers, cut-flux estimates and scale iteration, explicitly distinguishing their quantifiers and the release's formalization scope without claiming complete proof verification. [family-level]

## News and blogs
- None found.
