# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Cody Haycraft, *A Kohn–Sham Hamiltonian for the OpenAI three-electron density: a note on representability beyond L^{3/2}+L^∞*](https://github.com/Hadron90/kohn-sham-representability) (GitHub working draft, status updated 2026-10-10). A response note that keeps the paper's exclusion in L^{3/2}+L^∞ and argues that a Friedrichs realisation of the candidate potential V = Δg/(2g) gives a Kohn–Sham Hamiltonian with ground-state density n (Theorem A). Per its README, a further theorem depends on an open estimate (Estimate 5.5), and the auxiliary Lean lemmas do not verify the analytic content.

## Expert comments and discussion
- [r/comp_chem participants, *OpenAI paper on Kohn-Sham DFT*](https://www.reddit.com/r/comp_chem/comments/1x0a9an/openai_paper_on_kohnsham_dft/) (Reddit discussion, accessed 2026-10-21). Community participants discuss the construction's scale and the distinction between density-functional theory and noninteracting representability, and link earlier literature; their specialist credentials are not established in the thread.

## Formalization
- None found.

## Related prior literature mentioned by others
- [Arno Schindlmayr and R. W. Godby, *Density-functional theory and the v-representability problem for model strongly correlated electron systems*](https://arxiv.org/abs/cond-mat/9709266) (arXiv:cond-mat/9709266, 1997-09-24). Linked in the r/comp_chem discussion as background on noninteracting representability; it studies Hubbard-type systems with occupation and orbital-overlap density variables, a different setting from the paper's continuum Coulomb molecule.

## Possibly relevant literature (found by the agent, not checked)
- [H. Englisch and R. Englisch, *Hohenberg-Kohn theorem and non-V-representable densities*](https://ideas.repec.org/a/eee/phsmap/v121y1983i1p253-268.html) (Physica A 121 (1983) 253–268, doi:10.1016/0378-4371(83)90254-6). Gives early examples of densities that are not ensemble-V-representable, bearing on the paper's discussion of prescribed densities that fail representability (Section 1.1), where the paper cites only Wagner et al.
- [P. E. Lammert, *Differentiability of Lieb functional in electronic density functional theory*](https://pure.psu.edu/en/publications/differentiability-of-lieb-functional-in-electronic-density-functi/) (Int. J. Quantum Chem. 107 (2007) 1943–1953). Analyses when directional derivatives of the Lieb functional are given by a potential, relevant to the paper's corollary excluding a local-potential first variation of the ensemble Hxc functional.
- [Nan Sheng, *Exact density-functional theory as parallel ensemble variational hierarchies: from Lieb's formulation to Kohn-Sham theory*](https://arxiv.org/abs/2603.23399) (arXiv:2603.23399, revised 2026-07-23). Distinguishes constrained-search feasibility from attainment by a representing potential, which is background for the paper's ensemble-representability obstruction and its consequence for local-potential first variations.
- [S. Kvaal, U. Ekström, A. M. Teale, T. Helgaker, *Differentiable but exact formulation of density-functional theory*](https://arxiv.org/abs/1312.3734) (arXiv:1312.3734, 2013; doi:10.1063/1.4867005). A Moreau–Yosida regularised Kohn–Sham formulation that avoids the noninteracting representability problem in a finite box, giving context for the scope of the paper's non-representability and first-variation statements.
- [T. C. Corso, *v-representability and Hohenberg-Kohn theorem for non-interacting Schrödinger operators with distributional potentials in the one-dimensional torus*](https://arxiv.org/abs/2501.13513) (arXiv:2501.13513, 2025). A positive noninteracting v-representability result on the 1D torus with distributional potentials, complementing the existence results the paper contrasts with its own (Sutter et al.; Corso's 1D interval paper).

## Digests and expositions
- [Gradient Damage, *QAOA Reaches the SK Optimum, Laughlin Spectral Gap Conjecture and 7 More*](https://gradientdamage.com/videos/qaoa-reaches-the-sk-optimum-laughlin-spectral-gap-conjecture-and-7/) (video compilation, 2026-10-15). The opening chapter (0:00–0:21) introduces the claimed Kohn–Sham representability counterexample as a visual illustration, and the accompanying page links the paper.

## News and blogs
- None found.
