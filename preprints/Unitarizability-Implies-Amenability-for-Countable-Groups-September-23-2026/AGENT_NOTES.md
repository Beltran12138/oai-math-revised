# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note 251: Amenability, unitarizability, and strong Ulam stability*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/251.md) (lean/docs/251.md, October 2026). The release's Lean scope note states that the formalization proves amenability ⇔ unitarizability for every discrete group and gives nonunitarizable representations with bound at most 1+ε, with comparator statements `DixmierAllDiscrete.lean` and `Dixmier.lean` (the latter a separable witness with bound 101 for countable groups). [AI-generated per source]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [F. Khosravi and S.-G. Youn, *Non-unitarizable representations of compact and discrete quantum groups*](https://arxiv.org/abs/2608.27737) (arXiv:2608.27737, 27 August 2026). Constructs non-unitarizable representations of quantum groups with norms close to 1 and proves a quantum analogue of the lifting principle, which may be compared with the paper's 1+ε bound (Theorem 1.1) and its induction step from subgroups.

## Digests and expositions
- [Vadim Alekseev, *A geometric account of the solution to the Dixmier unitarisability problem*](https://github.com/certusoid/unitarisability-and-amenability) (GitHub note, 8 October 2026). A re-exposition of this paper's proof via a positive divergence flow on a non-amenable group, replacing the randomized Markov-operator construction by one coming from free groups and recording a remark, credited to Alon Dogon, that non-amenable groups are not deformation rigid; the note states it was developed through interaction with an AI model ("GPT-6 Astra") and edited by the author ([TeX source](https://raw.githubusercontent.com/certusoid/unitarisability-and-amenability/main/unitarisability-and-amenability.tex)).
- [Claude Opus 5.5 / Open Mathematics Courses, *Amenability and unitarizability*](https://kokunoyumeto.github.io/open-math-courses-public/courses/amenability-and-unitarizability/) (online course, undated). Four lessons with exercises present the manuscript's route through contracting averages, sparse edge assignments, random sign frames and the operator-cocycle obstruction; the source describes the course as self-checked with independent review incomplete. [AI-generated per source]

## News and blogs
- [Carlos Toledo, *OpenAI's math release: what it claims beyond what it checks*](https://carlostoledo.co/reports/openai-math.html) (cert-machine audit of release commit fd4aeeb2, 10 October 2026). The audit lists family 251's strong Ulam stability assertion among claims from manuscripts not linked by their family's Lean scope note, distinguishing that assertion from the unitarizability formalization. [AI-generated per source] [family-level]
