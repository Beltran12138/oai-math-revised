# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [el Houcein el Abdalaoui, *OpenAI partially disproves Littlewood's 1961 $L^\alpha$-flat theorem*](https://arxiv.org/abs/2610.30797) (arXiv:2610.30797, 22 October 2026; LLM assistance acknowledged). Attributes to this paper a counterexample to Littlewood's 1961 theorem with hyper-lacunary coefficients $a_m=2^{2^m}$, which it says violates an assumption implicit in Littlewood's argument and so gives "a limited refutation"; the term "lacunary" does not occur in the TeX sources of the three manuscripts, and the author says the note and arXiv:2509.04212 (a contrary claim examined in this paper's Appendix A) "will be adapted or withdrawn to reflect the consolidated literature". [family-level]

## Comments and discussion
- [Thomas Bloom, *Erdős problems in the OpenAI proofs*](https://www.erdosproblems.com/forum/thread/blog:10) (erdosproblems.com blog, 8 October 2026). Lists Erdős Problem #1150 among the release's claimed results, links the ultraflat companion PDF and the comparator Lean file for this paper's Theorem 1.1, and notes that the 16-page PDF "appears to heavily rely on two other related PDFs". [family-level]
- [Erdős Problems forum, *Problem #1150 discussion thread*](https://www.erdosproblems.com/forum/thread/1150) (erdosproblems.com, comments February–August 2026). Predates the release; T. Bloom and T. Tao comment on gaps in el Abdalaoui's arXiv:2504.21499, one of the contrary nonflatness claims examined in this paper's Appendix A, and el Abdalaoui replies.

## Formalization
- [OpenAI math release, *Lean scope notes for family 076*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/076.md) (release Lean docs, October 2026). Describes the formalized upper bound $(1+\eta)\sqrt N$ at all large lengths and the finite-exponent $L^p$ flatness of one all-length family, both without effective rates.
- [OpenAI, *AsymptoticallyMinimalLittlewood.lean* (comparator statement)](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/AsymptoticallyMinimalLittlewood.lean) (openai/math, October 2026). Lean statement of Theorem 1.1; the proof is in [lean/OAI/Analysis/Littlewood/Main.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/Littlewood/Main.lean).
- [OpenAI, *LittlewoodFiniteFlatness.lean* (comparator statement)](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LittlewoodFiniteFlatness.lean) (openai/math, October 2026). Lean statement that one family of sign vectors is $L^p$-flat for every fixed $p>0$; merit factors themselves are not defined in the Lean code.
- [Google DeepMind formal-conjectures, *FormalConjectures/ErdosProblems/1150.lean*](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1150.lean) (formal-conjectures, 2026). Formal statement of Erdős Problem #1150, tagged as solved with answer "No", citing this paper and linking the OpenAI Lean proof; the statement in that file itself is closed by `sorry`.

## Related prior literature mentioned by others
- [Andrew Odlyzko, *Search for ultraflat polynomials with plus and minus one coefficients*](https://experts.umn.edu/en/publications/search-for-ultraflat-polynomials-with-plus-and-minus-one-coeffici/) (in *Connections in Discrete Mathematics*, Cambridge University Press, 2018). Flagged by the erdosproblemaday.com review as not cited by the paper; its extensive computations suggested that ultraflat ±1 polynomials do not exist and also discuss the merit factor. [AI-generated per source]
- [Paul Balister, Béla Bollobás, Robert Morris, Julian Sahasrabudhe and Marius Tiba, *Flat Littlewood polynomials exist*](https://annals.math.princeton.edu/2020/192-3/p06) (Annals of Mathematics 192, 2020). The [AI Proved What? exposition](https://aiprovedwhat.com/episodes/076-real-ultraflat-littlewood-polynomials-unbounded/) identifies this constant-factor two-sided flatness theorem as prior context for the family's stronger asymptotic claims. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [Jonathan Jedwab, Daniel J. Katz, Kai-Uwe Schmidt, *Advances in the merit factor problem for binary sequences*](https://arxiv.org/abs/1205.0626) (arXiv:1205.0626; J. Combin. Theory Ser. A 120 (2013) 882–906). Computes asymptotic merit factors of Legendre-type and skew-symmetric families; background for the merit-factor consequence in Section 8, distinct from the cited Adv. Math. paper by the same authors.

## Digests and expositions
- [Patrick White with Claude, *Erdős #1150: OpenAI ultraflat Littlewood, refereed*](https://erdosproblemaday.com/day/1150-openai-ultraflat-littlewood-refereed) (erdosproblemaday.com, 12 October 2026). Referee-style reading of the three family-076 papers by seven Claude "referee seats", which report no gap found and a local kernel replay of the release's 28-module Lean proof (axioms only `propext`, `Classical.choice`, `Quot.sound`), noting that the formal proof replaces two cited combinatorial inputs and one analytic step of the paper. [AI-generated per source] [family-level]
- [Latent Seminar, *Ultraflat Littlewood polynomials and autocorrelation*](https://lowrank.github.io/latent-seminar/OpenAI-Math/076-littlewood-ultraflatness) (6 October 2026). Explains the three claims, the merit-factor implication, stationary phase, packing, discrepancy rounding and lower-bound refinements, explicitly limiting its review to statements and proof mechanisms. [family-level]
- [AI Proved What?, *Flat with signs only? Ultraflat Littlewood polynomials and merit factors*](https://aiprovedwhat.com/episodes/076-real-ultraflat-littlewood-polynomials-unbounded/) (Episode 076, October 2026). Video and transcript explain the progression of the three manuscripts, quadratic-phase waves, rounding and the documented Lean scope. [AI-generated per source] [family-level]

## News and blogs
- None found.
