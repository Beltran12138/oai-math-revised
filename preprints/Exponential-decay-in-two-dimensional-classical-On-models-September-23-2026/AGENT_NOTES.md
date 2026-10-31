# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Anton Ragin, *The massive continuum limit of the two-dimensional O(4) sigma model*](https://zenodo.org/records/23349319) (Zenodo, doi:10.5281/zenodo.23349319, v7, 2026-10-13). Cites this manuscript; its stated conditional inputs are the O(4) renormalization-group paper and the O(3) continuum-limit paper, not this one. [AI-generated per source]
- [Masaki Oshikawa, *Faster-than-power-law decay of order parameter correlations in the two-dimensional RP2 model: a rigorous result by vibe-proving*](https://hexagonmath.org/abs/2610.00453v1) (hexagon:2610.00453v1, doi:10.5281/zenodo.23549037, 2026-10-22). States a bound $C\exp\{-c[\log(2+r)]^2\}$ on the two-point order-parameter correlation of the RP2 and RP3 models at every finite inverse temperature; its provenance statement says this paper was supplied to the AI system as the starting point. [AI-generated per source]

## Comments and discussion
- [Peter Hall and Joseph Howlett, *The most exciting claims from OpenAI's heap of new proofs*](https://www.scientificamerican.com/article/the-most-exciting-claims-from-openais-heap-of-new-proofs/) (Scientific American, 2026-10-08). Reports several release papers claiming to resolve the sigma-model analogue of the Yang-Mills mass-gap problem, quoting Michael Douglas and Roland Bauerschmidt (the first sigma-model paper "seems very reasonable", the second "horrible"); it does not identify the papers by title, and it is unclear whether this paper is among them. [family-level]
- [Rudy Pei (@PeaBrane10), post on X](https://x.com/PeaBrane10/status/2107739572344094729) (2026-10-07). States that the twist estimate in the proof of Polyakov's conjecture "never uses the sign of the couplings", so it would extend to show the 2D Heisenberg spin glass has finite χ_SG at every T > 0.
- [Zohar Komargodski (@ZoharKo), post on X](https://x.com/ZoharKo/status/2107976691855626565) (2026-10-07). Replies that the O(N) result "was known to be true from numerics for decades".

## Formalization
- [OpenAI math release, Lean scope note *Canonical O(3) continuum limit and exact O(4) mass asymptotics* (lean/docs/215.md)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/215.md) (release Lean documentation, 2026-10-06). States that the Lean development proves Theorem 1.1, exponential decay on finite free-boundary subgraphs with edge strengths in [0,β] for all n≥3 (comparator `ClassicalON.lean`), and excludes the infinite-volume limit and the O(4) spectral-gap claim.
- [Masaki Oshikawa, *rp2-rp3-lean*](https://github.com/masakioshikawa/rp2-rp3-lean) (GitHub, version 0.4.0; archived as [Zenodo doi:10.5281/zenodo.23548847](https://zenodo.org/doi/10.5281/zenodo.23548847), 2026-10-22). Lean 4 formalization of the log-square decay bound for the RP2 and RP3 models, which states that it adapts portions of OpenAI's ClassicalON development and does not import the O(n) decay theorem as an assumption. [AI-generated per source]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Ron Peled and Yinon Spinka, *Lectures on the Spin and Loop O(n) Models*](https://arxiv.org/abs/1708.00058) (arXiv:1708.00058, v3 2019). A survey of decay of correlations in spin O(n) models covering the two-dimensional n≥3 conjecture addressed by Theorem 1.1; not in the paper's bibliography.

## Digests and expositions
- [AI Proved What?, *Do spins forget?*](https://aiprovedwhat.com/episodes/215-o3-continuum-o4-mass-asymptotics/) (Episode 215, October 2026). Explains the five papers’ claims, proof strategies and differing formalization scopes. [AI-generated per source] [family-level]
- [Roland Bauerschmidt and contributors (README credits "the community"), *Digesting the O(3) NLSM construction*](https://github.com/bauerscr/nlsm) (GitHub repository bauerscr/nlsm, first commit 2026-10-13, latest commit 2026-10-29). Open effort to write a human-digested version of the O(3) construction; its README describes this paper as showing exponential decay without an estimate on $m(\beta)>0$, not used later, with a related idea strengthened in the later papers. [family-level]

## News and blogs
- None found.
