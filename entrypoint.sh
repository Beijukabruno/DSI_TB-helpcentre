#!/bin/sh
set -euo pipefail

echo "Starting semantic-only container entrypoint"

# If Vector_db doesn't exist, build the index from knowledge_base
if [ ! -d ./Vector_db ] || [ -z "$(ls -A ./Vector_db 2>/dev/null || true)" ]; then
  echo "Vector_db not found or empty — building index from knowledge_base. This may take several minutes."
  # Run chunking and indexing (these scripts are expected to exist in the image)
  if [ -f ./chunk_markdown.py ] && [ -f ./embed_and_index.py ]; then
    python chunk_markdown.py
    python embed_and_index.py
    echo "Indexing complete. Vector_db/ created."
  else
    echo "Indexing scripts not found — cannot build Vector_db. Exiting." >&2
    exit 1
  fi
else
  echo "Vector_db exists — skipping indexing."
fi

echo "Starting Uvicorn"
exec uvicorn semantic_app:app --host 0.0.0.0 --port 8000
