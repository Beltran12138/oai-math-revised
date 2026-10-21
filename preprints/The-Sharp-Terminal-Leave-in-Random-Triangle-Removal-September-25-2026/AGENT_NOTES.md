# Automatically collected context

Collected by an AI agent (Claude Opus 5.5 and GPT-6 Astra) on 2026-10-21.

## Follow-up works
- [Peter Keevash, *The terminal leave in random greedy hypergraph matching*](https://arxiv.org/abs/2610.20414) (arXiv:2610.20414, 14 Oct 2026). Proves that the edge count of the terminal graph of random triangle removal from $K_n$, divided by $n^{3/2}$, converges in $L^2$ to $1/(2\sqrt2)$, the same statement as Theorem 1.1 here, and extends it to any fixed strictly $k$-balanced $k$-graph; its §2 gives a triangle-case exposition of the approach (freezing the process, tree survival prediction, comparison with the finite random matching).

## Expert comments and discussion
- [Peter Keevash, "Statement on AI use and intellectual priority" in *The terminal leave in random greedy hypergraph matching*](https://arxiv.org/html/2610.20414v1) (arXiv:2610.20414v1, §1, 14 Oct 2026). Keevash writes that he shared triangle-removal ideas with ChatGPT from October 2025 and that his triangle-case solution "was essentially the same as that in the recent OpenAI sharing progress in mathematics announcement (manuscript 188)"; he asks OpenAI to clarify whether its model used his work, stating he has no direct evidence that it did.

## Formalization
- [OpenAI math release, *Lean scope note 188*](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/188.md) (release repository, 2026-10-06). The scope note says the Lean formalization proves the $L^2$ convergence of $F_n/n^{3/2}$ to $1/(2\sqrt2)$, also states convergence in probability and of the normalized expectation, and links the comparator statement `TriangleRemoval.lean`. [AI-generated per source]
- [OpenAI, *lean/OAI/Combinatorics/TriangleRemoval/Main.lean*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/TriangleRemoval/Main.lean) (openai/math, commit adc7f12, Oct 2026). The top-level Lean file states `sharp_terminal_leave_l2`, `sharp_terminal_leave_probability`, `sharp_terminal_leave_expectation` and their conjunction `sharp_terminal_leave` in namespace `OAI.SharpTerminalLeave`.
- [google-deepmind/formal-conjectures, *Issue #1984: Erdős Problem 1155*](https://github.com/google-deepmind/formal-conjectures/issues/1984) (opened 1 Feb 2026). An open request to formalize the statement of the Bollobás–Erdős random triangle-removal problem, with an unmerged related [PR #3587](https://github.com/google-deepmind/formal-conjectures/pull/3587) whose `opaque` declarations a reviewer noted are not tied to the actual process; it does not mention this paper.

## Related prior literature mentioned by others
- [Felix Joos and Marcus Kühn, *The hypergraph removal process*](https://arxiv.org/abs/2412.15039v2) (arXiv:2412.15039v2, 2025-08-03). Keevash's follow-up cites this work for approximate terminal exponents and estimates used before the final stage, complementing the release manuscript's use of its early-prefix control and sharp-constant conjecture.

## Possibly relevant literature (found by the agent, not checked)
- [Erdős Problems, *Problem #1155*](https://www.erdosproblems.com/1155) (erdosproblems.com, last edited 25 Jan 2026). Records the Bollobás–Erdős question of whether $\mathbb E f(n)\asymp n^{3/2}$ for the leave of random triangle removal, on which the paper's statement $\mathbb E F_n/n^{3/2}\to1/(2\sqrt2)$ bears directly; the entry does not mention the paper.

## Digests and expositions
- None found.

## News and blogs
- None found.
