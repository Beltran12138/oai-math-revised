# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Qiang Gao, *Improving the lower bound on the Laughlin gap: An SDP search*](https://arxiv.org/abs/2610.12700) (arXiv:2610.12700, 2026-10-08). Keeps this paper's architecture, refines its comparison estimates and optimizes its auxiliary operators by an SDP search certified in exact rational arithmetic, reporting $H_Q^2\ge\gamma H_Q$ for every $\gamma<0.2190037845063196\ldots$ at sufficiently large flux and hence a spherical Laughlin gap of at least $1/5$; the paper says the proof and search were completed by Claude Opus 5.5 under the author's direction. [AI-generated per source]
- [Qiang Gao and Taige Wang, *Thermodynamic-limit bootstrap: Solving fractional quantum Hall ground states*](https://arxiv.org/html/2610.21317v1) (arXiv:2610.21317, 2026-10-15). Cites this paper's Fock-space positivity and rotation averaging as antecedents to a finite-orbital-window bootstrap for thermodynamic ground-state energies and correlations.
- [Xin Shen (curator), *The Bosonic Laughlin Spectral Gap: A Candidate Proof*](https://github.com/Shencongli/bosonic-laughlin-spectral-gap) (GitHub, v0.1, 7 October 2026). Adapts this paper's Fock-space comparison strategy to the bosonic V0 model and claims $H_Q^2\ge H_Q/3$ for $Q\ge3088$; the repository states that independent review remains open. [AI-generated per source]
- [GitHub user Yuchenian, *vortexable-laughlin-gap*](https://github.com/Yuchenian/vortexable-laughlin-gap) (GitHub repository, 2026). Self-described AI-assisted research draft that transfers a reference Laughlin spectral inequality to changed vortexable one-particle subspaces, taking Gao's refinement of this paper (arXiv:2610.12700) as its input. [AI-generated per source]

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *Uniform Laughlin gap and stability under bounded scalar disorder: Lean scope notes*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/269.md) (OpenAI Math Release, lean/docs/269.md, 2026). Describes Lean statements for the $1/100$ finite spherical bound, the Fock-space inequality $H_Q^2\ge\gamma H_Q$ for $\gamma<\gamma_*$, the $1/25$ gap inequality and the planar endpoint inequality, with links to the comparator files; stability under projected one-body potentials is explicitly excluded. [family-level]
- [OpenAI, Lean development `OAI/Analysis/LaughlinFock`](https://github.com/openai/math/tree/main/lean/OAI/Analysis/LaughlinFock) (openai/math repository). The release's Lean sources for the Fock-space inequality, including the certificate-row files; Gao's arXiv:2610.12700 cites this directory as the formalization of the original constant.

## Related prior literature mentioned by others
- [Nicolas Rougerie, *On the Laughlin function and its perturbations*](https://arxiv.org/abs/1906.11656) (arXiv:1906.11656, 2019-06-27). Gao's follow-up cites Appendix A as a formulation of the spectral-gap conjecture addressed by this paper; the survey also discusses the response of Laughlin correlations to perturbations. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [D. Gosset and E. Mozgunov, *Local gap threshold for frustration-free spin systems*](https://arxiv.org/abs/1512.00088) (arXiv:1512.00088, J. Math. Phys. 2016). Sharpens Knabe's finite-size criterion, which is cited in the paper's proof-strategy section as the standard route via positivity of $H^2-\gamma H$.
- [N. Rougerie, *On the stability of Laughlin's fractional quantum Hall phase*](https://arxiv.org/abs/2208.02619) (arXiv:2208.02619, 2022). Review of the rigidity and incompressibility of the Laughlin phase from a mathematical-physics viewpoint; it complements the 2019 Rougerie survey the paper cites for the spectral-gap conjecture.

## Digests and expositions
- None found.

## News and blogs
- [Azmat (Binary Verse AI), *Laughlin Spectral Gap: OpenAI's Proof And The New 1/5 Bound*](https://binaryverseai.com/laughlin-spectral-gap-conjecture/) (blog post, 14 October 2026). Explains the $1/25$ result and the Lean scope documentation, and covers Gao's $1/5$ refinement; no outside experts are quoted.
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (self-published audit, 2026-10-10). Entries F-541 and F-542 report exact-arithmetic checks of both manuscripts' seven-row certificates, including 13 three-body margins and 23 four-body certificates, with certification limited to these finite components. [family-level]
