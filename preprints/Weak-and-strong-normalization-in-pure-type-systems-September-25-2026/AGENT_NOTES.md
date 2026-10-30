# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Ankit Pradhan, Cole Vick, Ruijie Fang, Carl Kwan, *Weak and strong βη-normalization in pure type systems with βη-conversion*](https://github.com/localmotiveproofs/PTS-beta-eta) (Lean repository, first commit 2026-10-24, latest 2026-10-27; no paper). Adapts this paper's proof to Geuvers' PTS_βη, the case the paper leaves aside, stating that weak βη-normalization, and also weak β-normalization, implies strong βη-normalization for every specification; the system with a strengthening rule and Geuvers' Conjecture 8.1.3 are stated as not proved. The development reuses OpenAI's Lean files for the β case and was checked by the kernels nanoda and con-ron according to Palomar (record PALOMAR-2026-10-27-000027 v1), with the review recorded as self-assessed and no outside reviewer of statement or proof. [AI-generated per source]

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note for family 245: Weak normalization implies strong normalization in pure type systems*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/245.md) (lean/docs/245.md; original at [openai/math commit adc7f12](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/245.md)). The scope note says the Lean development proves the β-Barendregt–Geuvers–Klop implication with reduction inside annotations and arbitrary, possibly nonfunctional, axioms and rules, and links the comparator statement `ComparatorChallenges/TypeSystemNormalization.lean`. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [M. H. Sørensen (submitter), *TLCA List of Open Problems, Problem #9: Is every weakly normalizing PTS also strongly normalizing?*](https://tlca.di.unito.it/opltlca/opltlcasu16.html) (TLCA open problems list). Standard open-problem record of the conjecture addressed by Theorem 1, noting that Barthe's K-conjecture follows from it for functional PTSs (Barthe 1998); neither is cited in the paper's bibliography.
- [P.-A. Melliès and B. Werner, *A generic normalisation proof for pure type systems*](https://researchportal.ip-paris.fr/en/publications/a-generic-normalisation-proof-for-pure-type-systems/) (TYPES 1996, LNCS 1512, 1998). A generic reducibility-style strong normalisation proof for arbitrary PTSs assuming suitable Λ-sets for each sort, bearing on the paper's Tait–Girard candidate construction indexed by sort profiles.
- [Sebastián Urciuoli, *A Machine-checked Proof of Consistency for Impredicative Pure Type Systems*](https://arxiv.org/abs/2607.20188) (arXiv:2607.20188; EPTCS 449, 2026-07-22). Its Agda formalizations of β-confluence and subject reduction for pure type systems may provide a comparison for the corresponding metatheoretic lemmas in Section 2 of the paper.

## Digests and expositions
- [AI Proved What?, *If every program can finish, must it?*](https://aiprovedwhat.com/episodes/245-wn-implies-sn-pure-type-systems/) (episode 245, October 2026). Provides a video and transcript explaining the system-wide hypothesis, the restriction to β-reduction, and the proposed proof through sort profiles and exclusion of a paradox-supporting configuration. [AI-generated per source] [family-level]
- [Ankit Pradhan, Cole Vick, Ruijie Fang and Carl Kwan, *A visual guide to the proof of the βη-Barendregt–Geuvers–Klop conjectures*](https://github.com/localmotiveproofs/PTS-beta-eta/blob/main/guide/proof-map.pdf) (GitHub manuscript, accessed 2026-10-30). Explains OpenAI's β proof through recursion over strongly connected components of a signed sort-profile graph, illustrates the candidate constructions and typed paradox with examples linked to Lean declarations, and describes the changes needed for βη-conversion. [family-level]

## News and blogs
- None found.
