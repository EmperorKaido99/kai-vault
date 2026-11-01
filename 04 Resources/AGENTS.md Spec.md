---
description: The cross-agent AGENTS.md convention and where it's supported
title: AGENTS.md Spec
date: 2026-11-01
source: https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/
status: processed
tags: [resource]
cssclasses: [vault-resource]
---

# AGENTS.md Spec

> [!summary] One line
> A plain-markdown file at a repo's root (or nested in subdirectories) that gives coding agents context and conventions — not specific to any one vendor, unlike `.github/copilot-instructions.md` or `CLAUDE.md`.

## Key points
- Nesting: an `AGENTS.md` deeper in the tree applies to that subtree, letting different parts of a monorepo carry different instructions.
- Supported by GitHub Copilot (CLI and coding agent), and other agentic coding tools that adopted the same convention.
- Doesn't replace tool-specific files — Copilot CLI combines `AGENTS.md` with `.github/copilot-instructions.md` when both exist at a repo root.
- This vault's own `AGENTS.md` (root of `C:\EmperorKaido Vault`) uses it to tell any agent working directly in the vault repo — not just Claude or Copilot — to respect the existing PARA structure and color categories rather than reorganizing.

## My take
Worth adding to any repo Kai works in with more than one AI tool, not just this vault — it's the one file both Claude Code and Copilot CLI can read without per-tool duplication. See [[04 Resources/GitHub Copilot CLI]] for how it fits into Copilot's instruction hierarchy specifically.

## Related
- [[02 Projects/Second Brain Cross-Tool Setup]]
