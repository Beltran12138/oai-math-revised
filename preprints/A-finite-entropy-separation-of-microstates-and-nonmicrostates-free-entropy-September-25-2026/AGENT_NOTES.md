# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [David Jekel, *On counterexamples to the unification of free entropy*](https://arxiv.org/abs/2610.27243) (arXiv:2610.27243, 19 Oct 2026). Cites this preprint as the first example with $-\infty<\chi<\chi^*$, and presents a similar example with a diffuse (semicircular) last variable in place of the discrete one, proving the gap through a Wasserstein-distance lower bound instead of the data-processing argument.

## Expert comments and discussion
- None found.

## Formalization
- [mathcommunity/oai-math-revised, *lean/docs/298.md*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/298.md) (Lean scope notes of the release). States that the formalization constructs a bounded self-adjoint tuple with $-\infty<\chi(X)\le\chi^*(X)-1/2<\infty$, using operator-norm cutoff and a limsup over matrix sizes, and links the comparator statement `FiniteEntropySeparation.lean`.
- [OpenAI, *lean/OAI/Analysis/FreeEntropy/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/FreeEntropy/Main.lean) (openai/math, commit adc7f12). The release's Lean proof of the theorem `FiniteEntropySeparation.main`, whose statement is given in the separate comparator file [FiniteEntropySeparation.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/FiniteEntropySeparation.lean), where `chi` and `chiStar` are defined from first principles.

## Related prior literature mentioned by others
- [David Jekel and Jennifer Pi, *An Elementary Proof of the Inequality $\chi\leq\chi^*$ for Conditional Free Entropy*](https://arxiv.org/abs/2305.02574) (arXiv:2305.02574, 2023; revised 2024). The AI Proved What? episode links this comparison theorem as background; the manuscript uses its classical-to-free Fisher-information comparison to transfer the positive-time entropy deficit to the original tuple.
- [M. Fathi and B. Nelson, *Free Stein kernels and an improvement of the free logarithmic Sobolev inequality*](https://arxiv.org/abs/1605.05828) (arXiv:1605.05828; Adv. Math. 317, 2017). Jekel (arXiv:2610.27243) cites it as part of the free Stein-kernel literature providing context for the Stein-type identity used in this preprint; its free HSI inequality and entropic CLT also relate to the Sections 3–4 estimates relative to a semicircular family.
- [C.-P. Diez, *Free Stein kernels, free moment maps, and higher order derivatives*](https://arxiv.org/abs/2306.00967) (arXiv:2306.00967, 2023). Jekel cites it as related work for the same Stein-type identity; it relates higher-order free Stein discrepancies to relative free Fisher information and nonmicrostates free entropy.

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- [AI Proved What?, *Both finite, still unequal? Voiculescu’s two free entropies*](https://aiprovedwhat.com/episodes/298-free-entropy/) (episode 298, October 2026). This video and accompanying transcript explain the two entropy definitions, the proposed block-structure and noise-scale argument, and the limitation to a very large fixed number of variables. [AI-generated per source]

## News and blogs
- None found.
