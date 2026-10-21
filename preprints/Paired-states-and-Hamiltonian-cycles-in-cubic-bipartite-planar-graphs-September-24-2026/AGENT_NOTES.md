# Automatically collected context

Collected by an AI agent (Claude Opus 5.5) on 2026-10-20.

## Follow-up works
- None found.

## Expert comments and discussion
- [Gil Kalai, *Updates: Sharing AI progress on mathematics (amazing!); and my lecture plans*](https://gilkalai.wordpress.com/2026/10/07/updates-sharing-ai-progress-on-mathematics-amazing-and-my-lecture-plans/) (Combinatorics and more, 2026-10-07). Lists the manuscript as announcing a proof of Barnette's conjecture and links his earlier blog discussion of the conjecture.
- [jboggan, Hacker News](https://news.ycombinator.com/item?id=49987920) (2026-10-07). A commenter who reports working on the conjecture as a hobby since 2002 describes the proof as constructively selecting the edges not in the cycle, with a key step using a complex-valued exponential sum over edges.
- [jboggan, Hacker News](https://news.ycombinator.com/item?id=49988192) (2026-10-07). Same commenter characterizes the paper as short and tractable, with the disk lemma and cancellation calculations as the main parts to digest.
- [jboggan, Hacker News](https://news.ycombinator.com/item?id=49988526) (2026-10-07). Reports that an LLM-coded implementation of the paper's constructive algorithm passed the commenter's existing test suite of graphs.
- [prideout, Hacker News](https://news.ycombinator.com/item?id=49985321) (2026-10-06). Commenter who had tried the conjecture with AI models says the proof "looks approachable at first glance."

## Formalization
- [OpenAI, *Lean scope note for family 180*](https://github.com/openai/math/blob/main/lean/docs/180.md) (openai/math release, 2026-10-06). States that the release's Lean formalization proves the existence of a Hamiltonian cycle for every finite simple cubic bipartite planar 3-vertex-connected graph, with challenge statement [BarnetteHamiltonian.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/BarnetteHamiltonian.lean) and proof modules under [lean/OAI/Combinatorics/Hamiltonian](https://github.com/openai/math/tree/main/lean/OAI/Combinatorics/Hamiltonian); as of 2026-10-20 the family is not listed in `lean/formalization.yaml`.
- [explainx.ai, *OpenAI Math Results: 8 Claims, Lean Status, Expert Views*](https://explainx.ai/blog/openai-math-results-that-matter-expert-reactions-2026) (2026-10-07, updated to 2026-10-15). Notes the `formalization.yaml` omission and that the challenge file requires a single spanning cycle rather than a possibly disconnected 2-factor; the author did not build the Lean code.
- [anxkhn, *Add Barnette's Hamiltonian-cycle conjecture and manuscript result*](https://github.com/google-deepmind/formal-conjectures/issues/7144) (formal-conjectures issue #7144 and [PR #7149](https://github.com/google-deepmind/formal-conjectures/pull/7149), opened 2026-10-11, open). Proposes adding the statement with a reusable plane-embedding structure but no `formal_proof` link, since the external proof was not built or run through Comparator; a reviewer asked whether an already-closed conjecture should be added.

## Related prior literature mentioned by others
- [thomasahle, Hacker News](https://news.ycombinator.com/item?id=49989754) (2026-10-07). Relays a ChatGPT literature search suggesting that the cancellation trick resembles fully packed O(n) loop models, where complex phases on loop orientations cancel and the n→0 limit is used for Hamiltonian cycles.
- [jboggan, Hacker News](https://news.ycombinator.com/item?id=49988654) (2026-10-07). Points to Penrose's work on counting Tait (edge) colourings of planar cubic graphs and to Kasteleyn-sign and matrix-tree analogies as possible precedents for the construction.

## Possibly relevant literature (found by the agent, not checked)
- [Jesper Lykke Jacobsen, Jané Kondev, *Field theory of compact polymers on the square lattice*](https://arxiv.org/abs/cond-mat/9804048) (Nucl. Phys. B, 1998; arXiv:cond-mat/9804048). A standard reference on fully packed loop models and compact polymers (Hamiltonian walks), the physics setting named in the Hacker News comment above.
- [Peter Zograf, *The enumeration of edge colorings and Hamiltonian cycles by means of symmetric tensors*](https://arxiv.org/abs/math/0403339) (arXiv:math/0403339, 2004). Penrose-style tensor contractions that enumerate edge colourings and Hamiltonian cycles, a possible precedent for algebraic cancellation approaches.
- [Gunnar Brinkmann, Jan Goedgebeur, Brendan D. McKay, *The Minimality of the Georges-Kelmans Graph*](https://arxiv.org/abs/2101.00943) (Math. Comp., 2022; arXiv:2101.00943). Among other results, reports computational verification of Barnette's conjecture up to at least 90 vertices, a possible test bed for the manuscript's constructive algorithm.
- [Jan Florek, *A sufficient condition for cubic 3-connected plane bipartite graphs to be hamiltonian*](https://arxiv.org/abs/2309.09578) (arXiv:2309.09578, 2023). Recent partial result on Barnette's conjecture generalizing Goodey's face-size condition.
- [Bojan Mohar, *Barnette's Conjecture* (problem page)](https://users.fmf.uni-lj.si/mohar/Problems/P4BarnetteConjecture.html) (University of Ljubljana, undated). Problem page recording the Holton–Manvel–McKay computer verification (1985) and a 2002 announcement by Aldred, Brinkmann and McKay extending it to 84 vertices.
- [Lennart Rudolph, *A Counterexample to Prescribed-Cycle Recovery in Barnette Graphs*](https://zenodo.org/records/21890733) (Zenodo, 2026-08-11). AI-assisted note giving a 16-vertex Barnette graph whose particular Hamiltonian cycle cannot be produced by a known book-embedding algorithm, relevant to which cycles constructive methods can reach.

## Digests and expositions
- None found.

## News and blogs
- [Hacker News, *Sharing AI progress in mathematics*](https://news.ycombinator.com/item?id=49984923) (2026-10-06). Main discussion thread of the release, where most of the Barnette-specific comments above appear.
- [Brandon Harvey, *What happened in math on October 6*](https://kraken.substack.com/p/what-happened-in-math-on-october) (Substack, 2026-10-08). Newsletter that quotes a post relaying the Hacker News reaction to the Barnette proof.
