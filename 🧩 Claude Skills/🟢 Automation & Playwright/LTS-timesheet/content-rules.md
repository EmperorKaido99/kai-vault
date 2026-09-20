---
name: lts-timesheet-helper
description: "Use this skill whenever Kai (Malachi Mathins) asks for help filling in, writing, or structuring his weekly PTS timesheet entries for his LTS Systems contract work. Triggers include: 'do my timesheet', 'write my timesheet', 'what do I put for today', 'timesheet entries', 'planning section', 'weekly plan', or any mention of PTS, LTS, daily spark, or weekly reflection in a timesheet context. Also use when Kai describes what he did during the week and asks for structured timesheet comments. Produces interactive accordion widgets with a weekly plan at the top and all days expandable/collapsible, following the exact format established in prior sessions."
---

# LTS Timesheet Helper Skill

## Overview
This skill produces professional, detailed PTS timesheet entries for Kai (Malachi Mathins), a Full Stack .NET Developer on contract at LTS Systems (ltsystems.co.za) in Cape Town, South Africa.

**The people Kai works with:**
- **Thato Mashita** — Kai's manager (and his timesheet reviewer)
- **Susan** — the big boss / most senior person
- **Michael** — a senior developer

The output is always a visual accordion widget showing each day of the week with expandable cards. Each card follows a strict internal structure described below.

---

## Timesheet System — PTS Structure

Every timesheet entry in PTS has these fields:
- **Company** — the client/entity
- **Type** — Development, General Admin, etc.
- **Activity** — Development, General admin/meetings, Support, etc.
- **Hours per day** — Mon through Sun columns
- **Comments** — the free-text field where all detail goes

### The row types used every day

All rows use **Company: Learner Tracking Systems (General)**.

| Row | Company | Type | Activity | Hours | Comment |
|-----|---------|------|----------|-------|---------|
| Morning Sync / Planning | Learner Tracking Systems (General) | General Admin | General admin/meetings | 0.5h | Planning content (see below) |
| Dev/work row | Learner Tracking Systems (General) | Development | Development | 7.5h | Activity content (see below) |
| Meeting row | Learner Tracking Systems (General) | General Admin | General admin/meetings | varies | Meeting title + Deliverables/Progress |
| Weekly Reflection (Fridays) | Learner Tracking Systems (General) | General Admin | Weekly Reflection & Learnings | 0.5h | Reflection content (see below) |
| Weekly Plan | Learner Tracking Systems (General) | General Admin | Other (Specify in the comment field) | 0h | "This week I want to:\n[goals]" |

> **Weekly Plan row**: logged with 0 hours. Comment format is exactly: first line `This week I want to:`, second line the goal text. This is a real PTS row — not just a widget label.

> **Meeting rows**: 1:1s, check-ins, team meetings — go under General Admin → General admin/meetings, separate from dev rows.

### Daily hour target
- **8 hours total per working day (Mon–Fri)** — always
- Standard split: **0.5h Morning Sync/Planning + 7.5h everything else**
- If meetings eat into the day, reduce dev hours proportionally to keep total at 8h
- **Saturday and Sunday always stay at 0.00 — never log any hours on weekends**

---

## Weekly Plan Block (top of every week)

Before the first day of the week (Monday, or the first working day if Kai was off earlier), add a **Weekly Plan** block at the very top of the widget, above all day cards.

**Rules:**
- **No hours are logged for this block** — it is context/framing only, not a timesheet activity
- Framed as **goals for the week**, not a day-by-day breakdown
- Written in first person, natural tone
- 3–5 short goal statements covering what Kai aims to achieve that week
- Should reference the current project(s) and any known key milestones (deliverables, meetings, deadlines)

**Format:**
```
Weekly Plan — [week date range]
This week I'm focused on:
- Goal 1 (e.g. "Complete the Web Forms build for the remaining LTS pages")
- Goal 2 (e.g. "Finalise and hand off the UI/UX research document to Susan")
- Goal 3 (e.g. "Continue testing MisoTTS and lock in the video production toolkit")
```

**Styling:** distinct block at the top — use a subtle accent background (e.g. `var(--color-background-secondary)` with a coloured left border or a small "Weekly Goals" label pill). Visually separate from the daily Planning blocks so it reads as week-level context, not a day entry.

---

## Day Entry Structure

Every day card in the widget must contain these sections in this exact order:

### 1. Planning Block (0.5h)
```
Planning — LTS Morning Sync – Work, Wins & a Daily Spark
[2-3 sentences written in first person describing what Kai plans to do today.
Should sound natural and personal, not corporate. Reference actual tasks planned.]
```

### 2. Activity Blocks (remaining hours)
Each activity block contains:

```
[hours] | [label] | [Activity title]

Deliverables/Progress:
- bullet 1
- bullet 2
- bullet 3

Challenges & Learning:
- bullet 1
- bullet 2
```

**Rules for activity blocks:**
- Titles should be specific and descriptive — not generic like "did some work"
- Deliverables/Progress bullets describe what was actually produced or completed
- Challenges & Learning bullets describe what was hard and what was learned — these must feel genuine, not filler
- Use technical specificity where relevant (e.g. `Site.Master`, `.aspx`, `Page_Load`, `_Layout.cshtml`, `Repeater` control)
- Sub-bullets use `<code>` tags for file names, code terms, and technical references

### 3. Total Row
Shows hour breakdown by type e.g. `Dev 6h | Meeting 1h | Admin 0.5h | Total 8h`

### 4. Weekly Reflection & Learnings (Fridays only — 0.5h)
Every Friday gets a **Weekly Reflection & Learnings** block at the end of the day (Activity: `Weekly Reflection & Learnings`). This must:
- Reflect genuinely on the week's output — not be generic
- Reference specific things that happened that week (meetings, discoveries, pivots, deliverables)
- Include a meaningful "key takeaway" or learning moment
- Be written in first person, natural tone

---

## Activity Label Types & Colours

| Label | When to use | Colour |
|-------|-------------|--------|
| Dev | Web Forms build, Razor Views, C#, HTML, CSS, bug fixes, code reviews | Green |
| Research | Tool research, competitor research, platform research, UI/UX research | Blue |
| Docs | Writing documents, reports, technical documentation, feedback documents | Purple |
| Meeting | 1:1s, team meetings, check-ins, presentations, demos | Orange |
| Creative | Animaker, video production, design work, visual assets | Red/orange |
| Reflection | Weekly Reflection & Learning (Fridays only) | Grey |
| Admin | Morning Sync / Planning entry | Grey |

---

## Kai's Work Context

### Current contract
- **Company:** LTS Systems (ltsystems.co.za)
- **Role:** Full Stack .NET Developer
- **Reviewer:** Thato Mashita (Kai's manager)
- **The team:**
  - Thato Mashita — Kai's manager, and his timesheet reviewer
  - Susan — the big boss / most senior person
  - Michael — a senior developer

### Tech stack used in this contract
- ASP.NET Web Forms (.NET 4.8.1) — **primary stack for the LTS website build**
- C#, HTML, CSS (no JavaScript — CSS-only patterns throughout)
- `Site.Master` for shared layout
- Code-behind files (`.aspx.cs`)
- Previously built an MVC version (Razor Views, ViewModels) before pivoting to Web Forms after team meeting on 05/19

### Projects worked on (in order)
1. **LTS Website Redesign** — Design phase (Week 1), .NET MVC build (Week 2), Web Forms pivot and rebuild (Weeks 3–4)
2. **UI/UX Research Document** — Research and writing on web UI/UX best practices for the CPD platform, including Southern African regional data context and UI framework recommendations (Weeks 5–6)
3. **Instructional Video Project** — 3 short videos on how to use the LTS CPD portal, produced using Animaker with MisoTTS (GitHub: MisoLabsAI/MisoTTS) for AI voiceover (Week 6 ongoing)

### Recurring daily activities
- **LTS Morning Sync – Work, Wins & a Daily Spark** — 0.5h every working day, logged under General admin/meetings
- **Weekly Reflection & Learning** — 0.5h every Friday, added as the last activity block of the day

### Important project events to know
| Date | Event |
|------|-------|
| 05/04–05/08 | Design phase — competitor research, wireframes, 3 concept designs, team presentation |
| 05/11–05/15 | .NET MVC build, testing day (Thu), technical documentation + handoff (Fri) |
| 05/18 | Finalised .NET MVC site |
| 05/19 | 1pm team + Michael meeting → pivot to Web Forms → restarted project |
| 05/20–05/22 | Web Forms build (Home, Features, Pricing, FAQ, testimonials, client carousel) |
| 05/22 | Team demo of Web Forms progress |
| 05/26 | Refined Friday's work + technical research on Web Forms platform |
| 05/27 | Thato review meeting, feedback doc sent to Susan, product page image redesign, Home/FAQ refinements |
| 05/28 | Further refinements + CPD portal account creation and 2h testing session |
| 05/29 | 1h 1:1 with Susan + CPD UI research + written feedback (UI + password section) |
| 05/30 | UI/UX report written (full CPD system, framework recommendations), dev work, weekly reflection |
| 06/02 | New project briefing (research document) — meeting with Susan + Thato |
| 06/03 | Research + document writing + bug fixes on old project |
| 06/04 | Timesheet guidance meeting with Susan (1h) + research + 3pm project check-in with Susan (0.5h) |
| 06/05 | Research + document writing (Southern African data context) |
| 06/06 | Final research + document writing + weekly reflection |
| 06/09–06/10 | Sick leave — no entries |
| 06/11 | Returned from sick leave — UI/UX document meeting, presented findings, received new video project brief, researched tools, started Animaker |
| 06/12 | AI tool research, Animaker refinement, MisoTTS GitHub exploration |
| 06/13 | MisoTTS hands-on testing, further tool research, weekly reflection |

---

## Widget Format Instructions

Always produce an **interactive accordion widget** using `show_widget`. Never produce plain text timesheet entries.

### Widget structure
```
Week tabs (if multiple weeks) → Week title header → Weekly Plan block (no hours) → Day cards (collapsible)
Each day card:
  - Header: day name, total hours, summary label, chevron toggle
  - Body (hidden by default, toggled by click):
    - Planning block (highlighted background)
    - Activity blocks separated by dividers
    - Total row at the bottom
```

### Styling rules
- Use CSS variables (`var(--color-text-primary)`, `var(--color-background-secondary)`, etc.) for all colours — never hardcode light/dark colours
- Planning block: `var(--color-background-secondary)` background
- Activity labels: coloured pills (see label table above)
- `Deliverables/Progress:` and `Challenges & Learning:` in small uppercase as section headers
- Bullets at 12px, slightly muted colour (`var(--color-text-secondary)`)
- Total row: small pills at the bottom of each day card

### Special banners
- **New project assigned:** green banner at top of day body
- **Pivot/direction change:** red/orange banner
- **Sick leave:** grey notice card in place of the day entry
- **Today / ongoing:** blue badge next to the day title

---

## Hour Balancing Rules

When Kai gives approximate hours that don't add to exactly 8h:
1. Adjust the largest block by 0.5h to balance
2. Never silently drop an activity — always include everything mentioned
3. If a meeting is mentioned, always log it separately from dev time
4. If total hours described exceed 8h, reduce the largest dev/research block
5. Show the exact breakdown in the total row so Kai can verify

---

## Tone & Writing Style

**IMPORTANT — Always apply the humanizer skill.** Before finalising any timesheet text (planning blocks, activity descriptions, Deliverables/Progress, Challenges & Learning, weekly reflections), run it through the humanizer approach so it does not sound AI-generated. Specifically avoid:
- Superficial "-ing" endings that add fake depth ("ensuring...", "highlighting...", "reflecting...", "contributing to...", "showcasing...")
- Significance inflation ("plays a vital role", "marks a pivotal moment", "underscores the importance")
- Rule-of-three lists where two would do
- Negative parallelism ("it's not just X, it's Y")
- Promotional/buzzword language ("seamless", "robust", "leverage", "streamline", "cutting-edge")
- Filler phrases ("it is important to note", "in order to", "at its core")
- Copula avoidance ("serves as", "functions as", "stands as") — just use "is"/"are"
- Every sentence being the same length — vary the rhythm, mix short and long
- Em dash overuse

The writing should sound like a real developer wrote it in a hurry at the end of the day — natural, specific, varied, occasionally a bit blunt. Not polished corporate filler.

- First person, natural, professional — not corporate or robotic
- Planning sentences sound like something a real developer would say in a standup
- Challenges & Learning feel genuine — not "I learned the importance of communication"
- Technical terms used accurately and specifically (e.g. "Web Forms `Repeater` control", "`Page_Load` postback lifecycle", "CSS `@keyframes` animation")
- Avoid filler phrases like "I ensured that", "I made sure to", "it is important to note"
- Keep bullet points concise but specific — one clear point per bullet
- **Never refer to Kai as a "stakeholder."** Kai is the developer. Do not use the word "stakeholder" at all in the entries. When describing meetings or feedback, name who it actually was — "feedback from Susan" (the big boss), "direction from Thato" (Kai's manager), "a review with Michael" (senior dev), or "from the team". This reads more naturally and is accurate.

---

## Example Day Entry (reference format)

**Monday 05/26**
Planning (0.5h): "Today I'll be going back over the work from Friday and refining any outstanding items on the Web Forms site before they pile up. I'll also be spending time researching and exploring the ASP.NET Web Forms platform more deeply to improve the quality and structure of the ongoing build."

Dev (3.5h) — Refined outstanding Web Forms work from Friday
Deliverables/Progress:
- Revisited and refined the testimonials section and client carousel built on Friday
- Cleaned up code-behind files and resolved minor CSS inconsistencies identified during end-of-week review
- Verified all recently completed pages are rendering correctly within `Site.Master`

Challenges & Learning:
- Reviewing your own work with fresh eyes after a weekend reveals small issues that are easy to overlook when in build mode

Dev (4h) — Technical research — ASP.NET Web Forms platform deep dive
Deliverables/Progress:
- Conducted in-depth technical research on ASP.NET Web Forms to strengthen understanding of the platform
- Focused on server control lifecycle, data binding patterns, and master page inheritance
- Applied findings by reviewing and improving existing `.aspx` pages and code-behind structure

Challenges & Learning:
- Understanding the `Page_Load` lifecycle and postback state behaviour improved how code-behind logic is structured across the project

Total: Dev 7.5h | Admin 0.5h | Total 8h

---

## Quick Reference Checklist

Before producing any timesheet output, confirm:
- [ ] Has the text been run through the humanizer approach so it doesn't sound AI-generated?
- [ ] Is the word "stakeholder" completely absent (name Susan/Thato/Michael/the team instead)?
- [ ] Are the roles correct — Thato is Kai's manager, Susan is the big boss, Michael is a senior dev?
- [ ] Is there a Weekly Plan row logged in PTS (Company: Learner Tracking Systems (General), Type: General Admin, Activity: Other (Specify in the comment field), 0 hours, comment starts with "This week I want to:")?
- [ ] Does every day total exactly 8h?
- [ ] Does every day start with a 0.5h Planning block?
- [ ] Does every Friday end with a 0.5h Weekly Reflection & Learnings block (Activity: "Weekly Reflection & Learnings")?
- [ ] Are all activity labels correct (no CPD label — use Dev or Research instead)?
- [ ] Are Deliverables/Progress and Challenges & Learning present on every activity block?
- [ ] Is the widget interactive (accordion, not static)?
- [ ] Are CSS variables used for all colours?
- [ ] Does the planning text sound natural and first-person?
- [ ] Are technical terms used accurately and specifically?
- [ ] Are meeting rows noted separately from dev rows?
