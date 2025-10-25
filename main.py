
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from semantic_chatbot import answer_query, chunk_markdown_file
import logging
import os

app = FastAPI()
logger = logging.getLogger("uvicorn.error")

class QueryRequest(BaseModel):
    question: str
    k: int = 3

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/chunks")
def get_chunks():
    folder = "knowledge_base"
    all_chunks = []
    for fname in os.listdir(folder):
        if fname.endswith(".md"):
            chunks = chunk_markdown_file(os.path.join(folder, fname))
            all_chunks.extend(chunks)
    return {"total_chunks": len(all_chunks), "chunks": all_chunks}

@app.post("/chatbot")
async def chatbot_endpoint(request: QueryRequest):
    try:
        result = answer_query(request.question, k=request.k)
        # Compute total_chunks from the knowledge_base folder (simple, deterministic)
        folder = "knowledge_base"
        total_chunks = 0
        for fname in os.listdir(folder):
            if fname.endswith(".md"):
                total_chunks += len(chunk_markdown_file(os.path.join(folder, fname)))

        # Return matched chunks and their metadata
        return {
            "answer": result["answer"],
            "sources": result["sources"],
            "meta": {
                "total_chunks": total_chunks,
                "matched_chunks": len(result["sources"]),
                "matched_metadata": result["sources"]
            }
        }
    except RuntimeError as e:
        # Likely an actionable runtime error (e.g., disabled external API)
        logger.error(f"Failed to process query (runtime): {str(e)}")
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        logger.error(f"Failed to process query: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error. Please try again later.")

@app.get("/")
def root():
    return {"message": "TB Help Centre Chatbot API is running."}


@app.get("/ready")
def readiness():
    """Readiness endpoint: reports whether the app is in mock mode or has an API key configured.

    This is a lightweight check and does not perform external API calls.
    """
    mock_mode = os.getenv("MOCK_GEMMA", "false").lower() == "true"
    api_key_present = bool(os.getenv("GOOGLE_API_KEY"))
    ready = mock_mode or api_key_present
    return {
        "ready": ready,
        "mode": "mock" if mock_mode else "live",
        "api_key_present": api_key_present
    }
