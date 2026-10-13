---
description: How this vault is organised and how to use it
title: Second Brain Guide
tags: [guide]
cssclasses: [vault-home]
---

# Second Brain Guide

> [!tip] The loop
> **Capture** into the Inbox, **organise** by actionability, **distil** to the key points, **express** by using it.

## Where things go
| Folder | What it holds | Test |
|---|---|---|
| [[00 Inbox/README\|00 Inbox]] | Anything new, unsorted | Empty it weekly |
| [[01 Daily/README\|01 Daily]] | One note per day | Scratchpad |
| [[02 Projects/README\|02 Projects]] | Work with an outcome and end date | Can it be "done"? |
| [[03 Areas/README\|03 Areas]] | Ongoing responsibilities | Does it never end? |
| [[04 Resources/README\|04 Resources]] | Reference material | Might I need it later? |
| [[05 Templates/README\|05 Templates]] | Note templates | |
| `ðŸ§© Claude Skills` | Live skills Claude Code loads | Do not move or rename (junctions) |
| `_archive` | Finished or retired | |

## Conventions
- Frontmatter on every note: `description`, `title`, `date`, `tags`; `source` for anything captured; `status` for projects, resources and ideas.
- Link as you write. Every note links to at least one Area, Project or Map.
- Names are plain words. Folder names are `snake_case` only for folders created by `vault-capture`.
- Tags are for type (`project`, `area`, `resource`, `idea`, `daily`, `review`). Links are for topics.

## Skill workflows
| I want to... | Use |
|---|---|
| Save a web page | `vault-capture` |
| Log something I learned today | `vault-journal` |
| Keep an insight from a Claude chat | `vault-save` |
| See what the vault knows on a topic | `vault-synthesize` |
| Build a map of a theme | `vault-moc` |
| Find broken links and orphans | `vault-health` |

## Rhythm
- **Daily:** open today's note, set a focus, log as you go.
- **Weekly:** run the [[05 Templates/Weekly Review|Weekly Review]] template.
- **Monthly:** run `vault-health` and archive finished projects.

## Views
- [[Dashboard.base|Dashboard]]: inbox, active projects and all skills as tables.

Back to [[Home]]