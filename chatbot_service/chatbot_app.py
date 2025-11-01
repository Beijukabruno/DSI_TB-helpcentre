from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, List
# Use the local semantic_search module copied into this service folder. When
# running via `uvicorn chatbot_service.chatbot_app:app` the package context
# makes the relative import predictable.
from . import semantic_search
from chatbot_service.call_gemma import call_gemma_model


app = FastAPI(title="TB Help Centre - Chatbot (LLM)")


class ChatRequest(BaseModel):
    query: str
    k: int = 5


class ChatResponse(BaseModel):
    query: str
    answer: str
    sources: List[dict]
    llm_model: str


def build_prompt(user_query: str, results: dict) -> str:
    prompt = (
        "You are a TB help centre assistant. Answer the following question using ONLY the provided information. "
        "Always cite the source for each fact.\n\n"
        f"Question: {user_query}\n\nRelevant Information:\n"
    )

    docs = results.get('documents', [[]])[0]
    metas = results.get('metadatas', [[]])[0]
    for i, (doc, meta) in enumerate(zip(docs, metas), 1):
        header = meta.get('header', '')
        src = meta.get('source_file', '') or meta.get('source_url', '') or 'unknown'
        prompt += f"{i}. {doc}\n(Source: {src}, Section: {header})\n"

    prompt += "\nYour answer:"
    return prompt


@app.post('/chat', response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    # Do semantic search to retrieve chunks
    try:
        results = semantic_search.search(req.query, k=req.k)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Semantic search failed: {e}")

    prompt = build_prompt(req.query, results)

    try:
        gen = call_gemma_model(prompt, model_name='gemma-3-4b-it')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM call failed: {e}")

    # Build sources list
    metas = results.get('metadatas', [[]])[0]
    docs = results.get('documents', [[]])[0]
    sources = []
    for doc, meta in zip(docs, metas):
        sources.append({
            'source_file': meta.get('source_file', ''),
            'header': meta.get('header', ''),
            'source_url': meta.get('source_url', ''),
            'excerpt': (doc[:300] + '...') if len(doc) > 300 else doc
        })

    return ChatResponse(
        query=req.query,
        answer=gen.get('response', ''),
        sources=sources,
        llm_model=gen.get('llm_model', 'gemma-3-4b-it')
    )


@app.get('/health')
def health() -> Any:
    return {"status": "ok"}
