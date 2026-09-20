# 🧩 Kai's Claude Skills Vault

Personal Obsidian vault of Claude Code skills — **82 skills** across **4 categories**, junctioned straight into `~/.claude/skills/` on my machine. This README is the cheatsheet: scroll down for every skill name and a one-line summary of what it does.

_Last updated: September 20, 2026_

## Contents

- [🔵 Coding & Dev](#coding-dev) (40)
- [🟡 Documents & Writing](#documents-writing) (22)
- [🟢 Automation & Playwright](#automation-playwright) (6)
- [🟣 Planning & Brainstorming](#planning-brainstorming) (14)

---

## 🔵 Coding & Dev

*40 skills*

| Skill (shortcut) | What it does |
|---|---|
| `algorithmic-art` | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. |
| `brandkit` | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. |
| `changelog-generator` | Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear, customer-friendly release notes. |
| `claude-api` | Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration. |
| `connect` | Connect Claude to any app. Send emails, create issues, post messages, update databases - take real actions across Gmail, Slack, GitHub, Notion, and 1000+ services. |
| `connect-apps` | Connect Claude to external apps like Gmail, Slack, GitHub. Use this skill when the user wants to send emails, create issues, post messages, or take actions in external services. |
| `design-taste-frontend` | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. |
| `design-taste-frontend-v1` | The original v1 taste-skill, preserved for projects depending on its exact behavior. The current default is `design-taste-frontend` (v2 experimental), which is a substantial rewrite. |
| `developer-growth-analysis` | Analyzes your recent Claude Code chat history to identify coding patterns, development gaps, and areas for improvement, curates relevant learning resources from HackerNews, and automatically sends a personalized growth… |
| `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work |
| `frontend-design` | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't read as templated defaults. |
| `full-output-enforcement` | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any task requiring exhaustive, unabridged output. |
| `gpt-taste` | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typography (bans 6-line wraps), gapless bento grids, strict GSAP… |
| `high-end-visual-design` | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. |
| `image-to-code` | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then implement the website to match them as closely as possible. |
| `imagegen-frontend-mobile` | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile products. |
| `imagegen-frontend-web` | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal image FOR EVERY section. |
| `industrial-brutalist-ui` | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog degradation effects. |
| `karpathy-guidelines` | Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria. |
| `langsmith-fetch` | Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. Use when debugging agent behavior, investigating errors, analyzing tool calls, checking memory operations, or examining agent… |
| `mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. |
| `minimalist-ui` | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows. |
| `ollama-cloud-test` | Test all free-tier Ollama Cloud models in one sweep. TRIGGER when: the user wants to test or verify which Ollama Cloud models are working, or wants to check free-tier availability. |
| `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind… |
| `redesign-existing-projects` | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. |
| `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `skill-creator` | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill… |
| `skill-share` | A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery. |
| `stitch-design-taste` | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, calibrated color, asymmetric layouts, perpetual micro-motion,… |
| `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session |
| `switch-model` | Fallback to Ollama cloud models when Claude token usage is high or exhausted. TRIGGER when: the user says "switch model", "use ollama", "tokens running out", "fallback model", or Claude Code reports token/context limits… |
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code |
| `use-ollama` | Switch the current session to route queries through Ollama Cloud free-tier models. TRIGGER when: the user invokes /use-ollama, says "use ollama", "switch to ollama", or "use nemotron/gemma/gpt-oss". |
| `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback |
| `using-superpowers` | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions |
| `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions… |
| `web-artifacts-builder` | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). |
| `writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment |

## 🟡 Documents & Writing

*22 skills*

| Skill (shortcut) | What it does |
|---|---|
| `article-optimizer` | Use when the user wants to improve a specific article under a fixed viral-scoring rubric, iterate on one article to raise its score, or run single-article scoring plus rewrite loops. |
| `brand-guidelines` | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. |
| `canvas-design` | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. |
| `content-research-writer` | Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section. |
| `doc-coauthoring` | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. |
| `docx` | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). |
| `image-enhancer` | Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity. Perfect for preparing images for presentations, documentation, or social media posts. |
| `internal-comms` | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. |
| `invoice-organizer` | Automatically organizes invoices and receipts for tax preparation by reading messy files, extracting key information, renaming them consistently, and sorting them into logical folders. |
| `meeting-insights-analyzer` | Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. |
| `pdf` | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding… |
| `pptx` | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx… |
| `publisher-wechatsync` | Use when the user has a finished blog master draft and wants to publish it to multiple content platforms (知乎/掘金/CSDN/公众号 等) via the @wechatsync/cli tool. |
| `research-collector` | Use when the user wants to collect research material for an article or topic by gathering YouTube videos and web articles into a NotebookLM notebook, then running analysis queries and saving results as markdown. |
| `score-optimizer` | Use when the user wants to iterate on a viral-article scoring system itself, calibrate or improve a scoring prompt against labeled samples, or run batch scoring experiments on a fixed article set. |
| `slack-gif-creator` | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. |
| `tailored-resume-generator` | Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills, and achievements to maximize interview chances |
| `theme-factory` | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. |
| `tight-writer` | Enforce concise, no-fluff writing whenever Kai asks Claude to write, summarize, draft, or explain anything. Cuts padding, unnecessary qualifiers, hollow transitions, and AI filler before delivering the output. |
| `twitter-algorithm-optimizer` | Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. Rewrite and edit user tweets to improve engagement and visibility based on how the recommendation system ranks content. |
| `xlsx` | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .xltx, .csv, or .tsv file (e.g., adding columns,… |
| `yt-dlp-direct` | Use when the user wants to download or inspect online audio/video directly with the installed `yt-dlp` CLI. |

## 🟢 Automation & Playwright

*6 skills*

| Skill (shortcut) | What it does |
|---|---|
| `file-organizer` | Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks. |
| `lts-timesheet-automation` | Use this skill when Kai (Malachi Mathins) asks to fill in, update, or submit his LTS PTS timesheet from the terminal. |
| `playwright-skill` | Complete browser automation with Playwright. Auto-detects dev servers, writes reusable test scripts, and supports screenshots, responsive checks, UX validation, login flows, link checks, and arbitrary browser… |
| `vercel-auto` | (no description found) |
| `youtube-downloader` | Download YouTube videos with customizable quality and format options. Use this skill when the user asks to download, save, or grab YouTube videos. |
| `webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs. |

## 🟣 Planning & Brainstorming

*14 skills*

| Skill (shortcut) | What it does |
|---|---|
| `academic-paper` | 12-agent academic paper writing pipeline. 11 modes (full/plan/outline/revision/revision-coach/abstract/lit-review/format-convert/citation-check/disclosure/rebuttal-audit). |
| `academic-paper-reviewer` | Multi-perspective academic paper review with dynamic reviewer personas. Runs a 5-seat, role-separated review panel (Journal-Fit Reviewer + 3 peer-review roles + Devil's Advocate) with field-specific expertise; role… |
| `academic-pipeline` | Orchestrator for the full academic research pipeline: research -> write -> integrity check -> review -> revise -> re-review -> re-revise -> final integrity check -> finalize. |
| `academy-guide` | Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product — it recommends matching courses, tutorials, and use cases from Claude Academy (academy.claude.com),… |
| `brainstorming` | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation. |
| `competitive-ads-extractor` | Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging, problems, and creative approaches are working. Helps inspire and improve your own ad campaigns. |
| `deep-research` | Universal deep research agent team. 13-agent pipeline for rigorous academic research on any topic. 8 modes: full research, quick brief, paper review, lit-review, fact-check, three-way literature scan, Socratic guided… |
| `discernment-nudge` | After you give a substantive answer or draft that the user may act on — advice or recommendations, drafted artifacts such as goals, plans, pitches, proposals, or emails, estimates or projections, analysis or… |
| `domain-name-brainstormer` | Generates creative domain name ideas for your project and checks availability across multiple TLDs (.com, .io, .dev, .ai, etc.). Saves hours of brainstorming and manual checking. |
| `executing-plans` | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| `lead-research-assistant` | Identifies high-quality leads for your product or service by analyzing your business, searching for target companies, and providing actionable contact strategies. |
| `raffle-winner-picker` | Picks random winners from lists, spreadsheets, or Google Sheets for giveaways, raffles, and contests. Ensures fair, unbiased selection with transparency. |
| `research-junshi` | Personalized academic literature digests and ranked research ideas grounded in the researcher's papers and persistent memory. |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |

---

## How these work

Each skill folder has a `SKILL.md` (the skill itself, loaded by Claude Code) and a `_notes.md` (my own notes on why I picked it). Locally, `~/.claude/skills/<name>` are directory junctions pointing back into this vault, so editing here updates every Claude Code session automatically.

To use one, just ask Claude Code for the thing the skill covers — it triggers automatically off the `description` field — or invoke it by name directly (e.g. `/skill-name` or via the Skill tool).
