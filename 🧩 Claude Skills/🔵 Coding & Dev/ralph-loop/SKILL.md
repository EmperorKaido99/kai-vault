---
name: ralph-loop
description: Use when considering running a coding agent unattended in a repeated loop over many iterations (bulk migrations, ports, scaffolding greenfield projects) and want fresh context each iteration instead of one long session. Also use when asked to explain, compare, or set up a "Ralph loop" / "Ralph Wiggum technique".
license: MIT
---

# Ralph Loop

## Overview

The Ralph loop (full name: "Ralph Wiggum as a 'software engineer'") is a technique coined by Geoffrey Huntley (ghuntley.com, Jul 2025). The entire mechanism is a one-line shell loop:

```bash
while :; do cat PROMPT.md | claude-code ; done
```

The payload isn't the loop — it's the discipline it forces: **state lives in the filesystem and git history, never in an LLM's accumulating conversation context.** Every iteration is a brand-new agent process with zero memory of prior iterations. The agent re-derives "where it left off" by reading a small fixed set of Markdown files and actively re-searching the actual codebase — never by trusting a cached summary.

Nothing about the loop itself is novel ("ancient computer science concepts... while loops and exit conditions"). What travels is the convention: forced context reset + a minimal, named set of durable on-disk artifacts as the only inter-iteration memory channel.

## Before recommending this technique at all

Gate everything on one question: **can "done" for this task be checked by something that cannot lie** — a compiler, type checker, or test suite?

- Yes, and the work is greenfield/well-specified/bulk → Ralph loop is a good fit.
- No, or the codebase is existing/brownfield, or the task is security-sensitive (auth, payments), or it requires architectural judgment, or it's exploratory/diagnostic ("why is the app slow") → **do not recommend it.** Huntley himself: "There's no way in heck would I use Ralph in an existing code base," and even for greenfield work, senior engineer supervision is required throughout.

Every documented success traces back to a strong verification signal; every documented failure traces back to its absence or weakness.

## Two things share the name "Ralph" — don't conflate them

This is the single most important distinction to get right.

| | Huntley's original | Anthropic's official `ralph-loop` plugin |
|---|---|---|
| Mechanism | External bash loop; each iteration = fresh OS process | `Stop` hook inside **one continuous session** |
| Context | Resets to zero every iteration | Accumulates — ~200k tokens by iteration 20 ([issue #125](https://github.com/anthropics/claude-plugins-official/issues/125)) |
| Continuity | Git commits + `fix_plan.md` + `AGENT.md` on disk | In-session conversation history |
| Avoids context rot? | Yes — that's the whole point | No — inherits the exact failure mode the original was built to avoid |

The official plugin's own GitHub issue calls its README "misleading" on this point. **Default to teaching the original external-loop mechanics.** Mention the plugin only as a lower-friction but architecturally different alternative, and flag the tradeoff explicitly if it comes up.

## How to set one up

**File conventions** (division of labor, not a free-for-all):
- `specs/*.md` — stable ground truth, rarely changes
- `fix_plan.md` / `IMPLEMENTATION_PLAN.md` — the volatile, mutable backlog, rewritten every iteration
- `AGENT.md` / `AGENTS.md` — slow-changing operational knowledge (build/test/lint commands). Cap it around 60 lines. **Not a changelog.**
- `PROMPT.md` — the fixed instruction set, re-read verbatim every iteration

**Prompt conventions that recur across sources:**
- "Study" the codebase, not "read" it — and explicitly instruct the agent **not to assume something isn't implemented**; have it search first (subagents are good for this)
- Allow broad parallelism for exploration, but serialize build/test validation to one subagent — "up to 500 parallel subagents for all operations but only 1 subagent for build/tests"
- Forbid placeholder implementations explicitly and forcefully
- One task per loop iteration

**The loop itself**, with the guardrails below layered on:

```bash
ITERATION=0
MAX_ITERATIONS=50   # no default in the original — pick one; see Guardrails

while true; do
    [ "$MAX_ITERATIONS" -gt 0 ] && [ "$ITERATION" -ge "$MAX_ITERATIONS" ] && break
    cat "PROMPT.md" | claude -p --output-format=stream-json --verbose
    git add -A && git commit -m "ralph iteration $ITERATION" --allow-empty
    git push origin "$(git branch --show-current)"
    ITERATION=$((ITERATION + 1))
done
```

(Community scripts commonly add `--dangerously-skip-permissions` to avoid interactive approval prompts blocking an unattended run — that is a real operational tradeoff, not something to default to. Flag it to the user rather than silently including it; running fully unattended with permissions skipped is exactly the kind of irreversible-action risk this environment's own guidance warns about.)

## Guardrails — the original had none; use the hardened version

Huntley's original formulation had no hard stop: it ran until the plan was empty, the agent went off the rails, or a human hit Ctrl+C. That's not safe for unattended runs. Layer in:

- **Iteration cap** — `MAX_ITERATIONS`, always. No source documents a wall-clock or dollar-cost cutoff in any real implementation — that's a known gap, so treat a time or spend ceiling as something you add yourself if cost matters.
- **Sentinel/exit-signal gate** — don't rely on loose semantic language ("I'm done!") alone. Require an explicit structured signal (e.g. an exact-match `--completion-promise` string, or a dual condition: completion language *and* an explicit `EXIT_SIGNAL: true` field) before trusting a stop.
- **Git commit (and push) every iteration** — this is the reversibility mechanism. Tag on successful compile if useful.
- **Search-before-modify** — prevents the agent re-discovering (and re-implementing) work a prior iteration already did.
- **Calibrate validation gates, don't maximize them** — Huntley's own follow-up warns that excessive back-pressure (over-strict tests/lints) can stall the loop as badly as too little.
- **Expect breakage** — "you'll wake up to a broken codebase that doesn't compile from time to time" is the creator's own expectation-setting, not a corner case.

## Known pitfalls

- **Context/output degradation** within a single iteration past roughly 170k tokens — the more of the context window used, the worse the output.
- **Reward-hacking toward placeholders** when the compiler is the only signal — explicit "no placeholders" prompt language is a direct countermeasure, not optional polish.
- **False-negative search** — the agent concludes something isn't implemented when it is, and duplicates it.
- **Drift over long unattended runs** — even successful multi-hour runs report task/intent drift as an open problem.
- **Cost figures are largely self-reported and unaudited.** Treat specific dollar claims (Huntley's own included) as anecdotal, not benchmarked. Don't repeat large runaway-cost numbers from aggregator content as fact — they're frequently uncorroborated against primary sources.

## How this differs from loop constructs already in this environment

Don't conflate any of these — they solve different problems:

- **`/loop` (interval or dynamic/self-paced mode)** — session-scoped and **continuous**: the same session, full transcript history, persists across iterations. This is architecturally the *opposite* of Ralph's fresh-context model, despite the shared word "loop." Use `/loop` for quick interval polling within an active session (checking a deploy, watching a CI run), not for long-horizon bulk execution.
- **Cloud scheduled tasks / routines** — the one native mechanism that actually matches Ralph's "restart from clean state" principle, but at the repo-clone/session level rather than per-task-iteration: each run executes from a fresh clone with no persistent local file access carried between runs.
- **Ralph (external-loop sense)** — for long-horizon bulk execution (migrations, ports, scaffolding) where avoiding context accumulation across *many* iterations within one continuous working session is the dominant concern, and where a machine-checkable "done" signal exists.

## Sources

Full citations in the underlying research report (`reports/Ralph loop coding agent technique.md` in the vault's companion research folder). Primary sources: [ghuntley.com/ralph/](https://ghuntley.com/ralph/) (Jul 14 2025), [ghuntley.com/loop/](https://ghuntley.com/loop/), [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop) and [issue #125](https://github.com/anthropics/claude-plugins-official/issues/125), [ghuntley/how-to-ralph-wiggum](https://github.com/ghuntley/how-to-ralph-wiggum), [frankbria/ralph-claude-code](https://github.com/frankbria/ralph-claude-code).
