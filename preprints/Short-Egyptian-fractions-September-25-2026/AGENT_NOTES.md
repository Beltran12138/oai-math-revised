# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-23.

## Follow-up works
- [Thomas F. Bloom and Wouter van Doorn, *Optimal bounds for the length and number of unit fraction representations*](https://hexagonmath.org/abs/2610.00407v1) (hexagon:2610.00407v1, 2026-10-20). A human-written exposition and simplification of this paper's proofs of $N(b)\ll\log\log b$, $\log\log F(k)\gg k$ and $\log\log v(k)\gg k$, deriving Theorem 1 from the more elementary prescribed-denominator argument and discussing improved constants in Section 5. The same note is also hosted at [erdosproblems.com](https://www.erdosproblems.com/static/UnitFractions.pdf).
- [Thomas Bloom (@thomasfbloom), post on X](https://x.com/thomasfbloom/status/2110500887026151887) (2026-10-14). A 12-post thread announcing the Bloom-van Doorn exposition, which describes the proof of the $O(\log\log b)$ bound as "short and elementary", combining sum-product theory and the weak Goldbach problem, and notes that the AI paper proved the bound twice, first in a long way and then "in a much shorter and simpler way".

## Comments and discussion
- [Thomas F. Bloom and Wouter van Doorn, Section 6 "Comparison to the AI-generated paper"](https://www.erdosproblems.com/static/UnitFractions.pdf) (hexagon:2610.00407v1, October 2026). Says the later elementary argument for $v(k)$ also gives Theorem 1, so "the technical arguments of Sections 3-5 (occupying 15 pages, out of 33 total) are entirely redundant"; it also criticizes the exposition and attribution of novelty, and the authors state they had not read Sections 3-5 in detail.
- [Thomas Bloom, *Erdős Problem #304*](https://www.erdosproblems.com/304) (erdosproblems.com, last edited 2026-10-16). The problem page now refers to "the recent OpenAI proof that $N(b)\ll \log\log b$" and links the paper and the Bloom-van Doorn exposition.
- [Thomas Bloom, *Erdős Problem #293*](https://www.erdosproblems.com/293) (erdosproblems.com, last edited 2026-10-16). Credits the paper with the proof that $\log\log v(k)\gg k$ (the paper's prescribed-denominator corollary), after van Doorn and Tang's $\log v(k)\gg k^2$.
- [Thomas Bloom, *Erdős Problem #148*](https://www.erdosproblems.com/148) (erdosproblems.com, last edited 2026-10-16). Credits the paper with the proof that $\log\log F(k)\gg k$; the page cites Elsholtz-Planitzer for the best known upper bound on $F(k)$.

## Formalization
- [OpenAI math release, Lean scope notes for family 025](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/025.md) (OpenAI Math Release, 2026-10-06). Per these notes, the release's Lean development proves the $\Theta(\log\log b)$ order of $N(b)$, $\log\log F(k)=\Theta(k)$, and $e^{e^{k/600}}\le v(k)\le 1+k^{2^{k-1}}$ for large $k$, via the comparator challenges `EgyptianFractions.lean` and `ShortEgyptianFractions.lean`.
- [Google DeepMind formal-conjectures, *FormalConjectures/ErdosProblems/304.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/304.lean#L25) (formal-conjectures). The statement `upper_bound` ($N(b)=O(\log\log b)$) is tagged `research solved` and links to the release's Lean proof `lean/OAI/NumberTheory/ShortEgyptian/Main.lean`, while the local theorem body remains `sorry`; the change came in [PR #6898](https://github.com/google-deepmind/formal-conjectures/pull/6898) (merged 2026-10-11).
- [thepriceisright/publications, *Lower1950.lean*](https://github.com/thepriceisright/publications/blob/8f055eb3fd1485477c92cbfbdfa4b3c56f192610/erdos/304/Lower1950.lean) (GitHub, commit 8f055eb; accessed 2026-10-21). A separate Aristotle-generated formalization of the classical lower bound for Erdős Problem 304, compiled against pinned formal-conjectures definitions; it does not cover the paper's new upper bound. [AI-generated per source]

## Related prior literature mentioned by others
- [Wouter van Doorn (with ChatGPT), *Practical numbers and Egyptian fractions*](https://github.com/Woett/ChatGPT-s-note-on-Erdos18) (GitHub, uploaded 2026-09-16). An earlier, mostly AI-written note with Lean formalization proving $N(b)\le 2c_0(\log\log b)^2$ and $v(k)\ge\exp(\exp(\sqrt{k/(2c_0)}))$, with $c_0=14/\log 2$, via practical numbers; Bloom-van Doorn cite it as the previous best bound. [AI-generated per source]
- [Ernest S. Croot III, *On a coloring conjecture about unit fractions*](https://arxiv.org/abs/math/0311421) (Ann. of Math. 157 (2003), 545-556). Bloom-van Doorn say the Fourier method in the paper's proof of Theorem 1 is closely related to Croot's work; the paper cites Croot's 1999 Mathematika paper but not this one.
- [K. Soundararajan, *Approximating 1 from below using n Egyptian fractions*](https://arxiv.org/abs/math/0502247) (arXiv:math/0502247, 2005-02-11). Cited by Bloom-van Doorn in Appendix A for the classical approximation bound used to obtain the complementary bounds for the three results.
- [Thomas F. Bloom and Christian Elsholtz, *Egyptian fractions*](https://arxiv.org/abs/2210.04496) (arXiv:2210.04496; Nieuw Arch. Wiskd. 2022). A survey of open problems and recent progress on unit fractions, cited by Bloom-van Doorn for background.

## Possibly relevant literature (found by the agent, not checked)
- None found.

## Digests and expositions
- [heyprof, *Short Egyptian fractions*](https://www.heyprof.app/en/demo/aegyptische-brueche) (VisuApp, undated; accessed 2026-10-21). A paper-specific interactive exposition comparing greedy and shortest expansions and illustrating the historical length bounds.

## News and blogs
- [OfficeChai Team, *OpenAI Has Also Included Proofs For 23 Erdos Problems In Its Latest Math Proof Drop*](https://officechai.com/ai/openai-has-also-included-proofs-for-23-erdos-problems-in-its-latest-math-proof-drop/) (OfficeChai, 2026-10-09). Reports Thomas Bloom's list of Erdős problems addressed by the release, grouping problems 148, 293 and 304 under this paper and noting that Bloom had not verified the proofs.
- [Azmat, *Short Egyptian Fractions: How OpenAI’s Proof Solved Erdős’s 76-Year-Old Conjecture and Established the Optimal Double-Logarithmic Bound*](https://binaryverseai.com/short-egyptian-fractions-openai-erdos-proof/) (Binary Verse AI, 2026-10-16). Walks through the paper's dense-family construction and two corollaries and discusses the published Lean scope.
