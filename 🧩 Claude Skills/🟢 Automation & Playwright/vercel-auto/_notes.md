---
tags: [claude-skill, automation, vercel]
created: 2026-09-06
status: active
---

# vercel-auto

General-purpose Vercel automation orchestrator. Dual-path: CLI or Playwright browser.

## Triggers
- `/vercel-auto`
- `/vercel`

## Dependencies
- `vercel` CLI (installed globally, v59+)
- `playwright-skill` (for browser-path tasks)
- Chrome Profile 3 (ddskai51@gmail.com) — persistent Vercel login

## Key Learnings (2026-09-06)

- **CLI auth is flaky** — token expires, throws "specified token is not valid". Default to Browser path.
- **`launchPersistentContext` crashes** with Chrome's actual User Data dir. Must use CDP approach:
  launch Chrome externally → connect via `connectOverCDP('http://127.0.0.1:9222')`
- **fullPage screenshots timeout** on Vercel pages (font loading). Use viewport-only or text scraping.
- **Renaming a project does NOT auto-update the `.vercel.app` domain.** Must manually edit the domain
  in Settings > Domains after renaming.
- **Domain edit flow** has a two-step Save: first Save triggers a confirmation with radio buttons
  (redirect-old-to-new vs delete-old), then a second Save applies it.
- **Deployment rows** use overlay `<a>` tags that intercept clicks — navigate directly to deployment
  URLs instead of clicking on them.
- **Team slug:** `mk99-s-projects`
- **Account:** Kai (Hobby plan)
