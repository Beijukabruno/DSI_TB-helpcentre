#!/usr/bin/env bash
set -euo pipefail

# scripts/run_pipeline.sh
# Simple pipeline to validate CSV coverage, chunk markdown, index, and run a test query.
# Usage:
#   source .venv/bin/activate
#   bash scripts/run_pipeline.sh

ROOT_DIR=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT_DIR"

echo "1) Check md_sources coverage"
python3 scripts/report_missing_sources.py

echo "\n2) Chunk markdown files into data/chunks.json (semantic_service)"
python3 semantic_service/scripts/chunk_markdown.py

echo "\n3) Rebuild semantic_service/vector_db (this will download embedding model if needed)"
rm -rf semantic_service/vector_db || true
python3 semantic_service/scripts/embed_and_index.py

echo "\n4) Run a quick semantic test query"
python3 semantic_service/scripts/test_search.py "How is TB spread?" 5

echo "\nPipeline complete. If results above show links and source_url, good to go."