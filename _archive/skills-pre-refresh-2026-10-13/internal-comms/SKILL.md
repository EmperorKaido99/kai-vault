---
name: internal-comms
description: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).
license: Complete terms in LICENSE.txt
---

## When to use this skill
To write internal communications, use this skill for:
- 3P updates (Progress, Plans, Problems)
- Company newsletters
- FAQ responses
- Status reports
- Leadership updates
- Project updates
- Incident reports

## How to use this skill

To write any internal communication:

1. **Identify the communication type** from the request
2. **Load the appropriate guideline file** from the `examples/` directory:
    - `examples/3p-updates.md` - For Progress/Plans/Problems team updates
    - `examples/company-newsletter.md` - For company-wide newsletters
    - `examples/faq-answers.md` - For answering frequently asked questions
    - `examples/general-comms.md` - For anything else that doesn't explicitly match one of the above
3. **Follow the specific instructions** in that file for formatting, tone, and content gathering

If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format.

## Keywords
3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms


---

## Writing style (tight-writer rules — always apply)

All text output from this skill must be concise and direct. Apply these rules before delivering any written content:

- **Lead with the point** — first sentence IS the answer, no warm-up
- **Cut filler phrases** — "it is worth noting", "in todays landscape", "lets dive in", etc.
- **One hedge max** — never stack "could potentially might"
- **Active voice** by default
- **End cleanly** — no "I hope this helps" or "let me know if you need anything"
- **Length targets**: emails ≤150 words, summaries 3–5 sentences, list items 1 sentence

Unless Kai explicitly asks for more detail or a different style, keep it tight.

