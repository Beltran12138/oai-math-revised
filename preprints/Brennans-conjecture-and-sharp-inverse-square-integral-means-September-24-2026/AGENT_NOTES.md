# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Ilia Binder, Oleg Ivrii, István Prause, Stanislav Smirnov, *Brennan's Conjecture and the Universal Integral Means Spectrum*](https://arxiv.org/abs/2610.23853) (arXiv:2610.23853 [math.CV], 16 Oct 2026). Cites this paper and its companion and gives a short proof that $B_b(t)\le t^2/4$ for $t\in[-2,2]$. Via Makarov's identity $B(t)=\max\{B_b(t),3t-1\}$, this yields Brennan's conjecture $B(-2)=1$; the authors say they reached it "while validating these results". [family-level]

## Comments and discussion
- [Ilia Binder, Oleg Ivrii, István Prause, Stanislav Smirnov, §1.2–1.3 of *Brennan's Conjecture and the Universal Integral Means Spectrum*](https://arxiv.org/abs/2610.23853) (arXiv:2610.23853, 16 Oct 2026). The authors write that "none of the techniques appear unprecedented, their combination in this context was missed by the human experts". They add that the AI proofs contain derivations "that, while correct, are redundant". [family-level]

## Formalization
- [OpenAI math release, *Lean scope notes for family 072*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/072.md) (lean/docs/072.md). Describes the release's Lean formalization of the area-integrability range $4/3<s<4$ (equivalently $-2<t<2/3$), the uniform inverse-square bound with exponent $-1-\varepsilon$, $B_{\mathcal S}(-2)=1$, and Koebe divergence at the endpoints. The comparator statements are `Brennan.lean` and `BrennanSharp.lean`. [family-level]
- [google-deepmind/formal-conjectures, *FormalConjectures/Wikipedia/Brennanconjecture.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/Brennanconjecture.lean) (formal-conjectures repository). An independent Lean statement of the unrestricted and bounded Brennan endpoint identities, with proofs left as `sorry`; $B(-2)=1$ is tagged `research solved` with a link to the OpenAI Lean proof, while $B_b(-2)=1$ remains tagged `research open`.
- [mo271, *feat: mark problems solved in the OpenAI math release and link formal proofs*](https://github.com/google-deepmind/formal-conjectures/pull/6898) (formal-conjectures PR #6898, merged 11 Oct 2026). This PR marks "Brennan B(-2) = 1" as solved and leaves "Brennan bounded spectrum" open "on purpose".
- [Carlos Toledo’s cert-machine, *Statement-scope audit: family 072*](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-statements.json) (cert-machine, snapshot `9814e4c`). The report identifies Brennan’s integrability interval and the strict Kraetzer bound as stated in the Lean challenges, but flags that the manuscript’s spectral identity for all $t\le -2$ is represented there only at $t=-2$. [family-level]

## Related prior literature mentioned by others
- [Lars V. Ahlfors, *Quasiconformal reflections*](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5956-11511_2006_Article_BF02391816.pdf) (Acta Mathematica 109, 1963). Binder et al. identify this as an antecedent of the papers' critical-point maps. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- [AI Proved What?, *Four thirds to four? Brennan’s conjecture and the integral-means spectrum*](https://aiprovedwhat.com/episodes/072-brennans-conjecture-integral-means-spectrum/) (episode 072, October 2026). Animated exposition and transcript covering both claims, Koebe endpoint behavior, the probability-law construction, and the saddle–maximum comparison; its status discussion does not incorporate the Binder–Ivrii–Prause–Smirnov follow-up. [AI-generated per source] [family-level]
- [Ilia Binder, *Brennan, quadratic bounds, and AI*](https://events.k-state.edu/event/copy-of-28th-distinguished-harry-e-valentine-lecture-can-a-computer-see-the-shape-of-a-domain) (Kansas State University Analysis Seminar, 28 October 2026). The seminar abstract describes a shorter deterministic proof of the quadratic spectrum bound that retains the OpenAI proof’s Morse-theoretic idea, using maxima–saddle counts, a signed-area identity, and a radial estimate.

## News and blogs
- None found.
