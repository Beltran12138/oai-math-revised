# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Yangyan Gu, Rongxing Xu, *A shorter proof of the linear list Hadwiger conjecture*](https://arxiv.org/html/2610.01946v2) (arXiv:2610.01946v2, revised 2026-10-12). Revised version of a paper whose v1 this manuscript cites; it gives a simpler proof of a weaker form of this paper's Proposition 3.1 (graphs on at most $t(\ln t)^5$ vertices) and reuses its thinning argument as Lemma 2.9 to give a shorter proof of the conjecture.

## Comments and discussion
- None found.

## Formalization
- [OpenAI, Lean scope note for family 157 (`lean/docs/157.md`)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/157.md) (openai/math release, 2026-10-06). The release's formalization proves the existence of one integer $C\ge1$ with $\chi_{\mathrm{list}}(G)\le C\,h(G)$ for all finite nonempty simple graphs (comparator file `ListHadwiger.lean`). [family-level]
- [anxkhn, *feat(Paper): add the linear list-Hadwiger bound*, google-deepmind/formal-conjectures PR #6981](https://github.com/google-deepmind/formal-conjectures/pull/6981) (opened 2026-10-08, open). Adds this paper's Theorem 1.1 as a formal-conjectures statement pinned to the release; a reviewer found no statement mismatch but reports Comparator and compilation compatibility failures, and the PR is not yet approved.
- [Sergey Norin and Raphael Steiner, *Linear Hadwiger's conjecture in Lean*](https://github.com/snorin239/LinearHadwiger) (GitHub; README reports a build on 2026-09-25). This separate development formalizes their ordinary-coloring bound, corresponding to the type of conclusion in Corollary 1.2 rather than the arbitrary-list theorem, and attributes the formalization to Codex under the authors' guidance. [AI-generated per source]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Sergey Norin, Raphael Steiner, *A Proof of the Linear Hadwiger Conjecture*](https://arxiv.org/abs/2610.05291) (arXiv:2610.05291, 2026-10-04). Independently proves that $K_t$-minor-free graphs are $Ct$-colorable, the ordinary bound in Corollary 1.2, and its Section 4 identifies the absence of a list-coloring analogue of their Lemma 13 as an obstacle to extending the method; its abstract states the proof "was found by GPT-6 Astra, following the directions by the authors". [AI-generated per source]
- [David R. Wood, *Tweaking the constant in the Linear Hadwiger Theorem*](https://arxiv.org/html/2610.10831) (arXiv:2610.10831, 2026-10). Optimizes the Norin–Steiner argument to the explicit constant 1,118,430 for the ordinary linear bound, whereas the constant in this paper's Theorem 1.1 is not computed; its AI-use statement reports using Claude Opus 5.5 and GPT-6.

## Digests and expositions
- None found.

## News and blogs
- None found.
