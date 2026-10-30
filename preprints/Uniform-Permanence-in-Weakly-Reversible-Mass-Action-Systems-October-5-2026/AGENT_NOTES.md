# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Michael Mislan, *Endotactic permanence and quantitative recovery with vanishing reverse rates*](https://hexagonmath.org/abs/2610.00321v1) (hexagon:2610.00321, October 2026). Cites this paper and its companion and uses "the finite affine construction of OpenAI" to prove classwise permanence for ordinary endotactic networks with measurable rates in a fixed positive rate box; it also gives quantitative concentration bounds and recovery times for weakly reversible networks whose rates scale as powers of a small parameter. [AI-generated per source] [family-level]
- [Haoran Lv, Chengjin Ni, Manqin Wang and Shenli He, *Global Convergence of Detailed Balanced Mass Action Systems*](https://arxiv.org/abs/2610.30808) (arXiv:2610.30808, 2026-10-22). Uses the companion September boundedness-and-persistence paper's affine barrier construction to establish convergence to the unique positive equilibrium in each positive stoichiometric class under detailed balance, with a bounded-speed descent argument replacing LaSalle's invariance principle. [AI-generated per source] [family-level]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, Lean scope note *Classwise permanence for weakly reversible mass-action systems* (`lean/docs/149.md`)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/149.md) (openai/math release, October 2026). The scope note lists only the companion paper as accompanying and formalizes its pointwise statement: global existence and an ε bound depending on the network, the rates and the initial state. The classwise uniformity of this paper's Theorem 1.1 is not in the stated scope. [family-level]
- [Michael Mislan, *palomar-endotactic-permanence* (Lean repository)](https://github.com/mmislan/palomar-endotactic-permanence) (GitHub; registered as Palomar record PALOMAR-2026-10-09-000015 per hexagon:2610.00321, 2026). A Lean development of uniform permanence for endotactic networks with measurable rates; its README says the finite affine barrier construction is adapted from OpenAI's mass-action development. [AI-generated per source] [family-level]
- [Michael Mislan, *palomar-quantitative-permanence* (Lean repository)](https://github.com/mmislan/palomar-quantitative-permanence) (GitHub; Palomar record PALOMAR-2026-10-11-000020, 2026-10-11). Lean statements for quantitative permanence and recovery bounds with vanishing reverse rates; its README says the general construction builds on an attributed affine permanence development from this preprint. [AI-generated per source]
- [BitMiracle AI Lab, *detailed-balance-gac*](https://github.com/BitMiracle-AI/detailed-balance-gac) (Lean 4 repository accompanying arXiv:2610.30808, October 2026). Adapts 71 modules from the release's weakly reversible boundedness-and-persistence development and adds a detailed-balance convergence theorem, with paper-to-code correspondence and formal coverage limits documented in the README. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- [Matthew D. Johnston, Casian Pantea, Pete Donnell, *A computational approach to persistence, permanence, and endotacticity of biochemical reaction systems*](https://arxiv.org/abs/1412.4662) (arXiv:1412.4662, 2014; [Journal of Mathematical Biology 72, 2016](https://researchportal.port.ac.uk/en/publications/a-computational-approach-to-persistence-permanence-and-endotactic/)). Cited by hexagon:2610.00321 as the source of the endotactic permanence conjecture (its Conjecture 1.3), which that follow-up proves using the affine construction from this family. [family-level]
- [Gheorghe Craciun, Abhishek Deshpande, *Endotactic networks and toric differential inclusions*](https://arxiv.org/abs/1906.08384) (arXiv:1906.08384, 2019). Cited by hexagon:2610.00321 alongside Boros–Hofbauer as related work on endotactic networks. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [Polly Y. Yu, Gheorghe Craciun, *Mathematical Analysis of Chemical Reaction Systems*](https://arxiv.org/abs/1805.10371) (arXiv:1805.10371, 2018). This survey states the Permanence Conjecture as a globally attracting compact set in every stoichiometric compatibility class, the formulation that Theorem 1.1 addresses.
- [James D. Brunner and Gheorghe Craciun, *Robust persistence and permanence of polynomial and power law dynamical systems*](https://arxiv.org/abs/1705.06785) (arXiv:1705.06785, 2017). Its two-dimensional tropically endotactic permanence theorem provides a comparison for the family's all-dimensional weakly reversible claims and treatment of fixed versus time-dependent parameters. [family-level]

## Digests and expositions
- [Latent Seminar, *Weakly reversible mass-action systems: persistence and permanence*](https://lowrank.github.io/latent-seminar/OpenAI-Math/149-mass-action-permanence) (6 October 2026). Explains both manuscripts' affine barriers, cut-flux estimates and scale iteration, explicitly distinguishing their quantifiers and the release's formalization scope without claiming complete proof verification. [family-level]
- [RMJ / VideoToBlog, *Uniformní permanence ve slabě reverzibilních reakčních systémech: jedna bezpečná oblast pro všechny kladné začátky*](https://rmj.videotoblog.ai/uniformni-permanence-slaba-reverzibilita) (undated). This Czech exposition explains the October manuscript's common absorbing set, initial-state-dependent entry times and proof outline using a one-species reversible example.

## News and blogs
- None found.
