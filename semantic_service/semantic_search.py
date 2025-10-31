from sentence_transformers import SentenceTransformer
import chromadb
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
model_name = os.environ.get('EMBEDDING_MODEL', 'all-MiniLM-L6-v2')
print(f"Loading embedding model: {model_name}")
model = SentenceTransformer(model_name)
persist_directory = str(BASE_DIR / "vector_db")
client = chromadb.PersistentClient(path=persist_directory)
collection = client.get_or_create_collection(name="DSI_TB")


def search(query, k=3):
    embedding = model.encode(query)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=k
    )
    return results


if __name__ == "__main__":
    user_query = "What are the side effects of TB treatment?"
    results = search(user_query)
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        print(f"Text: {doc}\nSource: {meta['source_file']}\nSection: {meta['header']}\n")
