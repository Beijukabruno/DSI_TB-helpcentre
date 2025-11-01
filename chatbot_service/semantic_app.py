from fastapi import FastAPI
from pydantic import BaseModel
from routes.semantic_search_api import router as search_router
from typing import Any

app = FastAPI(
    title="TB Help Centre - Semantic Search (no-LLM)",
    description="Semantic search API over the TB knowledge base. Returns relevant document chunks without calling an LLM.",
    version="1.0.0"
)


class HealthResponse(BaseModel):
    status: str

@app.get("/health", response_model=HealthResponse, tags=["Health"])
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.get("/ready", tags=["Health"])
def ready() -> Any:
    return {"ready": True, "mode": "semantic-only"}


app.include_router(search_router)
