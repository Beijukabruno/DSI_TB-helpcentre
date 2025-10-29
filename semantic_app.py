from fastapi import FastAPI
from pydantic import BaseModel
from routes.semantic_search_api import semantic_search_endpoint
from typing import Any
import routes.semantic_search_api as api

app = FastAPI(title="TB Help Centre - Semantic Search (no-LLM)")


class Health(BaseModel):
    status: str


@app.get("/health")
def health() -> Health:
    return Health(status="ok")


@app.post("/search")
def search_proxy(body: api.SearchRequest):
    """Proxy to the semantic-search-only endpoint (keeps a flat single-file entrypoint).

    This endpoint intentionally calls the semantic-search implementation and
    returns the same exact structured response (no LLM involvement).
    """
    return api.semantic_search_endpoint(body)


@app.get("/ready")
def ready() -> Any:
    # Always ready for semantic-search-only image (no external API required).
    return {"ready": True, "mode": "semantic-only"}
