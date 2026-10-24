# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 110: Optimal-order randomized k-server on arbitrary metrics*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/110.md) (lean/docs/110.md, October 2026). The release's own scope description: it says a uniform randomized bit algorithm on finite rational metrics was formalized, with polynomial preprocessing and per-request time and an additive movement constant not claimed to be polynomially bounded, and it links the comparator statements. [family-level]
- [OpenAI, *UniformKServer/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/UniformKServer/Main.lean) (openai/math, commit adc7f12). Lean file containing `uniform_squared_logarithmic_main : UniformAlgorithmClaim`, the formal counterpart of Theorem 1.1. The file shows no `sorry`, but it imports further modules that were not inspected here.
- [OpenAI, *ComparatorChallenges/UniformKServer.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/UniformKServer.lean) (openai/math, commit adc7f12). Standalone comparator statement (proof left as `sorry` by design) covering boot halting, legal server labels on reachable requests, and the expected-cost bound, phrased via a bit-machine model.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Ben-David, Borodin, Karp, Tardos, Wigderson, *On the power of randomization in on-line algorithms*](https://cris.huji.ac.il/en/publications/on-the-power-of-randomization-in-on-line-algorithms/) (Algorithmica 11 (1994), 2–14, doi:10.1007/BF01294260). Classical game-theoretic treatment of online adversary models, including when an existentially proved online algorithm can actually be constructed; possibly relevant to the paper's goal of turning the companion paper's existence theorem into a computable algorithm.
- [Bubeck, Cohen, Lee, Lee, Mądry, *k-server via multiscale entropic regularization*](https://arxiv.org/abs/1711.01085) (arXiv:1711.01085, STOC 2018). Source of the $O(\log^2 k)$ HST algorithm and the $O(\log^3 k\log\Delta)$ dynamic-embedding bound, cited in the companion paper but not here; possibly relevant to this paper's comparison with the Coester–Cosson $O(\log n\log^2 k)$ bound (Section 1.1).

## Digests and expositions
- [Latent Seminar, *Randomized k-server: competitive ratios and uniform computation*](https://lowrank.github.io/latent-seminar/OpenAI-Math/110-randomized-k-server) (blog exposition, 2026-10-07). Exposition of both manuscripts' proof mechanisms, including partition and allocation costs, the bounded request filter, and delayed activation with an unrestricted additive constant; it states that it did not independently verify the complete proofs. [family-level]

## News and blogs
- None found.
