# Vercel Auto — General-Purpose Vercel Automation

A reusable orchestrator skill for ANY Vercel task: renaming projects,
managing domains, checking deployments, rolling back, managing env vars,
inspecting build logs, and anything else that comes up.

**Triggers:** `/vercel-auto`, `/vercel`, "do a vercel thing"

## Account Info

- **Team slug:** `mk99-s-projects` (personal Vercel account, Hobby plan)
- **Account name:** Kai
- **GitHub user:** ddskai51-3317
- **Chrome profile:** Profile 3 (ddskai51@gmail.com) — always logged in

### Known Projects

| Project | Live URL | Stack |
|---------|----------|-------|
| crimespots | crimespots.vercel.app | Next.js + Supabase |

## Dual Execution Paths

| Path | Tool | Best for |
|------|------|----------|
| **CLI** | `vercel` CLI (v59+) + Vercel REST API | Scriptable, structured tasks: deployments, env vars, project config, logs, rollbacks, aliases, domains (most operations) |
| **Browser** | Playwright driving vercel.com dashboard | Dashboard-only flows: team billing, domain editing, project renaming, promoting deployments, visual verification |

### Path Selection — Lessons Learned

**CLI auth is unreliable** on this machine. The token expires frequently
and `vercel login` must be re-run. When the CLI throws "specified token
is not valid", switch to Browser path immediately — don't waste time
debugging CLI auth.

**Browser path is the reliable default** for this user. The ddskai51
Chrome profile stays logged in persistently. Prefer Browser unless the
task is trivially CLI-only AND CLI auth is confirmed working.

Use CLI when:
- CLI auth is confirmed working (test with `vercel project ls` first)
- The task is a simple read-only query (logs, inspect, list)
- Structured/parseable output is needed

Use Browser when:
- CLI auth fails (common — default to this)
- Project renaming (Settings > General > Project Name field)
- Domain changes (Settings > Domains > Edit button flow)
- Deployment promotion (Deployment page > "Deployment Actions" menu > "Promote to Production")
- Any visual verification needed
- The user says "use the browser" or refers to their Chrome profile

## Decision Protocol (MANDATORY)

Before executing ANY task, present a brief decision block:

```
Path: CLI | Browser
Why this path: <1-2 sentences>
Token cost: CLI ~low (structured JSON) | Browser ~high (DOM, navigation)
Risk: <specific risks for this task>
```

Wait for user acknowledgement before proceeding.

### Mid-Task Path Switch

If the current path hits a wall, STOP and say:

> "The CLI/Browser path can't complete this because [reason]. I'd like
> to switch to [other path]. OK to proceed?"

Never silently switch approaches.

## Execution Mechanics

### CLI Path

```bash
# Test auth first — if this fails, switch to Browser
vercel project ls

# Project operations
vercel ls                           # list projects
vercel inspect <url>                # deployment details
vercel logs <url>                   # build/runtime logs
vercel rollback <deployment-url>    # rollback
vercel promote <deployment-url>     # promote to production

# Environment variables
vercel env ls
vercel env add <name> <environment>
vercel env rm <name> <environment>
vercel env pull .env.local

# Domains
vercel domains ls
vercel domains add <domain>
vercel domains inspect <domain>

# Deploy
vercel deploy                       # preview
vercel deploy --prod                # production
```

For operations the CLI doesn't cover, use the REST API:

```bash
curl -X PATCH "https://api.vercel.com/v9/projects/<project-id>" \
  -H "Authorization: Bearer $VERCEL_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "new-project-name"}'
```

### Browser Path

**Always use Chrome Profile 3 (ddskai51@gmail.com) via CDP.**

**Step 1 — Launch Chrome:**

```bash
# Kill existing Chrome
taskkill //F //IM chrome.exe 2>/dev/null
sleep 2

# Launch with remote debugging
powershell -Command "Start-Process 'C:\Program Files\Google\Chrome\Application\chrome.exe' -ArgumentList '--remote-debugging-port=9222','--profile-directory=Profile 3','--user-data-dir=C:\Users\muras\AppData\Local\Google\Chrome\User Data','--no-first-run','about:blank'"

# Wait and verify CDP is up
sleep 5
curl -s http://127.0.0.1:9222/json/version
```

**Step 2 — Run Playwright script:**

```bash
export SKILL_DIR="$HOME/.claude/skills/playwright-skill"
export TMP_DIR="$(node -p 'require("node:os").tmpdir()')"
node "$SKILL_DIR/run.js" "$TMP_DIR/vercel-auto-task.js"
```

**Standard template:**

```javascript
const { chromium } = require('playwright');

(async () => {
  var browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  var context = browser.contexts()[0];
  var page = context.pages()[0] || await context.newPage();

  try {
    await page.goto('https://vercel.com/mk99-s-projects');
    await page.waitForTimeout(3000);

    // ... task-specific automation ...

  } catch (e) {
    console.error('Error: ' + e.message);
  } finally {
    browser.close();
  }
})();
```

### Browser Gotchas (from real experience)

1. **`launchPersistentContext` does NOT work** with Chrome's actual User
   Data directory on this machine. It crashes immediately. Always use
   the CDP approach (launch Chrome externally, connect via
   `connectOverCDP`).

2. **`fullPage: true` screenshots timeout** on Vercel dashboard pages
   (font loading hangs). Use viewport-only screenshots or skip them and
   read text instead.

3. **Vercel deployment rows use overlay `<a>` tags** that intercept
   clicks on text elements. Navigate directly to deployment URLs
   instead of clicking row text:
   ```
   https://vercel.com/mk99-s-projects/<project>/<deployment-id>
   ```

4. **Login check**: After navigating to dashboard, check if the URL
   contains `/login`. If so, the session expired — tell the user to
   log in manually in the browser window.

## Verified Procedures

### Rename a Project

**Path:** Browser (Settings > General page)

1. Navigate to `https://vercel.com/mk99-s-projects/<project>/settings`
2. Find the input with the current project name value
3. Clear it and type the new name
4. Click the "Save" button
5. **IMPORTANT:** Renaming does NOT update the `.vercel.app` domain
   automatically. You must also update the domain (see below).

### Update Production Domain After Rename

**Path:** Browser (Settings > Domains page)

1. Navigate to `https://vercel.com/mk99-s-projects/<project>/settings/domains`
2. Click the "Edit" button on the old `.vercel.app` domain
3. Clear the domain input, type the new `.vercel.app` domain
4. Click "Save" — a confirmation dialog appears with two options:
   - **"Redirect old domain to new"** — keeps old URL working via redirect (recommended)
   - **"Remove old domain"** — permanently deletes the old domain
5. Select the redirect radio: `[role="radio"][value="redirect-old-to-new"]`
6. Click the second "Save" button (in the confirmation section)

**Radio button selectors in the edit dialog:**
- `[role="radio"][value="connect-to-environment"]` — environment assignment
- `[role="radio"][value="redirect"]` — redirect to another domain
- `[role="radio"][value="redirect-old-to-new"]` — redirect old → new (rename flow)
- `[role="radio"][value="delete-old"]` — delete old domain (rename flow)

### Promote a Deployment to Production

**Path:** Browser (Deployment detail page)

1. Navigate to `https://vercel.com/mk99-s-projects/<project>/<deployment-id>`
2. Click the button with `aria-label="Deployment Actions"` (three-dot menu)
3. Menu items available:
   - "Instant Rollback"
   - **"Promote to Production"**
   - "Redeploy"
   - "Copy URL"
   - "View All Branch Deployments"
   - "Skew Protection Threshold"
   - "Delete"
4. Click "Promote to Production"
5. Confirm in the dialog that appears

**Finding deployment IDs:** On the deployments page, look for
`a[href*="/mk99-s-projects/<project>/"]` — the last path segment is
the deployment ID (e.g., `5Fw3m59nZVYuEvfqyUSkYT5R3o52`).

### Check Deployment Status

**Path:** Browser (quick text scrape)

```javascript
await page.goto('https://vercel.com/mk99-s-projects/<project>/deployments');
await page.waitForTimeout(5000);
var text = await page.locator('body').innerText();
// Parse for "Ready", "Error", "Building" statuses
```

## Dashboard URLs

- Dashboard: `https://vercel.com/mk99-s-projects`
- Project overview: `https://vercel.com/mk99-s-projects/<project>`
- Project settings: `https://vercel.com/mk99-s-projects/<project>/settings`
- Domains: `https://vercel.com/mk99-s-projects/<project>/settings/domains`
- Env vars: `https://vercel.com/mk99-s-projects/<project>/settings/environment-variables`
- Deployments: `https://vercel.com/mk99-s-projects/<project>/deployments`
- Deployment detail: `https://vercel.com/mk99-s-projects/<project>/<deployment-id>`
- Logs: `https://vercel.com/mk99-s-projects/<project>/logs`
- Billing: `https://vercel.com/mk99-s-projects/~/billing`

## Safety Rules

1. **Never delete** a Vercel project or domain without explicit user
   confirmation, regardless of which path is used.
2. **Never touch Supabase** or any other connected service — Vercel-only.
3. **Always show a plan** before executing anything with side effects
   (renames, redeploys, domain changes, env var edits, rollbacks).
4. **Destructive CLI flags** (`--force`, `--yes`) require explicit user
   approval.
5. **API tokens**: Use `$VERCEL_TOKEN` from env. Never hardcode.
6. **Domain renames**: Always offer the redirect option so old URLs
   keep working. Never silently delete an old domain.

## Dependencies

- **Vercel CLI** (`vercel` v59+) — installed at `%APPDATA%/npm/vercel`
- **playwright-skill** — for browser-path execution
- **Node.js** v25+ — for Playwright scripts
- **Chrome** — installed at `C:\Program Files\Google\Chrome\Application\chrome.exe`
