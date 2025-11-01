#!/bin/sh
set -euo pipefail

echo "[chatbot-service] Starting container..."

cd /app || { echo "Failed to cd into /app"; exit 1; }

if [ ! -d ./chatbot_service/vector_db ] || [ -z "$(ls -A ./chatbot_service/vector_db 2>/dev/null || true)" ]; then
  echo "[chatbot-service] vector_db not found or empty — building index from knowledge_base (this may take a few minutes)..."

  if [ -f ./chatbot_service/scripts/chunk_markdown.py ] && [ -f ./chatbot_service/scripts/embed_and_index.py ]; then
    python chatbot_service/scripts/chunk_markdown.py
    python chatbot_service/scripts/embed_and_index.py
    echo "[chatbot-service] Indexing complete — chatbot_service/vector_db created."
  else
    echo "[chatbot-service] Indexing scripts not found — cannot build vector_db. Exiting." >&2
    exit 1
  fi
else
  echo "[chatbot-service] vector_db exists — skipping indexing."
fi

echo "[chatbot-service] Starting Uvicorn on 0.0.0.0:8000 ..."
exec uvicorn chatbot_service.chatbot_app:app --host 0.0.0.0 --port 8000
