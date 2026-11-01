---
description: Make this vault the shared external memory for both Claude Code and GitHub Copilot CLI
title: Second Brain Cross-Tool Setup
date: 2026-11-01
status: active
area: Claude and AI Tooling
tags: [project]
---

# Second Brain Cross-Tool Setup

> [!abstract] Outcome
> Claude Code and GitHub Copilot CLI both read this vault as context automatically, from any repo, without re-explaining it each session.

## Next actions
- [x] Decommission the orphaned `~/Obsidian/YourVault` duplicate — deleted 2026-11-01
- [x] Confirm Copilot CLI actually picks up `~/.copilot/copilot-instructions.md` — verified 2026-11-01 via `copilot instruction list` (shows both `AGENTS.md` and the personal file, from the vault and from `~`) and a live `-p` prompt that answered correctly from instructions alone
- [ ] Reconcile the `dotnet-skills` and `karanb192-awesome-claude-skills` embedded git repos under `🧩 Claude Skills/` (currently untracked, nested `.git` dirs — either proper submodules or flatten them)

## Notes
- The vault lives at `C:\EmperorKaido Vault`, is the live git working copy of `github.com/EmperorKaido99/kai-vault`, and was previously drifted across three untracked-from-each-other copies (this one, `~/kai-vault`, `~/Obsidian/YourVault`). Reconciled 2026-11-01.
- Claude Code reads `~/CLAUDE.md` (global, home-directory scoped).
- Copilot CLI reads `~/.copilot/copilot-instructions.md` (global) and `AGENTS.md` (repo-level) — see [[04 Resources/GitHub Copilot CLI|GitHub Copilot CLI]].
- `~/.claude/skills/*` are Windows junctions into `🧩 Claude Skills/` — 72 of them, rebuilt 2026-11-01 after they were found pointing at the stale `YourVault` copy.

## Log
- 2026-11-01: Rebuilt `~/.claude/skills` junctions against the live vault (was pointing at a stale duplicate). Merged the Oct 13 PARA/second-brain reorg that had landed on GitHub but never been pulled locally. Added `~/.copilot/copilot-instructions.md` and vault-root `AGENTS.md` so Copilot CLI shares the same second brain. Updated `~/CLAUDE.md` to point at the real vault path.

## Related
- Area: [[03 Areas/Claude and AI Tooling]]
- [[04 Resources/GitHub Copilot CLI]]
- [[04 Resources/AGENTS.md Spec]]
