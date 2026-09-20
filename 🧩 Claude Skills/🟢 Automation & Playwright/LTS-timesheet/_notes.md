---
skill: LTS-timesheet
source: custom (user-created)
date_added: 2026-09-01
---

## LTS Timesheet Automation

**Description:** Automates Kai's LTS PTS timesheet — launches a persistent browser, reads Google Calendar for meetings, generates timesheet content from conversation, fills the PTS web form via Playwright, and confirms before submitting. Never closes the browser.

**Source:** Custom skill built from Kai's existing LTS Timesheet Helper workflow

**Files:**
- `SKILL.md` — Browser automation logic (Playwright persistent context, login, form filling)
- `content-rules.md` — Writing/formatting rules (Weekly Plan, daily structure, tone, hour balancing)
- `fill_timesheet.py` — Python Playwright driver skeleton (selectors need real-site discovery)

**Dependencies:** playwright-skill, humanizer

**Triggers:** `/lts-timesheet`, `/timesheet`, "do my timesheet", "fill in my timesheet", "update PTS"

**Why I picked this:**
- Automates the most tedious weekly task — filling in PTS timesheet entries
- Preserves the exact format and tone established over weeks of manual timesheet writing
- Three confirmation checkpoints before anything gets submitted
- Persistent browser means login once, reuse forever
