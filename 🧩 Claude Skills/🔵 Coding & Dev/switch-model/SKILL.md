---
name: switch-model
description: |-
  Fallback to Ollama cloud models when Claude token usage is high or exhausted.
  TRIGGER when: the user says "switch model", "use ollama", "tokens running out", "fallback model", or Claude Code reports token/context limits approaching.
  Reads the Ollama cloud API key from a read-only file and provides the user with ready-to-run commands to continue their work via Ollama.
---

# Switch Model — Ollama Cloud Fallback

When Claude Code tokens are running low or exhausted, help the user seamlessly continue work using an Ollama cloud model.

## Key File

- **Ollama Cloud API Key:** `C:\Users\muras\OneDrive\Desktop\tokesn\Ollama Cloud Keys.txt`
- This file is **read-only**. Never copy, store, or display the key in output.

## How It Works

1. **Detect:** Claude warns the user when token usage is high or context is nearly full.
2. **Read:** Read the API key file silently using the Read tool — never display its contents.
3. **Execute:** Make the API call directly via the Bash tool using the key internally.

## Usage

When triggered:

1. **Read the key file silently** using the Read tool — do NOT display its contents or the key value.
   File: `C:\Users\muras\OneDrive\Desktop\tokesn\Ollama Cloud Keys.txt`
   Key format: `Ollama Cloud Keys $env:= "..."` — parse the value between the quotes.

2. **Make the API call directly** via the Bash tool, with the key embedded in the command (never echoed to output):

```bash
curl -s https://ollama.com/v1/messages \
  -H "Authorization: Bearer <key-read-from-file>" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model": "<model>", "max_tokens": 512, "messages": [{"role": "user", "content": "<prompt>"}]}'
```

3. **Return only the model response** to the user — never the key, never a curl command with the key visible.

## When to Trigger

- User explicitly asks to switch models
- Claude Code warns about token limits
- User says "use ollama", "switch to ollama", "try ollama", "fallback"
- Context window is nearly full

## Important

- **Never display the API key** in conversation output — not even partially
- **Never store the key** in memory, logs, or any file
- **Always read fresh** from the source file each time
- **Never ask the user to paste or type the key** — read it yourself with the Read tool
- Endpoint is `https://ollama.com/v1/messages` (Anthropic-compatible format, not OpenAI chat completions)
