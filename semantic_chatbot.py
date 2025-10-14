
import os
import re
import json
from sentence_transformers import SentenceTransformer
import chromadb
from dotenv import load_dotenv
import google.generativeai as genai

# --- Load environment variables ---
load_dotenv()
GEMMA_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- 1. Chunk Markdown Files ---
def chunk_markdown_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    chunks = re.split(r'(?:^|\n)(##+ .*)', content)
    result = []
    for i in range(1, len(chunks), 2):
        header = chunks[i].strip()
        text = chunks[i+1].strip()
        # Extract source_url if present
        url_match = re.search(r'<!--\s*source_url:\s*(.*?)\s*-->', text)
        source_url = url_match.group(1) if url_match else None
        result.append({
            "text": re.sub(r'<!--.*?-->', '', text).strip(),
            "header": header,
            "source_file": os.path.basename(file_path),
            "source_url": source_url
        })
    return result

# --- 2. Embed and Index Chunks ---
def embed_and_index(chunks, persist_directory="Vector_db", collection_name="DSI_TB"):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    client = chromadb.PersistentClient(path=persist_directory)
    collection = client.get_or_create_collection(name=collection_name)
    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk['text'])
        metadata = {
            "header": chunk["header"],
            "source_file": chunk["source_file"],
            "chunk_id": f"{chunk['source_file']}_{i}",
            "source_url": chunk.get("source_url")
        }
        collection.add(
            ids=[metadata["chunk_id"]],
            embeddings=[embedding],
            documents=[chunk['text']],
            metadatas=[metadata]
        )
    print("Indexing complete.")

# --- 3. Semantic Search ---
def semantic_search(query, k=3, persist_directory="Vector_db", collection_name="DSI_TB"):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    client = chromadb.PersistentClient(path=persist_directory)
    collection = client.get_or_create_collection(name=collection_name)
    embedding = model.encode(query)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=k
    )
    return results

# --- 4. Build Prompt for LLM ---
def build_prompt(user_query, results):
    prompt = (
        "You are a TB help centre assistant. Answer the following question using ONLY the provided information. "
        "Always cite the source for each fact.\n\n"
        f"Question: {user_query}\n\nRelevant Information:\n"
    )
    for i, (doc, meta) in enumerate(zip(results['documents'][0], results['metadatas'][0]), 1):
        ref = meta.get('source_url') if meta.get('source_url') else f"{meta['source_file']}, Section: {meta['header']}"
        prompt += f"{i}. {doc} (Reference: {ref})\n"
    prompt += "\nYour answer:"
    return prompt

# --- 5. Call Gemma LLM ---
def call_gemma_model(prompt: str, model_name: str = 'gemma-3-4b-it') -> dict:
    if genai is None:
        raise ImportError("genai module not installed. Please install the Google GenAI SDK.")
    if not GEMMA_API_KEY or GEMMA_API_KEY == "your_gemma_api_key_here":
        raise ValueError("GEMMA_API_KEY environment variable is not set or is using placeholder value")
    genai.configure(api_key=GEMMA_API_KEY)
    model = genai.GenerativeModel(model_name)
    try:
        response = model.generate_content(prompt)
        model_version = model_name.split('-',1)[-1] if '-' in model_name else "unknown"
        return {
            "response": response.text,
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

# --- 6. End-to-End Orchestration ---
def answer_query(user_query, k=3):
    results = semantic_search(user_query, k=k)
    prompt = build_prompt(user_query, results)
    response = call_gemma_model(prompt)
    return {
        "answer": response['response'],
        "sources": [meta for meta in results['metadatas'][0]]
    }

if __name__ == "__main__":
    # Step 1: Chunk all markdown files in knowledge_base folder
    folder = "knowledge_base"
    all_chunks = []
    for fname in os.listdir(folder):
        if fname.endswith(".md"):
            chunks = chunk_markdown_file(os.path.join(folder, fname))
            all_chunks.extend(chunks)
    # Step 2: Index chunks (run once, comment out after DB is built)
    embed_and_index(all_chunks)
    # Step 3: Query loop
    print("Semantic Chatbot Ready. Type your TB-related question below.")
    while True:
        user_query = input("\nYour question (or 'exit' to quit): ")
        if user_query.lower() == "exit":
            break
        try:
            result = answer_query(user_query)
            print("\nAnswer:\n", result["answer"])
            print("\nReferences:")
            for src in result["sources"]:
                if src.get("source_url"):
                    print(f"- {src['header']} | {src['source_url']}")
                else:
                    print(f"- {src['header']} | {src['source_file']}")
        except Exception as e:
            print("Error:", e)
