---
name: lts-timesheet-automation
description: "Use this skill when Kai (Malachi Mathins) asks to fill in, update, or submit his LTS PTS timesheet from the terminal. Triggers include: 'do my timesheet', 'fill in my timesheet', 'update PTS', 'submit my timesheet for this week'. This skill drives a real, persistent browser via Playwright, checks Kai's Google Calendar for LTS meetings, generates timesheet content from what Kai tells it he did, fills the PTS web form directly, and keeps Kai in the loop before anything is submitted. It does NOT close the browser after running — it stays logged in and open for next time."
---

# LTS Timesheet Automation Skill (Claude Code + Playwright)

## What this skill does

1. Launches (or reconnects to) a **persistent** browser session on Kai's machine — logs in once, stays logged in across runs, never auto-closes.
2. Reads Kai's **Google Calendar** to find LTS-related meetings for the week and pulls their titles/times in automatically.
3. Asks Kai what he worked on (in his own words, like he's always done in chat).
4. Builds the timesheet content using the **exact same format** established in the LTS Timesheet Helper skill (Weekly Plan, daily Planning, Deliverables/Progress, Challenges & Learning, Friday Weekly Reflection).
5. Fills the PTS web form directly via Playwright — clicking "Add" rows, selecting Company/Type/Activity dropdowns, entering hours per day, and typing the comment text.
6. **Shows Kai a full preview before clicking "Update this timesheet."** Never submits without explicit confirmation.
7. Leaves the browser open and logged in when done — does not shut it down.

---

## First-time setup (Claude must do this once, and only once, with Kai)

Before this skill can run, Claude needs to ask Kai for the following and save the answers to `/lts-timesheet-automation/config.json` in the project so future runs don't ask again:

1. **Which browser to use** — Chrome, Edge, or Brave (whichever Kai has installed and normally uses). Playwright will launch this browser with a **persistent user data directory** so login sessions (PTS + Google) survive between runs.
2. **The PTS timesheet URL** — the exact login page Kai uses.
3. **Google account** — confirm Kai is fine with the same persistent browser profile being logged into Google Calendar, since this skill reads calendar events visually from `calendar.google.com` in that same browser (no separate API keys needed — it just looks at the calendar the way Kai would).
4. **Which calendar events count as "LTS meetings"** — ask Kai for a keyword filter (e.g. events containing "LTS", "Thato", "Susan", "Michael", "CPD", "daily spark") so the skill knows what to pull in automatically vs. ignore.

Save this config once:
```json
{
  "browser": "chrome",
  "user_data_dir": "~/.lts-timesheet-browser-profile",
  "pts_url": "<ask Kai for this on first run>",
  "calendar_keywords": ["LTS", "Thato", "Susan", "Michael", "CPD", "daily spark", "morning sync"]
}
```

**Never hardcode a guessed PTS URL or CSS selector.** The very first time this skill runs against the real site, Claude must use Playwright in headed mode, actually look at the page (via `page.content()` or a screenshot), and identify the real selectors for:
- Login fields
- "Timesheets" nav link
- "Add row" (+) button
- Company search input
- Type dropdown
- Activity dropdown
- Day-of-week hour inputs (Mon–Sun)
- Comments textarea
- "Update this timesheet" button
- "Request sign off for timesheet" button

Once found, **save these selectors into `config.json` under a `selectors` key** so every future run reuses them instead of re-discovering them. If the site's HTML changes and a selector stops matching, fall back to re-inspecting the page rather than guessing.

---

## Step-by-step workflow

### Step 1 — Launch the persistent browser
Use Playwright's `launch_persistent_context` (not a throwaway `launch()`), pointed at the saved `user_data_dir`. This is what makes login "sticky" — Kai logs into PTS and Google once, and every future run reuses that same profile, so it opens already signed in.

```
# Conceptual — Claude Code should adapt this to the actual playwright API being used (python or node)
context = playwright.chromium.launch_persistent_context(
    user_data_dir=config["user_data_dir"],
    headless=False,       # must stay visible — Kai wants to see it live, not headless
    channel=config["browser"]  # "chrome", "msedge", etc.
)
page = context.pages[0] if context.pages else context.new_page()
```

Do **not** call `context.close()` or `browser.close()` at the end of the run. The whole point is that it stays open and logged in — closing it defeats the purpose and would force a re-login next time.

### Step 2 — Check if already logged into PTS
Navigate to `config["pts_url"]`. If the page shows the timesheet home (not a login form), Kai is already authenticated from a previous session — skip straight to Step 3.

If it shows a login form, this is a first-time run (or the session expired): pause and tell Kai "PTS isn't logged in — please log in in the browser window that just opened, then tell me when you're done." Wait for Kai's confirmation before continuing. **Never ask Kai for his password in the chat** — he types it directly into the real browser window.

### Step 3 — Read Google Calendar for LTS meetings this week
In the same persistent browser context, open a new tab to `calendar.google.com`, switch to week view for the target week, and read the visible events (via `page.content()` / accessibility tree / screenshots — whichever is more reliable for that week's layout).

Filter events whose title or description matches any of `config["calendar_keywords"]`. For each match, extract:
- Event title
- Day and start/end time
- Any attendees visible (helps confirm it's a Thato/Susan/Michael meeting)

Present this list back to Kai before doing anything else:
> "I found these LTS-related meetings on your calendar this week: [list]. Want me to include these automatically in the relevant days, or is anything missing/wrong?"

Wait for Kai to confirm or correct before proceeding. This calendar pull is a **starting point**, not a substitute for asking Kai what actually happened in each meeting — still ask him what was discussed, same as always.

### Step 4 — Ask Kai for his week
Same as the manual process this skill was built from: ask Kai (in plain conversation, exactly like before) what his weekly plan is, and what he did each day. Use the calendar findings from Step 3 to prompt him — e.g. "I see a meeting with Thato Tuesday 2–3pm, what was that about?" — rather than assuming.

### Step 5 — Generate the timesheet content
Apply the **exact same rules as the LTS Timesheet Helper skill** (this should live alongside this file as `content-rules.md` — see below) to turn Kai's plain description into:
- A Weekly Plan (goals, no hours)
- Daily Planning entries (0.5h, Morning Sync)
- Activity blocks with Deliverables/Progress and Challenges & Learning
- Friday Weekly Reflection & Learning (0.5h)

Run every piece of generated text through the **humanizer** approach so it doesn't sound AI-generated (see content-rules.md — same rule as before, non-negotiable).

Get every day to total exactly 8h. If Kai's numbers are short, ask him what filled the gap rather than silently padding hours.

### Step 6 — Preview before touching the real form
**Before Playwright types a single character into PTS, show Kai the full week's content** (same as the chat widget previews from before — a clear breakdown per day, per activity, with hours). Ask: "Ready for me to fill this into PTS?" Do not proceed without a yes.

### Step 7 — Fill the PTS form via Playwright
For each day **(Mon–Fri only — never touch the Sat or Sun columns)**:
1. Click "Add row" (+)
2. Type into the Company Search field and select **Learner Tracking Systems (General)** — this is the company for every row, including dev rows
3. Select Type dropdown → Development / General Admin
4. Select Activity dropdown → Development / General admin/meetings / Weekly Reflection & Learnings / Other (Specify in the comment field)
5. Click into the correct day-of-week hour input (Mon–Fri only) and type the hour value — leave Sat and Sun inputs untouched
6. Click into the Comments textarea and type the generated comment text (Planning text, or Deliverables/Progress + Challenges & Learning combined, matching how Kai has manually written it into that box based on the screenshots)
7. Repeat for every activity row that day

Use explicit waits (`page.wait_for_selector`, not fixed `sleep()`) between actions so it doesn't race ahead of the page.

### Step 8 — Final review before submitting
Once every row for the week is filled, **do not click "Update this timesheet" or "Request sign off" automatically.** Take a screenshot of the filled form (or read back the values Playwright entered) and show Kai:
> "Here's what's now in the PTS form for [week]. Everything look right before I hit Update?"

Only click "Update this timesheet" after Kai explicitly confirms. Never click "Request sign off for timesheet" unless Kai separately says he's ready to send it for review — that's a bigger action than saving a draft.

### Step 9 — Leave the browser open
After updating, tell Kai it's done and leave the browser tab open on the timesheet page. Do not close the browser, the context, or navigate away. It should just sit there, logged in, ready for next time.

---

## Keeping Kai in the loop — non-negotiable rules

- **Never fill and submit silently.** Every run shows Kai the calendar findings, then the generated content, then the final filled-form state — three separate check-ins, not one blanket "trust me."
- **Never guess a password or click through a login Kai hasn't done himself.**
- **Never click "Request sign off"** without Kai explicitly asking for that specific action in that specific run.
- **If a selector can't be found** (site changed, page didn't load, etc.), stop and tell Kai exactly what broke — don't retry blindly or fill the wrong field.
- **If the calendar can't be read** (permissions, different view, etc.), tell Kai and fall back to asking him directly about meetings that week — don't block the whole run on it.

---

## Companion file: content-rules.md

This skill depends on a second file, `content-rules.md`, which should contain the full formatting rulebook — copy this in verbatim from the existing `lts_timesheet_skill.md` (Weekly Plan structure, daily Planning format, Deliverables/Progress + Challenges & Learning structure, activity labels, hour-balancing rules, the correct roles — Thato is Kai's manager, Susan is the most senior, Michael is a senior dev — and the humanizer requirement). Keep the two files separate: this file (`SKILL.md`) is the **automation/browser logic**, `content-rules.md` is the **writing/formatting logic**. That way updating how the timesheet should read doesn't require touching the browser automation code, and vice versa.

---

## Playwright setup notes for Claude Code

- Install: `npm install -D playwright` or `pip install playwright` depending on which language Claude Code is driving this in, then `playwright install chrome` (or whichever browser Kai chose).
- Use `launch_persistent_context`, never plain `launch()` — this is what makes the login persist between separate terminal sessions.
- Run **headed**, not headless — Kai explicitly wants to see the browser live.
- The user data directory should be a fixed, reused path (e.g. `~/.lts-timesheet-browser-profile`) — not a temp directory that gets wiped.
- If Kai runs this skill from a fresh terminal session tomorrow, the same browser profile should already be logged into both PTS and Google — that persistence is the entire point of using `launch_persistent_context` over a fresh `launch()`.

---

## What Claude must NOT assume

- Do not assume the PTS URL, login field names, or button selectors — these must be discovered live on Kai's actual site the first time this runs, then saved.
- Do not assume Kai's calendar layout — Google Calendar's DOM varies by view (day/week/month) and account settings; inspect it live rather than hardcoding fixed coordinates or selectors that may not exist.
- Do not assume every calendar event with a person's name in it is a real LTS work meeting — always confirm with Kai before treating it as timesheet content.
