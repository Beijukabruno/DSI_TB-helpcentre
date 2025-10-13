# semantic_search.py
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')
persist_directory = "Vector_db"
client = chromadb.PersistentClient(path=persist_directory)
collection = client.get_or_create_collection(name="DSI_TB")

def search(query, k=3):
    embedding = model.encode(query)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=k
    )
    # Each result contains: document, metadata
    return results

# Example usage
if __name__ == "__main__":
    user_query = "What are the side effects of TB treatment?"
    results = search(user_query)
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        print(f"Text: {doc}\nSource: {meta['source_file']}\nSection: {meta['header']}\n")