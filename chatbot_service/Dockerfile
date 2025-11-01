FROM python:3.10-slim

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install PyTorch CPU wheel for sentence-transformers
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the service into the image. This Dockerfile is intended to be built from
# the `chatbot_service` directory as build context (for CI you can set the build
# context to the repo root and copy both chatbot_service and semantic_service).
COPY . .

RUN chmod +x ./entrypoint.sh || true

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]