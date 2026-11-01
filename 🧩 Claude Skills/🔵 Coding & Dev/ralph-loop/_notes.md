---
tags: [skill, coding-dev]
cssclasses: [skill-coding]
---
# ralph-loop
**Description:** Use when considering running a coding agent unattended in a repeated loop over many iterations (bulk migrations, ports, scaffolding greenfield projects) and want fresh context each iteration instead of one long session. Also use when asked to explain, compare, or set up a "Ralph loop" / "Ralph Wiggum technique".
**Source:** Written from a 4-agent deep-research pass (origin/definition, implementation mechanics, pitfalls/guardrails, comparison to existing loop constructs); full report at `reports/Ralph loop coding agent technique.md` alongside the underlying notes in `research_notes/Ralph loop coding agent technique/` on this machine. Primary source: https://ghuntley.com/ralph/
**Date added:** 2026-11-01

## Why I picked this.
Wanted to understand whether the "Ralph loop" technique circulating in the agentic-coding community is worth using, and specifically how it differs from Claude Code's own `/loop` skill and Anthropic's official `ralph-loop` plugin — those turned out to be three genuinely different things sharing overlapping names, which is the main thing worth remembering here. The official Anthropic plugin does NOT reproduce the original's fresh-context mechanic (uses a Stop hook in one continuous session instead, context balloons toward ~200k tokens by iteration 20 — documented in anthropics/claude-plugins-official#125).

<!-- skill-links:start -->
## Related
Home: [[Home]]
Maps: [[Skill Maps/Dev Workflow|Dev Workflow]]
Works with: [[🧩 Claude Skills/🔵 Coding & Dev/using-git-worktrees/_notes|using-git-worktrees]], [[🧩 Claude Skills/🔵 Coding & Dev/dispatching-parallel-agents/_notes|dispatching-parallel-agents]], [[🧩 Claude Skills/🔵 Coding & Dev/subagent-driven-development/_notes|subagent-driven-development]], [[🧩 Claude Skills/🔵 Coding & Dev/verification-before-completion/_notes|verification-before-completion]], [[🧩 Claude Skills/🔵 Coding & Dev/test-driven-development/_notes|test-driven-development]]
<!-- skill-links:end -->
