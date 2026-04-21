#!/usr/bin/env python3
"""
test_search.py

Run a semantic query against the local ChromaDB collection and
print the top-k results with document metadata.

Usage:
  python3 test_search.py "How is TB spread?" 5
"""

import sys
import json
import chromadb
from sentence_transformers import SentenceTransformer

VECTOR_DB_PATH = "vector_db"
COLLECTION_NAME = "DSI_TB"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def load_model():
    """Load the MiniLM embedding model (no auth required)."""
    print(f"Loading embedding model: {EMBED_MODEL}")
    return SentenceTransformer(EMBED_MODEL, use_auth_token=False)


def connect_chromadb():
    """Connect to the persistent Chroma database."""
    print(f"Connecting to ChromaDB at '{VECTOR_DB_PATH}'...")
    client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
    try:
        collection = client.get_collection(COLLECTION_NAME)
        print(f"Connected to collection '{COLLECTION_NAME}' "
              f"({collection.count()} records)")
    except Exception:
        print(f"Collection '{COLLECTION_NAME}' not found, creating a new one.")
        collection = client.get_or_create_collection(COLLECTION_NAME)
    return collection


def run_query(model, collection, query_text, top_k=5):
    """Embed the query and return the top-k most similar results."""
    print(f"\nRunning query: \"{query_text}\" (top {top_k})")
    query_embedding = model.encode([query_text]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]
    dists = results.get("distances", [[]])[0]

    formatted = []
    for doc, meta, dist in zip(docs, metas, dists):
        formatted.append({
            "text_preview": (doc[:250] + "...") if len(doc) > 250 else doc,
            "distance": round(dist, 4),
            "header": meta.get("header", ""),
            "source_file": meta.get("source_file", ""),
            "source_url": meta.get("source_url", "")
        })
    return formatted


def main():
    # Parse CLI args
    query_text = sys.argv[1] if len(sys.argv) > 1 else "How is TB spread?"
    top_k = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    try:
        model = load_model()
        collection = connect_chromadb()
        results = run_query(model, collection, query_text, top_k)

        print("\nResults:")
        print(json.dumps({"query": query_text, "results": results}, indent=2))

    except Exception as e:
        print(f"Error: {type(e).__name__} — {e}")
        raise


if __name__ == "__main__":
    main()