# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Kenta Kitamura, *Next-order Riesz and logarithmic energy on spheres of dimensions 2, 8 and 24*](https://github.com/KitaKen1/riesz-energy-spheres) (GitHub repository with manuscript and Lean sources, commits 2026-10-14 to 2026-10-19). Lists Conjecture 4 of Brauchart–Hardin–Saff as solved for d = 2, 8, 24, which overlaps this paper's Corollary 1.3 at d = 2; the manuscript relies on a "sharp triangular Gaussian minorant theorem", has no bibliography and does not cite this paper, and the README self-reports its Lean checks.
- [Xavier Callens, *The Sandier-Serfaty triangular-lattice conjecture: an independent reproduction of a claimed finite certificate, an adversarial audit of the claimed reduction, and a Lean statement (no proof of the conjecture is claimed)*](https://zenodo.org/records/23653827) (Zenodo 10.5281/zenodo.23653827, 2026-10-26). Reports reproducing all 22 printed certificate pairs and auditing Sections 2–5, while identifying unchecked analytic/reference dependencies and expressly declining to prove, verify or refute the manuscript’s claim. Its Lean part gives statements in the manuscript and original Sandier–Serfaty normalizations, ten checked non-degeneracy lemmas and arithmetic checks on printed certificate data, leaving the conjecture, puncture-limit existence and normalization equivalence unproved. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [Yuhao Lei, *Triangular-Lattice-Coulomb-Lean*](https://github.com/yuhaolei-ctrl/Triangular-Lattice-Coulomb-Lean) (GitHub repository, created 2026-10-06, last push 2026-10-07). Work-in-progress Lean 4 statement of Theorem 1.1 of Lei's own manuscript *The triangular lattice minimizes the two-dimensional Coulomb renormalized energy* (cited without a link, v2), the same type of inequality W(E) ≥ W(E_Λ) as this paper's Theorem 1.1 for discs or squares and every cutoff width; its status file marks the statement as under review and most proof layers as not started, and `formalization.yaml` credits Claude Code with assisting the Lean work and the manuscript's mathematics to the human author.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Stefan Steinerberger, *A set of points on the sphere with small Riesz energy*](https://arxiv.org/abs/2607.08049) (arXiv:2607.08049, July 2026). Constructs explicit point sets on the 2-sphere from pieces of the hexagonal lattice whose Riesz s = 2 energy constant matches the Brauchart–Hardin–Saff conjectured value; this is the Riesz analogue of Corollary 1.3, which by its own statement gives an asymptotic value and does not construct point sets.

## Digests and expositions
- [Latent Seminar, *Triangular lattices: universal energies, Fourier packing, and Coulomb renormalization*](https://lowrank.github.io/latent-seminar/OpenAI-Math/090-triangular-lattice-optimality) (exposition, 2026-10-06). Explains the four manuscripts' distinct claims and proof mechanisms, explicitly limiting its review to statements, introductions, and selected mechanisms rather than complete proof verification. [family-level]

## News and blogs
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (AI-assisted audit at fd4aeeb2, 2026-10-10). Reports certification of the finite computation in Proposition comp:finite-soundness (F-180), with the stated scope restricted to a finite component.
