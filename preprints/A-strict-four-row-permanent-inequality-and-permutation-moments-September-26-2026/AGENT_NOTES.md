# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [J. D. Jones, *Sharp robustness and stability of the four-row permanent inequality*](https://palomar-registry.org/entry?id=PALOMAR-2026-10-08-000007&version=1) (Palomar PALOMAR-2026-10-08-000007, registered 8 Oct 2026; code at [JD-Jones-ASES/four-row](https://github.com/JD-Jones-ASES/four-row)). A Lean development that the registry marks as adapting this paper; it claims the sharp total-variation radius 1/24 and optimal variance-deficit coefficient (1−24r)/9 for balanced laws, and its [disclosure](https://github.com/JD-Jones-ASES/four-row/blob/main/DISCLOSURE.md) says OpenAI models contributed and the review status is agent-reviewed. [AI-generated per source]

## Expert comments and discussion
- None found.

## Formalization
- [OpenAI math release, *Lean scope notes for family 238*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/238.md) (lean/docs/238.md, 2026). States that the strict four-row permanent inequality (some 4/3<p<2 and ε>0, laws on S₄ ε-close to uniform with uniform marginals) is formalized in FourRowPermanent.lean; the Thorp mixing consequence is outside the scope. [family-level]

## Related prior literature mentioned by others
- None found.

## Possibly relevant literature (found by the agent, not checked)
- [B. Roos, *Generalization of a Hadamard type inequality for permanents*](https://arxiv.org/abs/1709.05225) (arXiv:1709.05225; Linear Algebra Appl. 571, 2019). Extends the Carlen–Lieb–Loss permanent inequality by adapting their technique; possibly relevant to the paper's discussion of row-ℓ^p permanent bounds and to its robust four-row inequality.
- [Y. Jiang, *A subquadratic upper bound for the mixing time of the Thorp shuffle*](https://arxiv.org/abs/2610.18884) (arXiv:2610.18884, 3 Oct 2026). Independent preprint proving a full-deck bound of order d^{5/3} for N=2^d; relevant for comparison with this paper's O(log N) mixing consequence. It does not mention the release. [family-level]

## Digests and expositions
- [Latent Seminar, *Optimal logarithmic mixing of the Thorp shuffle*](https://lowrank.github.io/latent-seminar/OpenAI-Math/238-thorp-shuffle) (expository notes, 2026-10-06). Outlines all twelve manuscripts’ proof methods and formalization boundaries, explicitly disclaiming independent full-proof verification. [family-level]
- [heyprof, *Thorp shuffle: how often until the deck is random?*](https://www.heyprof.app/en/demo/thorp-mischen) (interactive exposition, undated). Illustrates the family’s full-deck mixing question with small-deck distributions, single-card marginals, and the support bound. [family-level]

## News and blogs
- None found.
