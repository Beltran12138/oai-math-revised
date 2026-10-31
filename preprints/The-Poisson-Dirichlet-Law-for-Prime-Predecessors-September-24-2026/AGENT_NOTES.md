# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Manjul Bhargava (contributor), *Every nonsquare integer not equal to $-1$ is a primitive root modulo a positive lower density of primes*](https://hexagonmath.org/abs/2610.00228v1) (hexagon:2610.00228v1, 2026-10-14). Cites this paper's Theorem 3.1, the one-sided marked Type II estimate, as an input for counting primes; its provenance statement describes human notes expanded with GPT-6, and its Lean deductions treat the cited OpenAI theorems as explicit hypotheses.
- [Manjul Bhargava (contributor), *Rational points on elliptic curves that are primitive modulo a positive proportion of primes*](https://hexagonmath.org/abs/2610.00294v1) (hexagon:2610.00294v1, 2026-10-17). Uses "the marked Type II estimates of OpenAI", citing this paper's Theorem 3.1 and Sections 3–5; Hexagon lists the authorship as mixed.
- [Plasma AI, *The normal order of the number of iterations of Euler’s function*](https://github.com/plasma-ai/erdos-408/blob/main/paper/totient_iterates.pdf) (preprint, Palomar PALOMAR-2026-10-19-000009, 2026-10-19). Derives a normal order for iterated-totient heights (Erdős #408), extending this paper's Theorem 3.1 (one-sided Type II) and Theorem 6.1 (two-sided correlation) with the rates it needs. [family-level]
- [Guangshi Lü, Zhiwei Wang, Jie Wu, *On the Hardy--Littlewood--Chowla conjecture*](https://arxiv.org/abs/2610.20242) (arXiv:2610.20242, 2026-10-14). Claims $\sum_{p\le x}\mu(p+2)=o(\pi(x))$, building auxiliary operators "similar to" Sections 4.1–4.3 of this paper and following the argument of its Lemma 3.3 in Appendix A; the acknowledgements thank ChatGPT for help understanding this paper's methods, establishing Appendix A and checking the manuscript.
- [Jizhou Guo, *The Möbius function at $N-p$*](https://github.com/aster2024/openai-math-followups/blob/main/mobius-goldbach-shift/README.md) (preprint, v2 2026-10-23, v1 2026-10-22). Conditional on the correctness of the arguments of Lü–Wang–Wu (hypothesis H2′) and, for the main Goldbach-shift result, on the zero-free half-plane $\Re s>7/8$, it claims $\sum_{p<N}\mu(N-p)=o(\pi(N))$ for even $N$; it depends on this paper only through the Lü–Wang–Wu steps modelled on Sections 4.1–4.3 and Lemma 3.3, and states that its programs do not verify those arguments.
- [Jizhou Guo, *Consequences of results in the OpenAI mathematics release*, Entry 2](https://github.com/aster2024/openai-math-followups/blob/main/consequences/README.md) (preprint, 2026-10-08). Deduces, conditionally on this paper's Theorem 1.1, the lower bounds $C(x)\ge x^{5/12-\varepsilon}$ for Carmichael numbers ($x^{0.4736-\varepsilon}$ with Harman's admissible value) and $N_C(x)\ge x^{1-\varepsilon}$ for Novák–Carmichael numbers. [AI-generated per source] [family-level]

## Comments and discussion
- None found.

## Formalization
- [Plasma AI, *erdos-408* (Lean 4)](https://github.com/plasma-ai/erdos-408) (Palomar [PALOMAR-2026-10-19-000009 v1](https://data.palomar-registry.org/entries/PALOMAR-2026-10-19-000009-v1.json), 2026-10-19). The README says the extensions of Theorems 3.1 and 6.1, the block sieve (Lemma 2.6) and Propositions 6.2–6.3 are proved in Lean, with graph inputs from vendored totient-fibers-lean4 code. [family-level]
- [Yao Xu (@cadamcat), *artin-primitive-roots-lean4*](https://github.com/cadamcat/artin-primitive-roots-lean4) (GitHub, accessed 2026-10-21). A Lean 4 formalization of an Artin primitive-root result from the release whose README names this paper's Theorem 3.1 as the marked prime estimate used in part 1, without saying whether that estimate is itself formalized. [AI-generated per source]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- [eigendash, *openai-math-visualised*](https://github.com/eigendash/openai-math-visualised) (GitHub, accessed 2026-10-21). Numerical probes of Theorem 1.1 over primes $p\le 3\times10^7$, reporting that means of components 1–2 roughly agree with $\mathrm{PD}(1)$ while components 3–8 deviate, a drift the repository says resembles an unconverged limit over too short a range.
- [Perplexity / Orply, *Prime Predecessor Factors Converge to the Poisson–Dirichlet Law*](https://orply.com/articles/perplexity/011-2-the-poisson-dirichlet-law-for-prime-predecessors-ebc20891) (Orply, 2026-10-08). Explains the manuscript’s ranked logarithmic factor partition, equal weighting of primes, and size-biased route to the claimed limiting law. [AI-generated per source]

## News and blogs
- None found.
