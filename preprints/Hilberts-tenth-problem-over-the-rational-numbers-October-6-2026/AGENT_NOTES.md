# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Zhi-Wei Sun, *86 unknowns for Hilbert's tenth problem over the rationals*](https://arxiv.org/abs/2610.20691) (arXiv:2610.20691, v1 14 Oct 2026, v2 19 Oct 2026). Starting from this paper's negative answer, it proves undecidability for polynomials in 86 rational unknowns, using this paper's Theorem 2.4, Corollary 2.5 and Sections 3.2, 5 and 6.1.

## Expert comments and discussion
- [Persiflage (galoisrepresentations.org), *A Brief Digest of Some New OpenAI Results*, item 3](https://galoisrepresentations.org/2026/10/08/a-brief-digest-of-some-new-openai-results/) (blog post, 8 Oct 2026). The blogger writes that the result "threw me for a loop", distinguishes it from existential definability of ℤ in ℚ, and raises the separate question of decidability for curves; the post also notes the Fontaine–Mazur-at-2 paper as an input to the proof.
- [Maarten Derickx, comment on the Persiflage digest](https://galoisrepresentations.org/2026/10/08/a-brief-digest-of-some-new-openai-results/#comment-28555) (blog comment, 10 Oct 2026). Pointing to a post by Jennifer Park, the comment says: "Apparently, they cite her work in a completely wrong way!"; a reply ([comment-28569](https://galoisrepresentations.org/2026/10/08/a-brief-digest-of-some-new-openai-results/#comment-28569)) answers that the point does not seem cogent and the proof's ideas need to be studied.
- [Felipe Voloch, comment on the Persiflage digest](https://galoisrepresentations.org/2026/10/08/a-brief-digest-of-some-new-openai-results/#comment-28562) (blog comment, 11 Oct 2026). On the curve case, it lists conjectural routes to decidability: ABC/Vojta with explicit constants, Tate + Hodge + Fontaine–Mazur (conditional algorithmic Mordell), and finiteness of Sha in genus one.

## Formalization
- [j2d9w5xtjn-png and reviewers, *feat: add Hilbert's 10th problem over ℚ*](https://github.com/google-deepmind/formal-conjectures/pull/5391) (google-deepmind/formal-conjectures PR #5391, opened 9 Sep 2026, open). A statement-only Lean formalization of the problem, with the ℚ case tagged `research open`; a 9 Oct 2026 review comment asks whether that tag is still appropriate given this preprint.

## Related prior literature mentioned by others
- [Levent Alpöge and Brian Lawrence, *Conditional algorithmic Mordell*](https://arxiv.org/abs/2408.11653) (arXiv:2408.11653, Aug 2024). Cited by Felipe Voloch in the Persiflage thread; it gives an algorithm for rational points on hyperbolic curves whose termination follows from the Hodge, Tate and Fontaine–Mazur conjectures, relevant to the curve case this paper leaves open.
- [Jonas Bayer, Marco David, Benedikt Stock, Abhik Pal, Yuri Matiyasevich, and Dierk Schleicher, *Diophantine Equations and the DPRM Theorem*](https://isa-afp.org/entries/DPRM_Theorem.html) (Archive of Formal Proofs, 2022-06-06). Cited in Yiping Deng's exposition as an Isabelle formalization of the classical integer undecidability theorem underlying the reduction.

## Possibly relevant literature (found by the agent, not checked)
- [Kirsten Eisenträger and Graham Everest, *Descent on elliptic curves and Hilbert's tenth problem*](https://arxiv.org/abs/0707.1485) (arXiv:0707.1485, Proc. AMS). It uses isogeny descent to construct complementary subrings of ℚ with undecidable Hilbert's tenth problem, relating to the introduction's discussion of Poonen's large subrings ℤ[S⁻¹]; not in the bibliography.
- [Peter Koymans and Carlo Pagano, *Hilbert's tenth problem for finitely generated rings*](https://arxiv.org/abs/2602.04468) (arXiv:2602.04468, Feb 2026). An expository account of the number-field and finitely-generated-ring results that the introduction contrasts with ℚ; the bibliography cites the research article but not this survey.

## Digests and expositions
- [Yiping Deng, *Hilbert’s tenth: from machines to equations, and a new rational-case claim*](https://loudcoder.com/blog/hilberts-tenth-from-machines-to-rationals/) (Loudcoder, 2026-10-07). Explains the finite-test Turing reduction, compactness and elliptic-height argument, and the pointwise 2-converse dependency, explicitly distinguishing exposition from verification. [cites earlier version] [family-level]
- [AI Proved What?, *No algorithm for fractions: Hilbert’s tenth problem over the rational numbers*](https://aiprovedwhat.com/episodes/004-hilberts-tenth-problem-q/) (Episode 004, October 2026; status updated 2026-10-19). An animated exposition and transcript covering the claim, its finite-test strategy, and the companion's role in obtaining rational points from 2-descent. [AI-generated per source] [family-level]

## News and blogs
- [Peter Hall and Joseph Howlett, *The most exciting claims from OpenAI's heap of new proofs*](https://www.scientificamerican.com/article/the-most-exciting-claims-from-openais-heap-of-new-proofs/) (Scientific American, 8 Oct 2026). Describes the negative answer over ℚ among the release's highlights and quotes Hector Pasten: "It's extremely surprising to me that they connect … Their general strategy is original."
- [Bill Gasarch, *Conjecture that I thought would not be solved in my lifetime....were*](https://blog.computationalcomplexity.org/2026/10/conjecture-that-i-thought-would-not-be.html) (Computational Complexity blog, 11 Oct 2026). Compares the claimed undecidability over ℚ with the known cases ℤ, ℝ and ℂ and notes the proof has not been Lean-formalized.
