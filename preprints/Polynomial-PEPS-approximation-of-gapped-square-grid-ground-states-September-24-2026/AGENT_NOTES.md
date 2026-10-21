# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- None found.

## Expert comments and discussion
- None found.

## Formalization
- [LionSR/TNLean, *Tracking: polynomial PEPS approximation of gapped square-grid ground states* (issue #8736)](https://github.com/LionSR/TNLean/issues/8736) (GitHub, opened 7 Oct 2026, closed 18 Oct 2026). The maintainer's closing comment reports Theorem 1.1 as `TNLean.PEPS.Approximation.polynomialPEPSApproximation`, using only the standard axioms. An earlier comment (17 Oct) listed three requirements of Proposition 7.1 that the work then in progress had not yet established.
- [TNLean contributors, *Polynomial PEPS approximation of gapped square-grid ground states*](https://sirui-lu.com/TNLean/blueprint/ch-peps_approximation.html) (formalization blueprint, accessed 2026-10-21). This chapter links Lean declarations for the paper’s distribution, column-selection and dyadic-routing arguments, explicitly separating intermediate hypotheses from their verification elsewhere in the development. [AI-generated per source]
- [TNLean, *Product-Reference Estimates and a Column on the Open Square*](https://sirui-lu.com/TNLean/paper-gaps/polypeps_product_reference_column.pdf) (formalization scope note, 2026-10-13; marked resolved 2026-10-17). The note explains the formal passage from product-reference and density-compression estimates to column extraction and routing on the original open square.
- [hz-xiaxz in LionSR/TNLean, *Formalize the two-dimensional area law and polynomial PEPS approximation from a global spectral gap* (issue #8732)](https://github.com/LionSR/TNLean/issues/8732) (GitHub, 7 Oct 2026). Proposes the formalization and states that the Lean code in the OpenAI release proves neither headline theorem. [family-level]
- [TNLean contributors, *Tensor-network theory, formalized in Lean 4*](https://github.com/LionSR/TNLean) (Lean 4 repository, accessed 2026-10-21). The repository hosting the family-specific formal developments describes a predominantly agent-produced formalization workflow and notes that some library results remain unfinished or assumed as axioms. [AI-generated per source] [family-level]
- [LionSR/QICLean, *doc(paper-gaps): update the area-law and PEPS gap notes after the TNLean proofs* (PR #856)](https://github.com/LionSR/QICLean/pull/856) (GitHub, merged 18 Oct 2026). Updates three "paper-gap" notes on the area-law and PEPS manuscripts to resolved status, citing `polynomialPEPSApproximation` and `adaptivePatchConstraint` (Proposition 4.1). [family-level]
- [LionSR/TNLean, *Tracking: explicit constants in the area law and the polynomial PEPS approximation* (issue #9638)](https://github.com/LionSR/TNLean/issues/9638) (GitHub, opened 18 Oct 2026, closed). Aims to make the constants C, c of Theorem 1.1 explicit; the thread records candidate values, some of them marked heuristic or unverified. [family-level]
- [LionSR/TNLean, *Tracking: polynomial PEPS approximation for interactions of range R* (issue #9641)](https://github.com/LionSR/TNLean/issues/9641) (GitHub, opened 18 Oct 2026, open). Targets an extension of Theorem 1.1 from nearest-neighbour to range-R interactions, explicitly described as "an extension of the source, not a source theorem"; it was in progress at collection time.
- [LionSR/TNLean, *Matrix product state approximation of gapped chains by the protocol route of the polynomial PEPS paper* (issue #9555)](https://github.com/LionSR/TNLean/issues/9555) (GitHub, 16 Oct 2026, open). Proposes a one-dimensional analogue of this paper's distributed-protocol construction, giving polynomial-bond-dimension MPS approximations of gapped chain ground states.

## Related prior literature mentioned by others
- [J. Ignacio Cirac, José Garre-Rubio and David Pérez-García, *Mathematical open problems in Projected Entangled Pair States*](https://arxiv.org/abs/1903.09439) (arXiv:1903.09439; Revista Matemática Complutense, 2019). Identified by VibeMathed as prior context: the survey's Questions 7–8 on polynomial-bond-dimension approximation relate to the manuscript’s open-square theorem.

## Possibly relevant literature (found by the agent, not checked)
- [Yichen Huang, *Two-dimensional local Hamiltonian problem with area laws is QMA-complete*](https://arxiv.org/abs/1411.6614) (J. Comput. Phys. 443, 110534 (2021)). Relevant to the paper's remark that Theorem 1.1 is an existence statement with no efficient construction or contraction, since it shows that 2D area-law ground states need not have efficient classical descriptions unless MA = QMA; it is not in the bibliography.
- [Tomotaka Kuwahara, *The Rényi area law conjecture is false below α=1 in high dimensions*](https://arxiv.org/abs/2610.15199) (arXiv:2610.15199, Oct 2026). Constructs uniformly gapped 2D ground states that violate a Rényi-α area law for every α<1, which bears on the paper's discussion of Huang's PEPS result assuming such a Rényi area law (Section 1.2).

## Digests and expositions
- None found.

## News and blogs
- [Azmat, *2D Area Law: How OpenAI’s Proof Connects the Global Gap to Entanglement*](https://binaryverseai.com/2d-area-law-openai-global-spectral-gap-proof/) (Binary Verse AI, 2026-10-13). This exposition outlines the proposed area-law argument and distinguishes the companion’s polynomial-bond PEPS existence claim from efficient tensor construction or contraction. [family-level]
