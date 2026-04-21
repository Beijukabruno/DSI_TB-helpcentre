#!/usr/bin/env python3
"""
scripts/semantic/embed_and_index.py

Embed chunks from `data/chunks.json` and persist them into a ChromaDB
collection located at `vector_db/`.

This organized script lives under `scripts/semantic/`.
"""
import os
import json
from pathlib import Path
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
import chromadb

# Constants
CHUNKS_PATH = os.environ.get('CHUNKS_PATH', 'data/chunks.json')
PERSIST_DIR = os.environ.get('PERSIST_DIR', 'vector_db')
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'DSI_TB')
MODEL_NAME = os.environ.get('EMBEDDING_MODEL', 'all-MiniLM-L6-v2')
BATCH_SIZE = int(os.environ.get('BATCH_SIZE', '64'))


def main():
    # Validate input
    if not Path(CHUNKS_PATH).exists():
        raise FileNotFoundError(f"Chunks file not found: {CHUNKS_PATH}")
    with open(CHUNKS_PATH, 'r', encoding='utf-8') as f:
        chunks = json.load(f)
    print(f"Loaded {len(chunks)} chunks from {CHUNKS_PATH}")

    # Connect to Chroma
    print(f"Connecting to ChromaDB (persist dir: {PERSIST_DIR})...")
    client = chromadb.PersistentClient(path=PERSIST_DIR)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    # Load model
    print(f"Loading embedding model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)

    # Prepare batches
    ids, texts, metadatas = [], [], []
    for i, chunk in enumerate(chunks):
        text = chunk.get('text', '').strip()
        if not text:
            continue
        cid = f"{chunk.get('source_file','unknown')}_{i}"
        meta = {
            'header': chunk.get('header',''),
            'source_file': chunk.get('source_file',''),
            'source_url': chunk.get('source_url',''),
        }
        ids.append(cid)
        texts.append(text)
        metadatas.append(meta)

    print(f"Indexing {len(texts)} chunks in batches of {BATCH_SIZE}...")
    for start in tqdm(range(0, len(texts), BATCH_SIZE)):
        batch_texts = texts[start:start+BATCH_SIZE]
        batch_ids = ids[start:start+BATCH_SIZE]
        batch_metas = metadatas[start:start+BATCH_SIZE]

        embeddings = model.encode(batch_texts, convert_to_numpy=True, show_progress_bar=False)
        try:
            emb_list = embeddings.tolist()
        except Exception:
            emb_list = embeddings

        collection.add(
            ids=batch_ids,
            embeddings=emb_list,
            documents=batch_texts,
            metadatas=batch_metas
        )

    print(f"Indexing complete. Persisted in '{PERSIST_DIR}'")
    try:
        print(f"Total documents in collection: {collection.count()}")
    except Exception:
        pass


if __name__ == '__main__':
    main()
