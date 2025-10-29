from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import semantic_search

router = APIRouter()


class SearchRequest(BaseModel):
    query: str
    k: int = 5


class Match(BaseModel):
    header: str
    source_file: str
    link: str | None = None
    markdown: str


class SearchResponse(BaseModel):
    query: str
    total_matches: int
    matches: List[Match]


@router.post("/search", response_model=SearchResponse)
def semantic_search_endpoint(req: SearchRequest):
    """Perform a semantic search over the indexed knowledge base.

    Returns the top-k matching chunks as markdown snippets with simple provenance.
    This endpoint intentionally does not call any LLM; it only returns stored
    document chunks returned by the vector store.
    """
    try:
        results = semantic_search.search(req.query, k=req.k)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    matches = []
    for doc, meta in zip(documents, metadatas):
        matches.append(Match(
            header=meta.get("header", ""),
            source_file=meta.get("source_file", ""),
            link=meta.get("link", ""),
            markdown=doc
        ))

    return SearchResponse(query=req.query, total_matches=len(matches), matches=matches)
