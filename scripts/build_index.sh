#!/usr/bin/env bash
# Build index script
# Usage: ./scripts/build_index.sh
# This will build the Docker image (if not present) and run the indexing step in a container, producing ./Vector_db

set -euo pipefail

# Ensure Vector_db dir exists
mkdir -p Vector_db

# Build the image (local tag tb-chatbot)
docker build -t tb-chatbot .

# Run the indexer in a temporary container. It will create/overwrite Vector_db/ in the project root.
# The container runs: python chunk_markdown.py && python embed_and_index.py

docker run --rm \
  -v "$(pwd)/Vector_db:/app/Vector_db" \
  -v "$(pwd):/app" \
  --env-file .env \
  tb-chatbot \
  /bin/sh -c "python chunk_markdown.py && python embed_and_index.py"

echo "Indexing complete. Vector_db/ populated."
