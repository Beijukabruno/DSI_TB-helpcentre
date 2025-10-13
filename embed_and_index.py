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
    metadata = {
        "header": chunk["header"],
        "source_file": chunk["source_file"],
        "chunk_id": f"{chunk['source_file']}_{i}"
    }
    collection.add(
        embeddings=[embedding],
        documents=[chunk['text']],
        metadatas=[metadata]
    )
print("Indexing complete.")