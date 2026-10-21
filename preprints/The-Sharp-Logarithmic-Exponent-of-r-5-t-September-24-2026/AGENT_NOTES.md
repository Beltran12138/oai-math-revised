# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Qizhong Lin, Qiuyang Zhang, *The logarithmic exponent of the Ramsey number r(4,t)*](https://arxiv.org/abs/2610.17891) (arXiv:2610.17891, 13 Oct 2026). Proves $t^3/(\log t)^{2+\varepsilon}\le r(4,t)\le Ct^3/(\log t)^2$, taking the lower bound $r(5,t)\ge t^4/(\log t)^{3+\delta}$ from Theorem 1.1 of this paper as an explicitly stated "external input" combined with Shearer's 1995 independence estimate, and also giving a sharper transfer using Li–Rousseau–Zang.
- [Kaizhe Chen, *A note on the logarithmic exponent of Ramsey number r(4,t)*](https://arxiv.org/abs/2610.15293) (arXiv:2610.15293, 11 Oct 2026). Informal note that cites this paper (s=5) and its companion (s≥6), and derives $r(4,t)=t^3/(\log t)^{2+o(1)}$ from them via a transfer principle from $r(s,t)$ to $r(s-1,t)$. [family-level]

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 170*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/170.md) (lean/docs/170.md, 2026-10-06). The release's scope note says the Lean development proves the eventual bounds $t^4/(\log t)^{3+\varepsilon}\le r(5,t)\le Ct^4/(\log t)^3$ and the limit of the logarithmic exponent along natural $t$, with comparator statement RamseyFive.lean (and SharpLogRamsey.lean for the companion paper). [family-level]
- [OpenAI, *RamseyFive/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/RamseyFive/Main.lean) (openai/math, commit adc7f12). The top-level Lean file for this paper, stating `main : SharpBounds ∧ SharpExponent` in namespace `OAI.SharpRamseyFive`.
- [Erdős Problem a Day, *#986: OpenAI's two Lean proofs kernel-replayed here*](https://erdosproblemaday.com/day/986-openai-sharp-log-exponent-off-diagonal-ramsey-refereed) (2026-10-20). Reports rebuilding and kernel-checking both Lean developments, matching their comparator statements, and developing an $s=4$ extension and a bridge to Formal Conjectures' Ramsey definition; the accompanying manuscript review is explicitly attributed to AI agents. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- [Domagoj Bradač, *Off-diagonal Ramsey numbers*](https://arxiv.org/abs/2605.28793v3) (arXiv:2605.28793v3, 2026-06-16). Chen and Lin–Zhang identify its lower bound $r(s,t)\ge c_s t^{s-1}/(\log t)^{2s-4}$ as the preceding polynomial-exponent result whose logarithmic loss the OpenAI family improves. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [Dhruv Mubayi, Jacques Verstraëte, *A note on pseudorandom Ramsey graphs*](https://arxiv.org/abs/1909.01461) (arXiv:1909.01461; J. Eur. Math. Soc. 2024). Gives the conditional pseudorandom-graph route to $r(s,t)=t^{s-1+o(1)}$, which is background to the finite-geometry lower-bound history in this paper's introduction (the companion paper cites it; this paper does not).
- [Marcelo Campos, Matthew Jenssen, Marcus Michelen, Julian Sahasrabudhe, *A new lower bound for the Ramsey numbers R(3,k)*](https://arxiv.org/abs/2505.13371) (arXiv:2505.13371, May 2025). Constant-factor lower bound $(1/3+o(1))k^2/\log k$ for $s=3$, relevant to the constant-factor asymptotic for $t^4/(\log t)^3$ that the paper says it leaves open.

## Digests and expositions
- [Latent Seminar, *Sharp logarithmic exponents for off-diagonal Ramsey numbers*](https://lowrank.github.io/latent-seminar/OpenAI-Math/170-off-diagonal-ramsey) (2026-10-07). Explains the two manuscripts' flag graphs, selected-sequence entropy bounds and compression iteration, while distinguishing exposition from independent proof verification. [family-level]
- [AI Proved What?, *Ramsey numbers: log power settled?*](https://aiprovedwhat.com/episodes/170-sharp-logarithmic-exponents-off-diagonal/) (episode 170, October 2026; last checked 2026-10-19). Provides an animated introduction and written transcript covering both papers' claims, proof strategy and distinction between a sharp logarithmic exponent and a constant-factor asymptotic. [AI-generated per source] [family-level]
- [Wolfram MathWorld, *Ramsey Number*](https://mathworld.wolfram.com/RamseyNumber.html) (MathWorld entry, footer dated 20 Oct 2026). The entry describes the Lin–Zhang $r(4,t)$ refinement as "using an external OpenAI theorem asserting R(5,t)>=t^4/(lnt)^(3+delta)" and notes that this input "has not been independently verified here".

## News and blogs
- None found.
