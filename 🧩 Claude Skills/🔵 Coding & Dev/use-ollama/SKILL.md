---
name: use-ollama
description: |-
  Switch the current session to route queries through Ollama Cloud free-tier models.
  TRIGGER when: the user invokes /use-ollama, says "use ollama", "switch to ollama", or "use nemotron/gemma/gpt-oss".
  Reads the API key silently and handles all subsequent prompts by calling Ollama via Bash.
---

# Use Ollama — Session Model Switch

When invoked, switch this session to use Ollama Cloud instead of Claude for answering prompts.

## On Invocation

1. **Read the key silently** using the Read tool — never display it.
   File: `C:\Users\muras\OneDrive\Desktop\tokesn\Ollama Cloud Keys.txt`
   Parse the value between the quotes on the `$env:=` line.

2. **Check for a model argument** in ARGUMENTS:
   - If a model name is provided, use it
   - If no argument, default to `nemotron-3-ultra:cloud`

3. **Confirm to the user:**
   > Now using `<model>` via Ollama Cloud. Send me your prompt.

4. **For every subsequent user prompt**, call the model via Bash:

```bash
curl -s https://ollama.com/v1/messages \
  -H "authorization: Bearer <key>" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d "{\"model\": \"<model>\", \"max_tokens\": 1024, \"messages\": [{\"role\": \"user\", \"content\": \"<prompt>\"}]}"
```

5. **Extract and return only the text response** — parse `content[].text` from the JSON, ignore thinking blocks unless the user asks to see them.

## Available Free Models

| Model | Notes |
|---|---|
| `nemotron-3-ultra:cloud` | Best quality, NVIDIA reasoning model (default) |
| `nemotron-3-super:cloud` | Heavy thinker — use max_tokens ≥ 500 |
| `gpt-oss:20b-cloud` | General use, has thinking |
| `gemma4:cloud` | Fastest, lightest |

## Rules

- **Never display the API key** — read and use it silently via Bash only
- **Always read fresh** from the key file each time — never cache it
- Use `max_tokens: 1024` by default; bump to `2048` if the user asks for long output
- For `nemotron-3-super`, use `max_tokens: 500` minimum or it burns tokens on thinking alone
