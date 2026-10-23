# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-23.

## Follow-up works
- [Manjul Bhargava, *Every nonsquare integer not equal to −1 is a primitive root modulo a positive lower density of primes*](https://hexagonmath.org/abs/2610.00228v1) (hexagon:2610.00228v1, 2026-10-14). Upgrades the conclusion to a positive lower density of primes, assuming a zero-free half-plane $\Re s>1-1/N$ for all Dedekind zeta functions (supplied, per the abstract, by the Cureton–Thorner result); it uses this paper's marked replacement proposition (Lemma 10.2, Proposition 10.3), the proof of Lemma 12.1 and Sections 11–12; the provenance statement reports contributions by GPT-6 and a Lean check of the deductions only, with the cited theorems kept as explicit hypotheses.
- [Manjul Bhargava, *Rational points on elliptic curves that are primitive modulo a positive proportion of primes*](https://hexagonmath.org/abs/2610.00294v1) (hexagon:2610.00294v1, 2026-10-17). Proves a Lang–Trotter-type positive lower density for $P=(2,2)$ on $y^2=x^3-2x$, citing this paper (Lemma 10.2, Proposition 10.3, Section 12, at a pinned commit) for its marked Type II input; the provenance statement reports GPT-6 contributions and partial Lean formalization.
- [Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind zeta functions*](https://hexagonmath.org/abs/2610.00200v2) (hexagon:2610.00200v2, 2026-10-12). Claims that every Dedekind zeta function is zero-free in $\Re s>31/32$, following the strategy of this paper's zero-free theorem for finite-order Hecke $L$-functions over cyclotomic fields containing $\mu_{12}$ (cited as reference 30); the abstract states the results were formalized in Lean using AxiomProver. [AI-generated per source]
- [Boyang Hu, *A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/abs/2610.00216v1) (hexagon:2610.00216v1, 2026-10-13). Claims a zero-free half-plane $\Re s>7/8$ for $L$-functions of unitary representations of the Weil group; the provenance statement says the work grew out of AI-assisted investigations of this paper's Hecke zero-free arguments, and the paper cites it as reference 17. [AI-generated per source]
- [OpenAI, *Deterministic Polynomial Factorization over Prime Fields*](https://github.com/openai/math/tree/main/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026) (OpenAI Math Release preprint, 2026-10-04). Another release manuscript, which the VibeMathed entry for it describes as depending on this paper's Theorem 1.2 (uniform Hecke zero-free strip over cyclotomic fields). [AI-generated per source]

## Comments and discussion
- [Persiflage (galoisrepresentations.org), *A Brief Digest of Some New OpenAI Results*](https://galoisrepresentations.org/2026/10/08/a-brief-digest-of-some-new-openai-results/) (blog, 2026-10-08). Item 4 discusses this paper: Hooley's argument would need quasi-RH for Dedekind $L$-functions, so the paper takes a different route, which the post calls "a little bit different, but also not at all surprising"; in the comments (2026-10-09) DH points to the paper's more general quasi-RH for Hecke characters of cyclotomic fields, and Persiflage replies that Hooley's argument "needs full GRH for these".
- [Christopher D. Long (@octonion), post on X](https://x.com/octonion/status/2110222443646177608) (2026-10-14). A two-post thread presenting the paper as "another consequence of the QRH" proving Artin's conjecture, and noting the conjecture dates from 1927 and "had been open for 99 years".
- [Almost Sure (@Almost_Sure), post on X](https://x.com/Almost_Sure/status/2110364679075942637) (2026-10-14). Contrasts this paper with a linked work "claiming a positive lower density of primes", calling that claim, if true, "significantly stronger" than this result.
- [Go Big or Go Home (@AmericaGetBig), post on X](https://x.com/AmericaGetBig/status/2110346460470649038) (2026-10-14). Notes that Hooley obtained both infinitude and the exact density on GRH in 1967 and asks: "Does the QRH route recover the full density, or just infinitude?"
- [Sendtoshi Profimoto (@profimoto), post on X](https://x.com/profimoto/status/2108363265264734544) (2026-10-09). Part of a thread summarizing the method as building primes with $p-1=2\cdot r\cdot Q$, $Q$ a prime above $x^{0.9}$, "plus a uniform zero-free strip for Hecke L-functions of cyclotomic fields", and suggesting the engine does not need an integer base.

## Formalization
- [Yao Xu (cadamcat), *artin-primitive-roots-lean4*](https://github.com/cadamcat/artin-primitive-roots-lean4) (GitHub, 2026). An independent Lean 4 project that follows this paper, with Lean theorems for the controlled-predecessor construction, uniform splitting and the Hecke zero-free region, and a main theorem stating that the set of primes with primitive root $a$ is infinite; the README says it was developed with AI assistance, that it is kernel-checked using only the standard axioms, and that it depends on pinned external libraries including openai/math.
- [Axiom Math, Dean Cureton and Jesse Thorner, *Dedekind Zeta Zero-Free Region*](https://github.com/AxiomMath/DedekindZetaZeroFree) (Lean 4 repository, October 2026). Reports formalizations of the Dedekind zeta nonvanishing theorem for Re(s)>31/32 and its finite-order Hecke corollary, covering a stronger version of the family's analytic input rather than either primitive-root counting theorem. [AI-generated per source] [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [M. Ram Murty and Sunil Naik, *A non-abelian large sieve and Artin's primitive root conjecture*](https://arxiv.org/abs/2608.21573) (arXiv:2608.21573, 2026-08-21). Derives Artin's conjecture for a fixed base from a conjectural non-abelian large sieve inequality, an alternative conditional route to the infinitude statement in Theorem 1.1.
- [Pieter Moree, *Artin's primitive root conjecture – a survey*](https://arxiv.org/abs/math/0412262) (arXiv:math/0412262, v2 2012). A survey of the history and results behind Artin's conjecture, covering the conditional and unconditional results summarized in the paper's historical section (Hooley, Gupta–Murty, Heath-Brown, averages over the base).

## Digests and expositions
- None found.

## News and blogs
- [Scientific American, *The most exciting claims from OpenAI's heap of new proofs*](https://www.scientificamerican.com/article/the-most-exciting-claims-from-openais-heap-of-new-proofs/) (Scientific American, 2026-10-08). Lists "Artin's conjecture on primitive roots" among the important number theory results in the release, without further discussion.
