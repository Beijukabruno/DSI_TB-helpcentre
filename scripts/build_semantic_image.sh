#!/bin/bash
set -euo pipefail

# Usage: ./scripts/build_semantic_image.sh <dockerhub-username>
USER=${1:-beijuka}
TAG="$USER/tb-chatbot-semantic:latest"

echo "Building semantic-only docker image: $TAG"
docker build -f Dockerfile.semantic -t "$TAG" .
echo "Built $TAG"
