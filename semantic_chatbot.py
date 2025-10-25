import os
import re
import json
from sentence_transformers import SentenceTransformer
import chromadb
from dotenv import load_dotenv
import google.generativeai as genai
import pandas as pd

# --- Load environment variables ---
load_dotenv()
GEMMA_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- 1. Chunk Markdown Files ---
def extract_sources(content):
    # Find *Sources: [text](url), [text](url)* at the top
    sources_match = re.search(r'\\*Sources:([\\s\\S]*?)\\*', content)
    sources = []
    if sources_match:
        sources_text = sources_match.group(1)
        sources += re.findall(r'\\[.*?\\]\\((.*?)\\)', sources_text)
    # Find resource links at the end (e.g., - [text](url))
    resources = re.findall(r'- \\[.*?\\]\\((.*?)\\)', content)
    sources += resources
    return list(set(sources))  # Remove duplicates

def get_sources_for_md(md_name, csv_path="md_sources.csv"):
    df = pd.read_csv(csv_path)
    sources = df[df["md_name"] == md_name]["source_url"].drop_duplicates()
    sources = sources[sources.notnull() & (sources != "")]
    # Return only the first link for each chunk
    return sources.iloc[0] if len(sources) > 0 else ""

def chunk_markdown_file(file_path, csv_path="md_sources.csv"):
    with open(file_path, 'r') as f:
        content = f.read()
    md_name = os.path.basename(file_path)
    link = get_sources_for_md(md_name, csv_path)
    chunks = re.split(r'(?:^|\n)(#+ .*)', content)
    result = []
    for i in range(1, len(chunks), 2):
        header = chunks[i].strip()
        text = chunks[i+1].strip()
        result.append({
            "text": text,
            "header": header,
            "source_file": md_name,
            "link": link
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
            "link": chunk.get("link", "")
        }
        collection.add(
            ids=[metadata["chunk_id"]],
            embeddings=[embedding],
            documents=[chunk['text']],
            metadatas=[metadata]
        )
    print("Indexing complete.")

# --- 3. Semantic Search ---
def semantic_search(query, k=5, persist_directory="Vector_db", collection_name="DSI_TB"):
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
        "Always cite your sources using the provided links wherever possible.\n\n"
        f"Question: {user_query}\n\nRelevant Information:\n"
    )
    for i, (doc, meta) in enumerate(zip(results['documents'][0], results['metadatas'][0]), 1):
        link = meta.get('link', '')
        prompt += f"{i}. {doc} [Source: {meta['source_file']}, Link: {link}]\n"
    prompt += "\nYour answer:"
    return prompt

# --- 5. Call Gemma LLM ---
def call_gemma_model(prompt: str, model_name: str = 'gemma-3-4b-it') -> dict:
    # Optional local mock mode for CI/testing: set MOCK_GEMMA=true in env to skip external calls
    if os.getenv("MOCK_GEMMA", "false").lower() == "true":
        return {"response": "[MOCK] This is a canned response used for testing.", "llm_model": "mock", "llm_model_version": "0.0"}

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
        # Detect common Google API errors and provide actionable guidance
        if "SERVICE_DISABLED" in error_msg or "generativelanguage.googleapis.com" in error_msg:
            activation_url = None
            # Try extracting activation URL from the message
            m = re.search(r'(https?://[\w\-./?=&%:]+generativelanguage\.googleapis\.com[\w\-./?=&%:]*)', error_msg)
            if m:
                activation_url = m.group(1)
            # Fallback to the console activation link pattern
            if not activation_url:
                activation_url = "https://console.developers.google.com/apis/api/generativelanguage.googleapis.com/overview"
            raise RuntimeError(
                f"Generative Language API appears disabled for your Google Cloud project. Enable it in the Cloud Console: {activation_url}\nOriginal error: {error_msg}"
            )
        if "API_KEY_INVALID" in error_msg or "API key not valid" in error_msg:
            raise ValueError(f"Invalid Gemma API key: {error_msg}")
        elif "quota" in error_msg.lower() or "rate limit" in error_msg.lower():
            raise RuntimeError(f"API quota exceeded or rate limited: {error_msg}")
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
    print(f"Total chunks created: {len(all_chunks)}")
    for chunk in all_chunks[:3]:  # Show first 3 chunks for inspection
        print("Sample chunk:", chunk)
    # Step 2: Index chunks (run once, comment out after DB is built)
    embed_and_index(all_chunks)
    # Step 3: Query loop
    print("Semantic Chatbot Ready. Type your TB-related question below.")
    while True:
        user_query = input("\nYour question (or 'exit' to quit): ")
        if user_query.lower() == "exit":
            break
        try:
            # Debug: Show semantic search results
            results = semantic_search(user_query)
            print("\nSemantic search results:")
            for i, (doc, meta) in enumerate(zip(results['documents'][0], results['metadatas'][0]), 1):
                print(f"Result {i}: {meta['header']} | {doc[:80]}...")
            # Debug: Show prompt sent to LLM
            prompt = build_prompt(user_query, results)
            print("\nPrompt sent to LLM:\n", prompt)
            # Call LLM and display answer
            response = call_gemma_model(prompt)
            print("\nAnswer:\n", response["response"])
            print("\nReferences:")
            for src in results['metadatas'][0]:
                refs = src.get("source_urls", '')
                if refs:
                    url_list = [url.strip() for url in refs.split(',') if url.strip()]
                    for url in url_list:
                        print(f"- {url}")
                else:
                    print(f"- {src['header']} | {src['source_file']}")
        except Exception as e:
            print("Error:", e)
