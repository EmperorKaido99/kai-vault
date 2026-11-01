---
tags: [claude-skill, automation, vercel]
created: 2026-09-06
status: active
cssclasses: [skill-automation]
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

<!-- skill-links:start -->
## Related
Home: [[Home]]
Maps: [[Skill Maps/Browser & Automation|Browser & Automation]]
Works with: [[🧩 Claude Skills/🟢 Automation & Playwright/playwright-skill/_notes|playwright-skill]], [[🧩 Claude Skills/🟢 Automation & Playwright/webapp-testing/_notes|webapp-testing]], [[🧩 Claude Skills/🔵 Coding & Dev/web-artifacts-builder/_notes|web-artifacts-builder]], [[🧩 Claude Skills/🟢 Automation & Playwright/file-organizer/_notes|file-organizer]], [[🧩 Claude Skills/🟢 Automation & Playwright/video-downloader/_notes|video-downloader]], [[🧩 Claude Skills/🔵 Coding & Dev/connect/_notes|connect]], [[🧩 Claude Skills/🔵 Coding & Dev/connect-apps/_notes|connect-apps]], [[🧩 Claude Skills/🟡 Documents & Writing/slack-gif-creator/_notes|slack-gif-creator]], [[🧩 Claude Skills/🟡 Documents & Writing/image-enhancer/_notes|image-enhancer]]
<!-- skill-links:end -->
