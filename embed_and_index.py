# embed_and_index.py
import json
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')
persist_directory = "Vector_db"
client = chromadb.PersistentClient(path=persist_directory)
collection = client.get_or_create_collection(name="DSI_TB")

with open("chunks.json") as f:
    chunks = json.load(f)

for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk['text'])
    # Ensure embedding is a plain Python list (Chromadb-friendly)
    try:
        embedding_list = embedding.tolist()
    except Exception:
        embedding_list = embedding

    # Normalize metadata fields to avoid None values (Chromadb requires primitive types)
    header = chunk.get("header") or ""
    source_file = chunk.get("source_file") or ""
    source_url = chunk.get("source_url") or ""
    metadata = {
        "header": str(header),
        "source_file": str(source_file),
        "chunk_id": f"{source_file}_{i}",
        "source_url": str(source_url)
    }
    collection.add(
        ids=[metadata["chunk_id"]],
        embeddings=[embedding_list],
        documents=[chunk['text']],
        metadatas=[metadata]
    )
print("Indexing complete.")