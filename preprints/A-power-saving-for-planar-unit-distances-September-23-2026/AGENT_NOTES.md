# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Codex and Claude (draft hosted by rohanarun), *A smaller generic grid in the unit-distance argument*](https://github.com/rohanarun/unit-distance-grid-refinement) (research draft, 2026-10-10). Claims a conditional reduction of the final algebraic witness from a 20×5 to an 8×4 generic grid, retaining the original generic-grid, negligible-height and private-valuation arguments as dependencies and giving no improvement or explicit value for the unit-distance exponent. [AI-generated per source]

## Comments and discussion
- [enaslund (merged by teorth), *Update Erdős unit distance bounds: lower bound 1.04317, upper bound 4/3 − ε*](https://github.com/teorth/optimizationproblems/pull/204) (teorth/optimizationproblems PR #204, opened 2 Oct 2026, merged 18 Oct 2026). Adds this preprint to the unit-distance constants table as the source of an upper exponent 4/3 − ε with ε not explicit; the PR has no review comments, and its author says Claude Opus 5.5 helped with the upper-bound update.

## Formalization
- [OpenAI math release, *Planar distinct distances and unit-distance bounds* (Lean scope notes)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/167.md) (lean/docs/167.md, October 2026). The release's scope note says the Lean development proves constants C>0 and 1≤β<4/3 with u(n)≤Cn^β for all n; one earlier sentence in the same note says the unit-distance theorem is "not included", which contradicts this. [family-level]
- [OpenAI, *PlanarUnitDistances.lean* (comparator statement)](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PlanarUnitDistances.lean) (openai/math, October 2026). Comparator file with the target statement `∃ C β : ℝ, 0 < C ∧ 1 ≤ β ∧ β < 4/3 ∧ ∀ n : ℕ, (u n : ℝ) ≤ C * n ^ β`, matching Theorem 1.1; erdosproblems.com/90 links this file as a formal proof of an O(n^{4/3−c}) bound.
- [OpenAI, *OAI/Geometry/UnitDistances/Main.lean*](https://github.com/openai/math/blob/main/lean/OAI/Geometry/UnitDistances/Main.lean) (openai/math, October 2026). Top-level file of the release's proof of `OAI.PlanarUnitDistances.main` (absolute constants C > 0 and 1 ≤ β < 4/3 with u(n) ≤ C n^β), which relies on imported results such as `counterexample_power_sequence` and `IncidenceDiagonal.impossible`.

## Related prior literature mentioned by others
- [Larry Guth, *Perspectives on the unit distance problem*](https://arxiv.org/abs/2609.10791) (arXiv:2609.10791, 2026-09-09). Cited in the Erdős Problem a Day report, this survey predates the manuscript and explains the obstacles to improving the 4/3 exponent, including comparison with incidence problems for other curves.

## Possibly relevant literature (found by the agent, not checked)
- [Steven Senger, *An incomplete attack on the upper bound of the unit distance problem*](https://arxiv.org/abs/2605.26145) (arXiv:2605.26145, 22 May 2026). A partial, self-described incomplete attempt to show that the n^{4/3} upper bound is not sharp, the question Theorem 1.1 addresses; not in the paper's bibliography.
- [Eric Naslund, *An Exponent of 1.043 for the Unit Distance Problem*](https://hexagonmath.org/2610.00016v2) (Hexagon 2610.00016v2, Oct 2026). Gives a construction lower bound with exponent 1.043171, above the Sawin exponent 1.014114 that the introduction quotes when it describes the remaining gap; not in the bibliography.

## Digests and expositions
- [Erdős Problem a Day (Patrick White with Claude), *#90: OpenAI claims the first power saving over Spencer–Szemerédi–Trotter in 42 years*](https://erdosproblemaday.com/day/90-openai-unit-distance-power-saving-refereed) (2026-10-14). Explains the reciprocal-coordinate-jump mechanism, reports two exposition issues concerning the score and full-row definitions, and records a Lean replay and external checker success in the body despite the headline's pending label. [AI-generated per source]
- [Readable Intelligence, *A power saving for planar unit distances* (readable version)](https://readable-intelligence.com/paper/a50280244b59?view=readable) (readable-intelligence.com, undated). Rewritten version of this paper; the page says its "proofs have not been independently checked." [AI-generated per source]

## News and blogs
- [Gil Kalai, *Updates: Sharing AI progress on mathematics (amazing!); and my lecture plans*](https://gilkalai.wordpress.com/2026/10/07/updates-sharing-ai-progress-on-mathematics-amazing-and-my-lecture-plans/) (Combinatorics and More, 2026-10-07). Item 8, "Distinct distances and unit distances", links this preprint's O(n^{4/3−δ}) planar unit-distance bound among the release's results and connects it to earlier posts on distance problems, within a discussion emphasizing the need for community verification.
