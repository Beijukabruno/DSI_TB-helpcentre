from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import semantic_search

router = APIRouter(prefix="/api", tags=["Semantic Search"])


class SearchRequest(BaseModel):
    """Incoming request for semantic search."""
    query: str = Field(..., description="User query string.")
    k: int = Field(5, ge=1, le=20, description="Number of top results to return (default: 5).")


class Match(BaseModel):
    """Single semantic match returned from vector search."""
    header: str = Field("", description="Section header or title of the source chunk.")
    source_file: str = Field("", description="Filename where this chunk was found.")
    link: Optional[str] = Field(None, description="Optional source URL or document link.")
    markdown: str = Field(..., description="Markdown-formatted text snippet.")


class SearchResponse(BaseModel):
    """Full semantic search response."""
    query: str
    total_matches: int
    matches: List[Match]


@router.post("/search", response_model=SearchResponse)
def semantic_search_endpoint(req: SearchRequest) -> SearchResponse:
    """
    Perform a semantic search over the indexed knowledge base.

    This endpoint retrieves the most semantically similar document chunks
    from the local ChromaDB vector store using the SentenceTransformer embeddings.

    Returns:
        A list of markdown snippets with metadata (header, file source, link).
    """
    try:
        results = semantic_search.search(req.query, k=req.k)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {e}")

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    matches = []
    for doc, meta in zip(documents, metadatas):
        # Clean up metadata keys
        match = Match(
            header=meta.get("header", ""),
            source_file=meta.get("source_file", ""),
            link=meta.get("source_url") or meta.get("link"),
            markdown=doc.strip(),
        )
        matches.append(match)

    return SearchResponse(
        query=req.query,
        total_matches=len(matches),
        matches=matches
    )