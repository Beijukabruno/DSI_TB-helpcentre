# Use official Python image
FROM python:3.10-slim

WORKDIR /app

RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Note: Do NOT bake secrets into images. GEMMA_API_KEY must be provided at runtime
# (via --env, --env-file, Docker/Kubernetes secrets, or a secret manager).
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]