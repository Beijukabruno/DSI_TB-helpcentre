# Use official Python image
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG GEMMA_API_KEY=""
ENV GEMMA_API_KEY=${GEMMA_API_KEY}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]