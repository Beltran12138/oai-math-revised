# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- [Elliot Kienzle, *Illustrating the AI proof of the Mahler conjecture*](https://chessapig.github.io/Mahler) (personal site, Oct 2026). Hand-drawn and interactive exposition of this paper's construction of large symplectic balls in $K\times K^\circ$, calling it "a clever construction applying a technique I haven't published yet"; Kienzle says he has not checked the details line by line. [family-level]

## Formalization
- [OpenAI math release, *Lean scope note for family 087*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/087.md) (lean/docs/087.md). States that for $n\ge2$ the formalization gives Gromov width 4 for $\mathrm{int}\,K\times\mathrm{int}\,K^\circ$ and embeddings of every ball of capacity $0<c<4$, without asserting an embedding at capacity 4. [family-level]
- [OpenAI math release, *Main.lean* (`symmetric_polar_main`)](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/PolarProducts/Main.lean) (openai/math, commit adc7f12). Lean statement of Theorem 1.1 (width equal to 4 and embeddings below capacity 4); the comparator challenge is `SymmetricPolar.lean`.

## Related prior literature mentioned by others
- [Shiri Artstein-Avidan, Roman Karasev, Yaron Ostrover, *From Symplectic Measurements to the Mahler Conjecture*](https://arxiv.org/abs/1303.4197) (arXiv:1303.4197; Duke Math. J. 163, 2014). Kienzle's exposition uses its Hofer–Zehnder capacity computation to explain the prior upper bound of 4, against which this paper supplies its ball-embedding lower bound.

## Possibly relevant literature (found by the agent, not checked)
- [Kun Shi, Guangcun Lu, *The Viterbo's capacity conjectures for convex toric domains and the product of a 1-unconditional convex body and its polar*](https://arxiv.org/abs/2008.04000) (arXiv:2008.04000, 2020). Proves the Viterbo volume-capacity inequality for $K\times K^\circ$ with $K$ 1-unconditional, a special case near the paper's claimed width and volume-product consequence; not in its bibliography.
- [Mark Berezovik, Roman Karasev, *Symplectic polarity and Mahler's conjecture*](https://arxiv.org/abs/2211.14630) (arXiv:2211.14630, Israel J. Math. 2025). Gives a symplectic reformulation of Mahler's conjecture and capacity bounds for symplectically self-polar bodies, related to the paper's symplectic route to the volume-product bound; not in its bibliography.

## Digests and expositions
- [OpenAI Math Digest, *Symplectic Balls in Symmetric Polar Products*](https://masataka123.github.io/OpenAI-Math-Digest/ja/papers/symplectic-polar-products/) (Japanese exposition, undated). Illustrated reading guide tracking the holomorphic ball construction, lens estimate uniform near the tips, approximation and volume consequence, distinguishing capacities below 4 from an endpoint embedding. [AI-generated per source]

## News and blogs
- None found.
