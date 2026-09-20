---
name: ollama-cloud-test
description: |-
  Test all free-tier Ollama Cloud models in one sweep.
  TRIGGER when: the user wants to test or verify which Ollama Cloud models are working, or wants to check free-tier availability.
  Checks that OLLAMA_API_KEY is exported, then runs test_models.sh — hitting each lightweight cloud model with a single hello prompt.
---

# Ollama Cloud Model Tester

Tests a curated list of lightweight (level 1–2) Ollama Cloud models against the live API to see which ones respond.

## What the script does

- Loops over 7 free-tier cloud models
- Sends each a short hello prompt via `https://ollama.com/v1/messages` (Anthropic-compatible format)
- Prints the raw JSON response per model
- Waits 2 seconds between calls (free tier allows 1 concurrent request)

## When to use

- After getting a new Ollama Cloud API key to confirm it works
- When you want to know which models are currently live and responding
- To quickly benchmark which free-tier models are fastest/most useful

## How to run

1. **Check that the key is set** — read it from `C:\Users\muras\OneDrive\Desktop\tokesn\Ollama Cloud Keys.txt` and export it:
   ```bash
   export OLLAMA_API_KEY="<key from file>"
   ```
2. **Run the script:**
   ```bash
   bash ~/.claude/skills/ollama-cloud-test/test_models.sh
   ```

## Script location

`~/.claude/skills/ollama-cloud-test/test_models.sh`

## Notes

- Model list in the script may go stale — cross-check against `ollama.com/library` for current tags
- Free tier key lives at: `C:\Users\muras\OneDrive\Desktop\tokesn\Ollama Cloud Keys.txt`
- Never paste or display the key value in conversation output
