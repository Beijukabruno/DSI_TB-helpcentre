#!/usr/bin/env python3
"""
semantic_service/scripts/chunk_markdown.py

Chunk markdown files located in the service `knowledge_base/` directory into
`data/chunks.json` inside the service. This script is self-contained and uses
paths relative to the semantic_service root so the service can be moved/copied.
"""
import os
import re
import csv
import json
from pathlib import Path


# BASE_DIR should point to the semantic_service root (one parent up from scripts)
BASE_DIR = Path(__file__).resolve().parents[1]
KB_DIR = BASE_DIR / "knowledge_base"
CSV_PATH = BASE_DIR / "md_sources.csv"
OUTPUT_PATH = BASE_DIR / "data" / "chunks.json"


def load_md_sources(csv_path: str = str(CSV_PATH)) -> dict:
    mapping = {}
    p = Path(csv_path)
    if not p.exists():
        print(f"[WARN] CSV not found: {csv_path}")
        return mapping

    with p.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            md = row.get("md_name", "").strip()
            url = (row.get("source_url") or "").strip()
            if md and url and md not in mapping:
                mapping[md] = url
    return mapping


def chunk_markdown_file(file_path: Path, md_sources: dict) -> list:
    with file_path.open(encoding='utf-8') as f:
        content = f.read().strip()

    basename = file_path.name
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

    if not chunks:
        chunks.append({
            "text": content,
            "header": "",
            "source_file": basename,
            "source_url": source_url
        })

    return chunks


def chunk_all_markdown(folder: Path = KB_DIR, output_path: Path = OUTPUT_PATH):
    md_sources = load_md_sources()
    all_chunks = []
    for p in sorted(folder.glob('*.md')):
        chunks = chunk_markdown_file(p, md_sources)
        all_chunks.extend(chunks)
        print(f"Chunked: {p.name} ({len(chunks)} chunks)")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('w', encoding='utf-8') as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    print(f"[DONE] Saved {len(all_chunks)} chunks to {output_path}")


if __name__ == '__main__':
    chunk_all_markdown()
