# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [muralisubbarao2 (GitHub), *TR-M529-Ram-Coulomb-Ionization-Energies*](https://github.com/muralisubbarao2/Part-5-Improved-solutions-to-239-of-the-722-math-problems-posted-by-OpenAI/blob/main/TR-M529-Ram-Coulomb-Ionization-Energies.pdf) (GitHub repository "Improved solutions to 239 of the 722 math problems posted by OpenAI", undated). A technical report whose readable outline and links point to this preprint and its Lean files; the repository README calls its reports "a first draft prepared with the help of GPT 6 Astra" that has "not been verified by humans yet". [AI-generated per source]

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *lean/docs/263.md: The ionization and generalized ionization conjectures*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/263.md) (Lean scope notes, 6 October 2026). States that the formalization covers $I_m(Z)/m^{7/3}\to a_{\mathrm{TF}}$ as $m\to\infty$, $Z/m\to\infty$, with the iterated limits, excluding fixed-$m$ convergence and ground-state attainment; the comparator statement is `CoulombIonization.lean`. [family-level]
- [Yao Xu (cadamcat), *atomic-ionization-lean4*](https://github.com/cadamcat/atomic-ionization-lean4) (GitHub, Lean 4/Mathlib). A third-party Lean 4 development whose main statement includes this paper's Theorem 1.1 together with the companion's first-ionization and radius bounds; the README says it was "Developed with AI assistance" and reuses OpenAI's `CoulombIonization` library unchanged, with some proofs taking different routes. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [P. T. Nam, *The ionization problem in quantum mechanics*](https://arxiv.org/abs/2206.15393) (arXiv:2206.15393, 2022; in the EMS volume for E. H. Lieb's 90th birthday). A survey of the ionization problem, giving background on the ionization-energy questions that Theorem 1.1 addresses.
- [R. L. Frank, P. T. Nam, H. Van Den Bosch, *The ionization conjecture in Thomas-Fermi-Dirac-von Weizsäcker theory*](https://arxiv.org/abs/1606.07355) (arXiv:1606.07355; Comm. Pure Appl. Math.). Obtains screened-potential bounds by comparison with Thomas–Fermi theory in TFDW, analogous to the outward Thomas–Fermi comparisons used here for Theorem 1.2 (deficit at a prescribed price).
- [B.-G. Englert, *Thomas-Fermi equation revisited: A variation on a theme by Majorana*](https://arxiv.org/abs/2603.29482) (arXiv:2603.29482, 2026). Treats the Thomas–Fermi solution for weakly ionized atoms and related atomic quantities, which concerns the weak-ionization Thomas–Fermi law that defines $a_{\mathrm{TF}}$ in (1.2).

## Digests and expositions
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*](https://arxiv.org/html/2610.17090v1) (arXiv:2610.17090, October 2026). Section 9.2.2 covers family 263, centered on the uniform excess-charge paper, and describes this paper as one of two formalized Thomas–Fermi asymptotic companions sharing the observation-conditioning instrument. [family-level]
- [Latent Seminar, *Coulomb ionization: excess charge, energy costs, and outer radii*](https://lowrank.github.io/latent-seminar/OpenAI-Math/263-coulomb-ionization-energies-radii) (7 October 2026). Explains all three manuscripts through conditional screening, priced-sector energy comparisons and expected exterior mass, explicitly limiting its review to statements and selected proof mechanisms. [family-level]
- [ChatGPT Astra, prepared at the request of Hal Tasaki, *Mathematical physics in the OpenAI math release*](https://haltasaki.github.io/writings/pdf/OpenAI_Mathematical_Physics_Catalogue_2026-10-07.pdf) (research catalogue, 7 October 2026). Entry 1.17 summarizes this paper's claim and records "Main Lean statement listed"; the document says it is not an independent proof audit. [AI-generated per source]
- [Gradient Damage, *Spacetime Penrose Inequality, Strong Cosmic Censorship Near Kerr and 8 More*](https://gradientdamage.com/videos/spacetime-penrose-inequality-strong-cosmic-censorship-near-kerr-and-8/) (video compilation, 15 October 2026). Includes an ionization-conjecture chapter at 0:43 and a family summary covering the excess-charge, energy and radius claims, presented as illustrations rather than proofs. [family-level]

## News and blogs
- None found.
