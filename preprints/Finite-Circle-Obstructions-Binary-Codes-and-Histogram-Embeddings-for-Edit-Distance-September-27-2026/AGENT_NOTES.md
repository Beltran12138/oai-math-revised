# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *The sharp exponential scale of edit-distance distortion: Lean scope note*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/099.md) (OpenAI Math release, lean/docs/099.md, 2026). The release's scope note lists a comparator statement (FiniteCircle.lean) covering both finite-circle lower constructions, their binary coding transfers, and the finite histogram upper embedding, uniformly over finite alphabets and including the empty word. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [G. Cormode and S. Muthukrishnan, *The string edit distance matching problem with moves*](https://www.cs.ox.ac.uk/people/graham.cormode/pubs/html/CormodeMuthukrishnan07.html) (ACM Transactions on Algorithms 3(1), 2007). Embeds edit distance with substring moves into L1 with O(log n log* n) distortion; related to the moves-based expansion estimate in the paper's histogram upper construction (Section 8).
- [M. Charikar and R. Krauthgamer, *Embedding the Ulam metric into ℓ1*](https://toc1234.cs.uchicago.edu/articles/v002a011) (Theory of Computing 2, Article 11, 2006). Proves O(log n) ℓ1 distortion for edit distance on permutations, a comparison point for the alphabet-uniform constants in Theorem 1.1 and for the role of repeated symbols in the lower constructions.
- [A. Andoni and K. Onak, *Approximating Edit Distance in Near-Linear Time*](https://arxiv.org/abs/1109.5635) (arXiv:1109.5635, 2011). Gives a near-linear-time 2^{Õ(√log n)} approximation for edit distance, an algorithmic counterpart to the overlapping-substring recursion of Ostrovsky and Rabani that the paper's histogram embedding develops.

## Digests and expositions
- [Latent Seminar, *Edit distance in L1: alignment obstructions and matching exponential scales*](https://lowrank.github.io/latent-seminar/OpenAI-Math/099-edit-distance-embeddings) (6 October 2026). This exposition compares the three manuscripts' alignment obstructions, Fourier arguments, binary transfers, and upper embeddings, explicitly stating that it does not independently verify the complete proofs. [family-level]

## News and blogs
- None found.
