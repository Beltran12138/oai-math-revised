# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Radu Curticapean, Mingjun Liu, Daniel Neuen, and Tim Seppelt, *Lower Bounds for Weisfeiler–Leman*](https://zenodo.org/records/23213174) (Zenodo:10.5281/zenodo.23213174, 2026-10-07). This concurrent AI-assisted manuscript cites the paper and states EXPTIME- and XP-completeness for pair equivalence on simple bipartite 3-degenerate graphs; its preface dates the AI-assisted results to September 19–29 and describes the manuscript as a hastily written public timestamp. [AI-generated per source] [family-level]

## Comments and discussion
- None found.

## Formalization
- [OpenAI, *The computational complexity of Weisfeiler–Leman refinement: Lean scope notes*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/133.md) (OpenAI Math Release, lean/docs/133.md, 2026-10-06). The release's Lean scope note says EXPTIME-completeness of joint-update $k$-WL equivalence with binary $k\ge2$ is formalized, for general graphs and for connected equal-order simple uncolored graphs of maximum degree three, with comparator `VariableWL.lean`. [AI-generated per source] [family-level]
- [OpenAI, *lean/OAI/Combinatorics/VariableWL/Completeness.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/VariableWL/Completeness.lean) (openai/math, commit adc7f12, 2026). The release's Lean file containing `theorem main : EXPTIMEComplete WL ∧ EXPTIMEComplete SubWL`, the formal counterpart of the paper's Theorem 1.1.
- [Radu Curticapean, Mingjun Liu, Daniel Neuen, and Tim Seppelt, *Lean formalizations of Weisfeiler–Leman results*](https://zenodo.org/records/23213174/files/leanhom-zenodo-submission.zip?download=1) (supplement to Zenodo:10.5281/zenodo.23213174, 2026-10-07). The archive documents WL/game/homomorphism correspondence, round bounds and a deterministic register compiler, with decision-complexity reductions outside its scope. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- [Martin Grohe, Moritz Lichter, Daniel Neuen, and Pascal Schweitzer, *Compressing CFI Graphs and Lower Bounds for the Weisfeiler–Leman Refinements*](https://arxiv.org/abs/2308.11970) (arXiv:2308.11970v2, 2025-01-27; Journal of the ACM 72(3), 2025). Curticapean and coauthors cite its Ω(n^{k/2}) refinement-round bound as a predecessor to their concurrent work on this family. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [Phokion G. Kolaitis and Jonathan Panttaja, *On the Complexity of Existential Pebble Games*](https://api.openalex.org/works/https://doi.org/10.1007/978-3-540-45220-1_26) (CSL 2003, LNCS, pp. 314–329, doi:10.1007/978-3-540-45220-1_26). According to later citations, this work shows that deciding the existential $k$-pebble game is EXPTIME-complete when $k$ is part of the input, the existential-game analogue of the paper's Theorem 1.1 for the bijective game.

## Digests and expositions
- [Orply / Perplexity, *Weisfeiler–Leman Equivalence Remains EXPTIME-Complete on Subcubic Graphs*](https://orply.com/articles/perplexity/133-4-variable-dimension-weisfeiler-leman-equivalence-on-general-and-subcubic-graphs-475ea5b3) (Orply, 2026-10-11). This explicitly AI-assisted exposition outlines joint refinement, dimension capping, the bijective game and the subcubic construction, while stating that it omits full proofs. [AI-generated per source]

## News and blogs
- [Tim Seppelt, *News: Lower Bounds for Weisfeiler–Leman*](https://tseppelt.github.io/news/) (author website, 2026-10-07). Seppelt announces the concurrent manuscript in response to OpenAI’s release and reports extensions involving classical complexity, parameterized complexity and iteration bounds. [family-level]
