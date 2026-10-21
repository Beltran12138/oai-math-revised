# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Sudais Arif, *A Factor-Two Lower Bound for Complementing Two-Way Deterministic Finite Automata*](https://arxiv.org/html/2610.18897) (arXiv:2610.18897, 10 Oct 2026). Cites this paper and its companion in its related-work paragraph for related descriptions of interval behavior, and states that "those papers concern different state-complexity questions"; the acknowledgments say the work was developed with assistance from an OpenAI model. [family-level]

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 129: Exponential state costs for two-way automata*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/129.md) (lean/docs/129.md, October 2026). Describes the release's Lean formalization of the bound $2^{\lfloor(h-2)/31\rfloor}\le4(s+2)^2$ for every $h\ge2$ under both acceptance conventions; this paragraph follows a sentence excluding the one-way-liveness result from scope. [family-level]
- [OpenAI, *OneWayLiveness.lean*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/ComparatorChallenges/OneWayLiveness.lean) (OpenAI Math Release comparator statement, 2026). This file defines relation-product liveness and both finite-run acceptance conventions and states the small-source/exponential-target theorem, with its proof represented by a `sorry` placeholder.

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Juraj Hromkovič and Georg Schnitger, *Nondeterminism versus Determinism for Two-Way Finite Automata: Generalizations of Sipser's Separation*](https://www.springerprofessional.de/nondeterminism-versus-determinism-for-two-way-finite-automata-ge/13523406) (ICALP 2003, doi:10.1007/3-540-45061-0_36). Extends Sipser's sweeping separation to oblivious 2DFAs and to 2DFAs with $o(n)$ non-obliviousness, adding to the paper's survey of earlier exponential bounds against restricted deterministic targets.
- [Giovanni Pighizzini, *Two-Way Finite Automata: Old and Recent Results*](https://arxiv.org/abs/1208.2755) (arXiv:1208.2755, EPTCS 90, 2012). Survey of partial results on the Sakoda–Sipser question, which the paper's main theorem addresses over growing alphabets.

## Digests and expositions
- [Gradient Damage, *Weisfeiler–Leman Refinement, PCP for PPAD and 8 More in Theoretical Computer Science*](https://gradientdamage.com/videos/weisfeiler-leman-refinement-pcp-for-ppad-and-8-more-in-theoretical/) (video, 2026-10-15). The chapter beginning at 2:03 introduces the Sakoda–Sipser simulation question and links this paper; the source describes the animations as illustrations rather than proofs.

## News and blogs
- None found.
