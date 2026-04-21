from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel, Field, conint
from typing import Any, List, Optional, Dict
from sentence_transformers import SentenceTransformer
import chromadb
import os
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
from transformers import pipeline
from chatbot_service.guardrail import guard_input, guard_output

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="TB Help Centre - Chatbot Service",
    description="Chatbot API for interacting with the TB knowledge base.",
    version="1.0.0"
)

# Rating request model
class RatingRequest(BaseModel):
    rating: conint(ge=1, le=5)  # Ensures rating is between 1 and 5

# Endpoint to capture user rating
@app.post("/rate")
async def rate_service(rating_request: RatingRequest):
    rating = rating_request.rating
    # TODO: Save the rating to a database or file
    # For now, just acknowledge receipt
    return {"message": "Thank you for your feedback!", "rating": rating}
# Initialize embedding model and database
BASE_DIR = Path(__file__).resolve().parent
model_name = os.environ.get('EMBEDDING_MODEL', 'all-MiniLM-L6-v2')
print(f"Loading embedding model: {model_name}")
model = SentenceTransformer(model_name)
persist_directory = str(BASE_DIR / "vector_db")
client = chromadb.PersistentClient(path=persist_directory)
collection = client.get_or_create_collection(name="DSI_TB")

# Helper functions
def search(query, k=5):
    embedding = model.encode(query)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=k
    )
    return results

def call_gemma_model(prompt: str, model_name: str = 'gemma-3-4b-it') -> Dict:
    api_key = os.getenv("GEMMA_API_KEY")
    if not api_key or api_key == "your_gemma_api_key_here":
        raise ValueError("GEMMA_API_KEY environment variable is not set or is using placeholder value")

    genai.configure(api_key=api_key)

    try:
        model = genai.GenerativeModel(model_name)
    except Exception:
        try:
            model = getattr(genai, 'GenerativeModel')(model_name)
        except Exception as e:
            raise RuntimeError(f"Failed to construct Gemma model client: {e}")

    try:
        response = model.generate_content(prompt)
        model_version = model_name.split('-', 1)[-1] if '-' in model_name else "unknown"
        text = getattr(response, 'text', str(response))
        return {
            "response": text,
            "llm_model": model_name,
            "llm_model_version": model_version
        }
    except Exception as e:
        error_msg = str(e)
        if "API_KEY_INVALID" in error_msg or "API key not valid" in error_msg:
            raise ValueError(f"Invalid Gemma API key: {error_msg}")
        elif "quota" in error_msg.lower() or "rate limit" in error_msg.lower():
            raise ValueError(f"API quota exceeded or rate limited: {error_msg}")
        else:
            raise Exception(f"Failed to generate model response: {error_msg}")

# API Models
class ChatRequest(BaseModel):
    query: str
    k: int = 5

class ChatResponse(BaseModel):
    query: str
    answer: str
    sources: List[dict]
    llm_model: str
    toxicity_input: dict
    toxicity_output: Optional[Dict] = None

class HealthResponse(BaseModel):
    status: str

class SearchRequest(BaseModel):
    query: str = Field(..., description="User query string.")
    k: int = Field(5, ge=1, le=20, description="Number of top results to return (default: 5).")

class Match(BaseModel):
    header: str = Field("", description="Section header or title of the source chunk.")
    source_file: str = Field("", description="Filename where this chunk was found.")
    link: Optional[str] = Field(None, description="Optional source URL or document link.")
    markdown: str = Field(..., description="Markdown-formatted text snippet.")

class SearchResponse(BaseModel):
    query: str
    total_matches: int
    matches: List[Match]
    toxicity_input: dict
    toxicity_output: Optional[Dict] = None
    message: Optional[str] = None

# Routes
@app.post('/chat', response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    # Guardrail on input
    proceed_in, label_in, score_in, safe_resp_in = guard_input(req.query)
    if not proceed_in:
        return ChatResponse(
            query=req.query,
            answer=safe_resp_in,
            sources=[],
            llm_model="guardrail",
            toxicity_input={"label": label_in, "score": score_in},
            toxicity_output=None
        )

    try:
        results = search(req.query, k=req.k)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Semantic search failed: {e}")

    # Fallback: if no chunks are retrieved, return default response
    docs = results.get('documents', [[]])[0]
    metas = results.get('metadatas', [[]])[0]
    if not docs or len(docs) == 0:
        fallback_msg = "Sorry, I could not find any relevant information for your question."
        return ChatResponse(
            query=req.query,
            answer=fallback_msg,
            sources=[],
            llm_model="none",
            toxicity_input={"label": label_in, "score": score_in},
            toxicity_output=None
        )

    prompt = build_prompt(req.query, results)

    try:
        gen = call_gemma_model(prompt, model_name='gemma-3-4b-it')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM call failed: {e}")

    # Guardrail on output
    proceed_out, label_out, score_out, safe_resp_out = guard_output(gen.get('response', ''))
    if not proceed_out:
        return ChatResponse(
            query=req.query,
            answer=safe_resp_out,
            sources=[],
            llm_model=gen.get('llm_model', 'gemma-3-4b-it'),
            toxicity_input={"label": label_in, "score": score_in},
            toxicity_output={"label": label_out, "score": score_out}
        )

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
        llm_model=gen.get('llm_model', 'gemma-3-4b-it'),
        toxicity_input={"label": label_in, "score": score_in},
        toxicity_output={"label": label_out, "score": score_out}
    )

@app.get("/health", response_model=HealthResponse, tags=["Health"])
def health() -> HealthResponse:
    return HealthResponse(status="ok")

@app.get("/ready", tags=["Health"])
def ready() -> Any:
    return {"ready": True, "mode": "chatbot"}

@app.post("/search", response_model=SearchResponse)
def semantic_search_endpoint(req: SearchRequest) -> SearchResponse:
    # Guardrail on input
    proceed_in, label_in, score_in, safe_resp_in = guard_input(req.query)
    if not proceed_in:
        return SearchResponse(
            query=req.query,
            total_matches=0,
            matches=[],
            toxicity_input={"label": label_in, "score": score_in},
            toxicity_output=None,
            message=safe_resp_in
        )

    try:
        results = search(req.query, k=req.k)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {e}")

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    matches = []
    for doc, meta in zip(documents, metadatas):
        match = Match(
            header=meta.get("header", ""),
            source_file=meta.get("source_file", ""),
            link=meta.get("source_url") or meta.get("link"),
            markdown=doc.strip(),
        )
        matches.append(match)

    # Guardrail on output (concatenate all docs)
    output_text = " ".join([m.markdown for m in matches])
    proceed_out, label_out, score_out, safe_resp_out = guard_output(output_text)
    if not proceed_out:
        return SearchResponse(
            query=req.query,
            total_matches=0,
            matches=[],
            toxicity_input={"label": label_in, "score": score_in},
            toxicity_output={"label": label_out, "score": score_out}
        )

    return SearchResponse(
        query=req.query,
        total_matches=len(matches),
        matches=matches,
        toxicity_input={"label": label_in, "score": score_in},
        toxicity_output={"label": label_out, "score": score_out}
    )

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