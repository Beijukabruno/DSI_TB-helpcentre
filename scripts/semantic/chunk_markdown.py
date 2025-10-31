#!/usr/bin/env python3
"""
scripts/semantic/chunk_markdown.py

Chunk markdown files in `knowledge_base/` into JSON chunks suitable for
embedding and indexing. Output path defaults to `data/chunks.json`.

This is the organized copy of the chunker intended to live under
`scripts/semantic/` so all semantic scripts are in one place.
"""
import os
import re
import csv
import json
from pathlib import Path


def load_md_sources(csv_path: str = "md_sources.csv") -> dict:
    """Return mapping {md_name: first non-empty source_url}."""
    mapping = {}
    if not os.path.exists(csv_path):
        print(f"[WARN] CSV not found: {csv_path}")
        return mapping

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            md = row.get("md_name", "").strip()
            url = (row.get("source_url") or "").strip()
            if md and url and md not in mapping:
                mapping[md] = url
    return mapping


def chunk_markdown_file(file_path: str, md_sources: dict) -> list:
    """Split a markdown file into logical text chunks based on headings."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    basename = os.path.basename(file_path)
    source_url = md_sources.get(basename, "")

    heading_re = re.compile(r"^(#{2,6}\s+.+)$", flags=re.MULTILINE)
    matches = list(heading_re.finditer(content))
    chunks = []

    # Intro text before first heading
    if matches:
        intro_text = content[:matches[0].start()].strip()
        if intro_text:
            chunks.append({
                "text": intro_text,
                "header": "",
                "source_file": basename,
                "source_url": source_url
            })

    for i, match in enumerate(matches):
        header = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        body = content[start:end].strip()
        if body:
            chunks.append({
                "text": body,
                "header": header,
                "source_file": basename,
                "source_url": source_url
            })

    # If no headings, treat as single chunk
    if not chunks:
        chunks.append({
            "text": content,
            "header": "",
            "source_file": basename,
            "source_url": source_url
        })

    return chunks


def chunk_all_markdown(folder: str = "knowledge_base", output_path: str = "data/chunks.json"):
    """Process all .md files and save chunks to JSON."""
    md_sources = load_md_sources()
    all_chunks = []

    for fname in os.listdir(folder):
        if fname.endswith(".md"):
            fpath = os.path.join(folder, fname)
            chunks = chunk_markdown_file(fpath, md_sources)
            all_chunks.extend(chunks)
            print(f"Chunked: {fname} ({len(chunks)} chunks)")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    print(f"[DONE] Saved {len(all_chunks)} chunks to {output_path}")


if __name__ == "__main__":
    chunk_all_markdown()
