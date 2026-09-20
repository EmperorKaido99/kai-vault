# ollama-cloud-test

**Description:** Batch test all free-tier Ollama Cloud models to see which are live.

**Source:** Custom skill (created by me)

**Date added:** 2026-09-05

## Why I picked this

I wanted a quick way to sweep all lightweight Ollama Cloud models after getting a new API key, rather than testing them one by one. The script loops through the free-tier list, hits each with a hello prompt, and shows the raw response so I can see which models are actually responding.
