# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope note 071: Koebe's circle-domain conjecture*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/071.md) (lean/docs/071.md, 2026-10-06). The release's scope note says the Lean development covers Koebe's circle-domain theorem for every domain together with removable-boundary rigidity, both stated in one Comparator file. [family-level]
- [OpenAI math release, *KoebeCircleDomains.lean* (Comparator challenge)](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KoebeCircleDomains.lean) (openai/math, commit adc7f12). The Comparator statement file has two theorems: `koebe_circle_domain` (every domain in the sphere is conformally equivalent to a circle domain) and `removability_implies_rigidity`. [family-level]

## Related prior literature mentioned by others
- [Dimitrios Ntalampekos, *Uniformization problems in the plane: A survey*](https://arxiv.org/abs/2603.15098) (arXiv:2603.15098, 2026-03-16). The AI Proved What? episode points to this survey for the pre-release history of circle-domain uniformization and its associated uniqueness problem. [family-level]

## Possibly relevant literature (found by the agent, not checked)
- [C. Karafyllia, D. Ntalampekos, *Koebe uniformization, John domains, and transboundary modulus*](https://arxiv.org/abs/2609.31216) (arXiv:2609.31216, 25 Sep 2026). Posted shortly before the release, it proves Koebe's conjecture for John domains and gives a necessary and sufficient condition via Schramm's transboundary modulus, related to the paper's transboundary-type tests; the bibliography cites the same authors' Gromov-hyperbolic paper but not this one.
- [Y. Zhong, *Koebe uniformization of nondegenerate domains with bounded gap-ratio*](https://arxiv.org/abs/2408.03484) (arXiv:2408.03484, 2024-08-07). Uses transboundary extremal length to uniformize nondegenerate uncountably connected domains with bounded gap-ratio, a special case of Theorem 1.1; not in the paper's bibliography.
- [X. Wang, Y. Zhong, *Koebe uniformization for infinitely connected attracting Fatou domains*](https://arxiv.org/abs/2406.13524) (arXiv:2406.13524, 2024). Proves circle-domain uniformization for infinitely connected attracting Fatou domains of geometrically finite rational maps, a special case of Theorem 1.1; not in the paper's bibliography.

## Digests and expositions
- [Latent Seminar, *Circle-domain uniformization and removable-boundary rigidity*](https://lowrank.github.io/latent-seminar/OpenAI-Math/071-circle-domain-uniformization) (2026-10-06). This exposition outlines retained-test transfer, barriers, periodic tests, and the rigidity companion's trace estimates, explicitly disclaiming independent verification of the complete proofs. [family-level]
- [AI Proved What?, *Every hole made round? Koebe's circle-domain conjecture*](https://aiprovedwhat.com/episodes/071-koebes-circle-domain-conjecture/) (Episode 071, October 2026). This AI-assisted video and transcript explain both manuscripts, their dependence on retained tests, and the distinction between circle-domain existence and rigidity under removability. [AI-generated per source] [family-level]

## News and blogs
- [机器之心 Pro (Synced / Machine Heart), *翻完OpenAI的722篇数学手稿，我们挑出了最重的30道名题*](https://finance.sina.com.cn/tech/roll/2026-10-07/doc-iniuksyc8187559.shtml) (Sina Technology republication, 2026-10-07; [English version on 36Kr](https://eu.36kr.com/en/p/4015466508816520), 2026-10-08). This Chinese-language article includes Koebe's conjecture among its 30 selected problems, noting that OpenAI claims only the existence part and that a Lean formalization is attached.
