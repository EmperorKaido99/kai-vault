#!/bin/bash
# Requires: export OLLAMA_API_KEY="258ed4d1cb1a4dabbf34a1837aefaf43.xaxjOuZJpsceroUHJXFd8aDU" before running

if [ -z "$OLLAMA_API_KEY" ]; then
  echo "Set OLLAMA_API_KEY first: export OLLAMA_API_KEY=\"258ed4d1cb1a4dabbf34a1837aefaf43.xaxjOuZJpsceroUHJXFd8aDU\""
  exit 1
fi

# Free-tier cloud models confirmed working as of 2026-09-05.
# Check ollama.com/library for the current live list/tags before relying on this.
MODELS=(
  "gpt-oss:20b-cloud"
  "gemma4:cloud"
  "nemotron-3-super:cloud"
  "nemotron-3-ultra:cloud"
)

for MODEL in "${MODELS[@]}"; do
  echo "=================================================="
  echo "Testing: $MODEL"
  echo "=================================================="
  curl -s https://ollama.com/v1/messages \
    -H "authorization: Bearer $OLLAMA_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d "{\"model\": \"$MODEL\", \"max_tokens\": 100, \"messages\": [{\"role\": \"user\", \"content\": \"Say hello and name yourself in one sentence.\"}]}"
  echo -e "\n"
  sleep 2   # free tier allows 1 concurrent request — avoid overlapping calls
done
