"""
LTS Timesheet Automation — Playwright driver skeleton.

This is a STARTING POINT, not a finished script. Claude Code must adapt the
selectors (marked with TODO) after inspecting the real PTS site on Kai's
machine, and must NEVER run steps 6-8 (filling/submitting) without an
explicit "yes" from Kai in the terminal for that specific run.

Run with: python fill_timesheet.py
Requires: pip install playwright && playwright install chrome
"""

import json
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

CONFIG_PATH = Path(__file__).parent / "config.json"


def load_config():
    if not CONFIG_PATH.exists():
        print("No config.json found. Run first-time setup with Kai before using this script.")
        sys.exit(1)
    return json.loads(CONFIG_PATH.read_text())


def save_config(config):
    CONFIG_PATH.write_text(json.dumps(config, indent=2))


def launch_persistent_browser(config):
    """
    Launches a persistent, visible browser session. Login state (PTS + Google)
    carries over between runs because we reuse the same user_data_dir every time.
    Never close this context automatically — see SKILL.md Step 9.
    """
    p = sync_playwright().start()
    user_data_dir = Path(config["user_data_dir"]).expanduser()
    user_data_dir.mkdir(parents=True, exist_ok=True)

    context = p.chromium.launch_persistent_context(
        user_data_dir=str(user_data_dir),
        headless=False,  # Kai wants to see it live
        channel=config.get("browser", "chrome"),
    )
    page = context.pages[0] if context.pages else context.new_page()
    return p, context, page


def check_pts_logged_in(page, config):
    """
    Navigates to PTS and checks whether we're already authenticated.
    TODO: replace the selector below with whatever actually indicates
    "logged in" on the real PTS home page (e.g. the "Sign out" link, or
    the "Timesheet User:" label seen in Kai's screenshots).
    """
    page.goto(config["pts_url"])
    page.wait_for_load_state("networkidle")

    # TODO: confirm this selector against the real page
    logged_in_marker = page.locator("text=Sign out")
    if logged_in_marker.count() > 0:
        return True

    print("PTS is not logged in. Please log in manually in the browser window that just opened.")
    input("Press Enter here once you've logged in... ")
    return True


def read_calendar_events(page, config, week_start, week_end):
    """
    Opens Google Calendar in a new tab within the SAME persistent context
    (so it uses Kai's already-logged-in Google session), switches to week
    view, and reads events matching config['calendar_keywords'].

    TODO: this needs real selectors once run against Kai's actual calendar
    view — Google Calendar's DOM differs by locale/settings, so inspect
    live rather than trusting any hardcoded selector here.
    Returns a list of dicts: [{"title": ..., "day": ..., "time": ...}, ...]
    """
    page.goto(f"https://calendar.google.com/calendar/r/week/{week_start}")
    page.wait_for_load_state("networkidle")

    # TODO: replace with real event-reading logic (accessibility tree or DOM)
    events = []
    print("⚠ Calendar reading not yet wired up to real selectors — "
          "inspect calendar.google.com's DOM on Kai's account before filling this in.")
    return events


def fill_day(page, config, day_entry):
    """
    Fills one day's worth of activity rows into the PTS form.
    day_entry example:
    {
        "date": "2026-07-21",
        "rows": [
            {
                "company": "Learner Tracking Systems (General)",
                "type": "General Admin",
                "activity": "General admin/meetings",
                "hours": {"Mon": 0.5},
                "comment": "LTS Morning Sync – Work, Wins & a Daily Spark\\n..."
            },
            ...
        ]
    }

    TODO: every selector below is a placeholder — confirm against the real
    PTS page structure (Add row button, Company Search input, Type/Activity
    dropdowns, day hour inputs, Comments textarea) before running for real.
    """
    for row in day_entry["rows"]:
        # TODO: click the real "+" add-row button
        page.click("text=+")  # placeholder

        # TODO: type into the real company search input and select the match
        page.fill("input[placeholder='Company Search']", row["company"])
        page.wait_for_timeout(300)
        page.click(f"text={row['company']}")

        # TODO: select the real Type and Activity dropdowns
        page.select_option("select[name='type']", row["type"])
        page.select_option("select[name='activity']", row["activity"])

        # TODO: locate the correct day-of-week hour input for this row
        for day, hours in row["hours"].items():
            page.fill(f"input[data-day='{day}']", str(hours))

        # TODO: locate the comments textarea for this specific row
        page.fill("textarea[name='comments']", row["comment"])


def main():
    config = load_config()
    p, context, page = launch_persistent_browser(config)

    try:
        check_pts_logged_in(page, config)

        print("This script is a skeleton. Wire up real selectors and the "
              "week-building logic from content-rules.md before running "
              "against the live timesheet. Never call fill_day() or click "
              "'Update this timesheet' without an explicit confirmation "
              "from Kai for the specific content about to be submitted.")

        # Example of the confirm-before-acting pattern required by SKILL.md:
        # summary = build_week_summary(...)
        # print(summary)
        # if input("Fill this into PTS now? (yes/no): ").strip().lower() != "yes":
        #     print("Stopped — nothing was filled in.")
        #     return
        # for day_entry in week_days:
        #     fill_day(page, config, day_entry)
        # print("Filled. Review the form in the browser before I click Update.")
        # if input("Click 'Update this timesheet' now? (yes/no): ").strip().lower() == "yes":
        #     page.click("text=Update this timesheet")

    finally:
        # Deliberately NOT closing context/browser here — see SKILL.md Step 9.
        # The browser stays open and logged in for next time.
        print("Done for this run. Browser window left open and logged in.")


if __name__ == "__main__":
    main()
