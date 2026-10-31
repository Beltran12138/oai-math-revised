# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-30.

## Follow-up works
- [Elena I. Bunina, Winston Lee, Alexei Miasnikov, Kyrylo Muliarchyk, *Failure of direct finiteness for group algebras in every odd characteristic*](https://arxiv.org/abs/2610.22536) (arXiv:2610.22536, 2026-10-15). Claims failure of direct finiteness for every odd prime, with witnesses over $\mathbb F_p$ and finitely presented $G_p$, by a different construction; it cites this preprint as covering one specified prime over a field of order $p^4$ using torsion. The authors state that "OpenAI's ChatGPT was used extensively for mathematical exploration".

## Comments and discussion
- [MathWorld (Wolfram), *Kaplansky Direct-Finiteness Conjecture*](https://mathworld.wolfram.com/KaplanskyDirect-FinitenessConjecture.html) (updated 2026-10-30). Reports the Bunina et al. all-odd-primes claim and says its inputs from unnamed "earlier OpenAI manuscripts" "have not been independently verified here", so the refutation is not treated as established.

## Formalization
- [OpenAI, *Lean scope note for family 197* (`lean/docs/197.md`)](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/197.md) (openai/math release, 2026-10-06). States that the formalization constructs the field of order $p^4$, a finitely generated group with torsion and $a,b$ with $ab=1\ne ba$. It also covers the injective, non-surjective map on $K^G$ and some fixed-field transfer results.
- [mo271, KevorkianPhilippe and others, *Wikipedia/SurjunctiveGroup: `gottschalk_surjunctivity_conjecture` is false*](https://github.com/google-deepmind/formal-conjectures/issues/6919) (formal-conjectures issue #6919, 2026-10-07 to 2026-10-19). Notes that the release's Lean proof for this preprint covers injectivity and non-surjectivity of the automaton only as a plain map. A commenter supplied a separate Lean bridge for continuity and shift-equivariance on top of the odd-characteristic main theorem; the resulting group is finitely generated, not necessarily finitely presented.
- [KevorkianPhilippe, *fix(Wikipedia/SurjunctiveGroup): `gottschalk_surjunctivity_conjecture` is false*](https://github.com/google-deepmind/formal-conjectures/pull/7440) (formal-conjectures PR #7440, merged 2026-10-19). Restates Gottschalk's conjecture as false, linking `OAI.OddKaplansky.main_theorem` and noting that continuity and shift-equivariance are not part of the linked proof; the approving reviewer (bocowgill) says they checked the non-surjunctivity conclusions (Section 8) and "relied on the reported build and axiom checks without independently rerunning the external proof."
- [The Formal Conjectures Authors, *Gottschalk’s surjunctivity conjecture — SurjunctiveGroup.lean*](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/Wikipedia/SurjunctiveGroup.lean) (GitHub, accessed 21 October 2026). This Lean statement file cites both characteristic companions but retains `sorry` in the counterexample declarations and notes that the linked odd-characteristic proof omits continuity and shift equivariance. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [Michal Doucha, Jakub Gismatullin, *On dual surjunctivity and applications*](https://arxiv.org/abs/2008.10565) (arXiv:2008.10565, 2020). Proves that dual surjunctive groups satisfy direct finiteness over all fields of positive characteristic, so Theorem 1.1 would also imply that $G$ is not dual surjunctive; complements the cellular-automaton consequence in Section 8.
- [OpenAI, *Ten Advances in Mathematics and Theoretical Computer Science*, Chapter 3 "Nonsofic groups exist"](https://cdn.openai.com/pdf/ten-proofs-oai.pdf) (OpenAI, updated 2026-08-06). An earlier claimed explicit nonsofic group; context for the introduction's remark that the group $G$ cannot be sofic.
- [Ken Dykema, Timo Heister, Kate Juschenko, *Finitely presented groups related to Kaplansky's Direct Finiteness Conjecture*](https://arxiv.org/abs/1112.1790) (arXiv:1112.1790, 2011). Finitely presented groups that are universal for one-sided inverses in group rings; may be compared with the finitely generated group of Theorem 1.1. Not in this preprint's bibliography.
- [Brandon Seward, *Krieger’s finite generator theorem for actions of countable groups II*](https://arxiv.org/abs/1501.03367) (arXiv:1501.03367, 2015; revised 2019). Its conditional implication from positive Rokhlin entropy for free ergodic actions of every countable group to surjunctivity and direct finiteness provides context for this paper’s claimed counterexample. [family-level]

## Digests and expositions
- [Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*](https://arxiv.org/html/2610.17090v1) (arXiv:2610.17090, 2026-10-12). The card for family 197 (Section 8.4.2) mainly covers the characteristic-two construction and says the repository formalizes this odd-characteristic companion; per the paper, the first extraction for each family used AI readings. [family-level]
- [AI Proved What?, *One-sided inverse? Kaplansky’s direct-finiteness conjecture*](https://aiprovedwhat.com/episodes/197-torsion-free-group-algebra-not/) (Episode 197, October 2026). This illustrated exposition compares all four papers, explains their construction ideas, and distinguishes their claims and formalization scope. [AI-generated per source] [family-level]

## News and blogs
- [Kingy.ai, *OpenAI's 722 Math Manuscripts: The Results, Proofs, Compute and Costs*](https://kingy.ai/blog/openai-math-722-manuscripts-results-proofs-compute-costs/) (October 2026). Discusses family 197 and contrasts the torsion-free headline with the Lean scope page, which covers the characteristic-two and odd-characteristic constructions with torsion. [family-level]
