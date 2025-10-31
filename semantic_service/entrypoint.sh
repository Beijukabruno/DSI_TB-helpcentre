#!/bin/sh
set -euo pipefail

echo "[semantic-service] Starting container..."

cd /app || { echo "Failed to cd into /app"; exit 1; }

if [ ! -d ./vector_db ] || [ -z "$(ls -A ./vector_db 2>/dev/null || true)" ]; then
  echo "[semantic-service] vector_db not found or empty — building index from knowledge_base (this may take a few minutes)..."

  if [ -f ./scripts/chunk_markdown.py ] && [ -f ./scripts/embed_and_index.py ]; then
    python scripts/chunk_markdown.py
    python scripts/embed_and_index.py
    echo "[semantic-service] ✅ Indexing complete — vector_db/ created."
  else
    echo "[semantic-service] ❌ Indexing scripts not found — cannot build vector_db. Exiting." >&2
    exit 1
  fi
else
  echo "[semantic-service] vector_db exists — skipping indexing."
fi

echo "[semantic-service] Starting Uvicorn on 0.0.0.0:8000 ..."
exec uvicorn semantic_app:app --host 0.0.0.0 --port 8000
