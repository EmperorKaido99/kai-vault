---
description: Where Copilot CLI reads custom instructions from, and how that compares to Claude Code
title: GitHub Copilot CLI
date: 2026-11-01
source: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions
status: processed
tags: [resource]
cssclasses: [vault-resource]
---

# GitHub Copilot CLI

> [!summary] One line
> Copilot CLI's instructions hierarchy: global `~/.copilot/copilot-instructions.md`, repo-level `.github/copilot-instructions.md`, and `AGENTS.md` — repo-level always wins, and if both `AGENTS.md` and `.github/copilot-instructions.md` exist at a repo root, both get used.

## Key points
- `$HOME/.copilot/copilot-instructions.md` — user-level, applies across every repo. This is the Copilot equivalent of Claude Code's `~/CLAUDE.md`.
- `$HOME/.copilot/instructions/**/*.instructions.md` — modular user-level instructions, split by topic.
- `.github/copilot-instructions.md` — repo-wide instructions, same idea but scoped to one repo.
- `.github/instructions/**/*.instructions.md` — modular repo-level instructions.
- `AGENTS.md` — the cross-agent standard (also read by Codex, Cursor, and others). Nested `AGENTS.md` files apply to subdirectories.
- Custom agents: repo-scoped under `.github/agents/*.agent.md`, personal/cross-project under `~/.copilot/agents/*.agent.md`.
- Config/state lives at `~/.copilot/` (`config.json`, `permissions-config.json`, trusted folders) — separate from the VS Code extension, which is not installed here; this machine uses the standalone CLI.

## My take
Trusted folder is set to `C:\Users\muras` (the whole home directory), which is why a home-scoped `copilot-instructions.md` works the same way `~/CLAUDE.md` does for Claude Code — see [[02 Projects/Second Brain Cross-Tool Setup|Second Brain Cross-Tool Setup]].

## Related
- [[04 Resources/AGENTS.md Spec]]
- [[03 Areas/Claude and AI Tooling]]
