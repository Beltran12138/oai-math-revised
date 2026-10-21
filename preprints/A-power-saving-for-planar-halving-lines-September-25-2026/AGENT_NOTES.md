# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *Power savings for planar halving lines and k-sets: Lean scope notes*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/183.md) (OpenAI mathematics release, lean/docs/183.md, 2026-10-06). The release's formalization covers the $Cn^{4/3-\varepsilon}$ halving-pair bound (Theorem 1.1) and the switch bound under the generic-position assumptions (Theorem 1.2), with existential constants; the $k$-set corollary is not in scope. [family-level]
- [OpenAI, *HalvingLines.lean* comparator challenge](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/HalvingLines.lean) (openai/math, commit adc7f12). Comparator statement file: a single theorem `power_bounds` that states both the halving-pair bound and the switch-count bound, left as `sorry` and checked against the release's separate proof. [family-level]
- [anxkhn, *feat(Paper): add the planar halving-line power saving*](https://github.com/google-deepmind/formal-conjectures/pull/6979) (google-deepmind/formal-conjectures PR #6979, 8–11 October 2026). Independent PR adding the Theorem 1.1 statement to formal-conjectures with a bridge to the first conjunct of the pinned OpenAI `power_bounds` proof; reviewer bocowgill confirmed the statement matches Theorem 1.1 and approved on 11 October after running Comparator independently (with small Lean/Mathlib version adaptations). [AI-generated per source]
- [anxkhn, *Add the power-saving upper bound for planar halving lines*](https://github.com/google-deepmind/formal-conjectures/issues/6974) (google-deepmind/formal-conjectures issue #6974, 8 October 2026). Tracking issue for the PR above, restricted to halving pairs; the author discloses AI assistance (OpenCode using GPT-6.1 Sol). [AI-generated per source]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Tamaki and Tokuyama, *A Characterization of Planar Graphs by Pseudo-Line Arrangements*](https://ftp.iaorifors.com/paper/75874) (Algorithmica 35(3):269–285, 2003). Shows that Dey's $O(nk^{1/3})$ level bound also holds for pseudoline arrangements, which bears on the paper's remark that Corollary 1.3 "asserts no corresponding saving for pseudolines".

## Digests and expositions
- [Open Mathematics Courses / Claude Opus 5.5, *Results on halving lines and k-sets: the theorems, Dey's bound, the packing estimate and the tools of its proof, with their assumptions*](https://kokunoyumeto.github.io/open-math-courses-public/courses/planar-halving-lines/providers.html) (Open Mathematics Courses, undated). Guide linking lessons on the paper's rank sweeps, activity-packing argument, spatial limits and $k$-set conclusion; it states the lessons were written and self-checked by AI without completed independent mathematical review. [AI-generated per source]
- [heyprof, *Halving lines and k-sets – interactive explanation*](https://www.heyprof.app/en/demo/halbierende-geraden) (heyprof, undated). Interactive exposition illustrating halving lines and rotating-line switches, comparing counts with Dey's bound, and discussing family 183's claimed exponent improvement with unspecified constants. [family-level]

## News and blogs
- None found.
