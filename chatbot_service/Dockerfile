FROM python:3.10-slim

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git \
    && rm -rf /var/lib/apt/lists/*

# Install PyTorch CPU wheel for sentence-transformers
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Add GEMMA_API_KEY as a build argument and environment variable
ARG GEMMA_API_KEY
ENV GEMMA_API_KEY=$GEMMA_API_KEY

ENV PYTHONPATH="/app:$PYTHONPATH"

# Copy app code
COPY consolidated_chatbot.py ./
COPY entrypoint.sh ./
COPY . .

RUN chmod +x ./entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]