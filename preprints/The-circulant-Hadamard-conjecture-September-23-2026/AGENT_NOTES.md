# Automatically collected context

Collected by an AI agent (Claude Opus 5.5) on 2026-10-20. Not reviewed by a human; may be incomplete or wrong. Corrections: open an issue.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI, *Lean scope note for family 179*](https://github.com/openai/math/blob/main/lean/docs/179.md) (openai/math release, 2026-10-06). The release's own Lean formalization covers the classification of circulant Hadamard orders (exactly 1 and 4) and the even-length Barker case; the odd-length Barker classification is stated to be outside its scope.
- [mo271 et al., *feat: mark problems solved in the OpenAI math release and link formal proofs*](https://github.com/google-deepmind/formal-conjectures/pull/6898) (google-deepmind/formal-conjectures PR #6898, merged 2026-10-11). Marks `CirculantHadamard.circulant_hadamard_conjecture` as solved and links the release's Lean theorem `OAI.CirculantHadamard.exists_iff_order_one_or_four`, absorbing the change proposed in PR #6897.
- [anxkhn, *fix(Arxiv/CirculantHadamard): link the OpenAI formal proof*](https://github.com/google-deepmind/formal-conjectures/pull/6897) (formal-conjectures PR #6897 and [issue #6896](https://github.com/google-deepmind/formal-conjectures/issues/6896), 2026-10-07). Supplies a Lean bridge from the release theorem to the repository's `n ≤ 4` statement; a reviewer (bocowgill) reports re-checking the implication conditional on the external theorem, and the author notes a sandboxed Comparator run was still outstanding.
- [mo271, *Arxiv/2104.00502/BarkerSequence: `barker_conjecture` is true*](https://github.com/google-deepmind/formal-conjectures/issues/6917) (formal-conjectures issue #6917, opened 2026-10-07, open). Proposes marking the Barker conjecture solved and notes that only the even-length case is formalized in the release, the odd-length classification being in the paper only.
- [JD Jones, *Barker sequences of odd length have length 1, 3, 5, 7, 11 or 13*](https://github.com/JD-Jones-ASES/ob-lean) (GitHub ob-lean; Palomar entry [PALOMAR-2026-10-19-000015](https://data.palomar-registry.org/entries/PALOMAR-2026-10-19-000015-v1.json), 2026-10-19). Formalizes the Schmidt–Willms odd-length Barker classification in Lean and, taking the release's even-length theorem as an explicit hypothesis, derives the full list of Barker lengths conditionally.

## Related prior literature mentioned by others
- [nellore and a co-author (community fork), *add references to the circulant Hadamard write-up*](https://github.com/mathcommunity/oai-math-revised/pull/1) (mathcommunity/oai-math-revised PR #1, merged 2026-10-18). Adds a paragraph and references (including Johnsen 1964 and Brualdi 1965) on the early settlement of the symmetric circulant case.
- [Jürgen Willms, *Counterexamples to Theorem 1 of Turyn's and Storer's Paper "On Binary Sequences"*](https://arxiv.org/abs/1404.4833) (arXiv:1404.4833, 2014). Cited in the ob-lean README as showing that Turyn–Storer's original odd-length argument relies on an incorrect lemma; the manuscript cites Turyn–Storer for odd-length nonexistence and uses the Schmidt–Willms proof for the exact list.

## Possibly relevant literature (found by the agent, not checked)
- [Barry Hurley, Paul Hurley, Ted Hurley, *The Hadamard circulant conjecture*](https://arxiv.org/abs/1109.0748) (arXiv:1109.0748, 2011). An earlier claimed proof of the same conjecture, not among the claimed proofs listed in the manuscript's bibliography.
- [Peter Borwein, Michael J. Mossinghoff, *Wieferich pairs and Barker sequences, II*](https://arxiv.org/abs/1306.0045) (LMS J. Comput. Math., 2014; arXiv:1306.0045). Computational lower bounds and candidate lengths for long Barker sequences, which the manuscript's Barker corollary would supersede.

## Coverage
- [Emergent Mind, *OpenAI Math Explorer: result 179*](https://www.emergentmind.com/openai-math-explorer/results/179) (catalogue page, October 2026). Third-party catalogue entry with an AI-generated explainer and links to the manuscript and Lean files.
- [lance.fortnow.com (no author named), *OpenAI Math: TCS Selection*](https://lance.fortnow.com/openai-math-tcs.htm) (2026-10-15). Curated catalogue that lists family 179 among combinatorics results.
