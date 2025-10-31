# chunk_markdown.py
import os
import re
import csv


def load_md_sources(csv_path="md_sources.csv"):
    """Return a mapping md_name -> first non-empty source_url from the CSV."""
    mapping = {}
    if not os.path.exists(csv_path):
        return mapping
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            md = row.get('md_name', '').strip()
            url = (row.get('source_url') or '').strip()
            if not md:
                continue
            if md not in mapping and url:
                mapping[md] = url
    return mapping

def chunk_markdown_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    # Load mapping of md -> source URL (if present)
    md_sources = load_md_sources()

    # Split by headings (## or ###)
    chunks = re.split(r'(?:^|\n)(##+ .*)', content)
    result = []
    for i in range(1, len(chunks), 2):
        header = chunks[i].strip()
        text = chunks[i+1].strip()
        result.append({
            "text": text,
            "header": header,
            "source_file": os.path.basename(file_path),
            # include the first known source URL for this markdown file, if any
            "source_url": md_sources.get(os.path.basename(file_path), "")
        })
    return result

# Example usage
if __name__ == "__main__":
    folder = "knowledge_base"
    all_chunks = []
    for fname in os.listdir(folder):
        if fname.endswith(".md"):
            chunks = chunk_markdown_file(os.path.join(folder, fname))
            all_chunks.extend(chunks)
    # Save chunks for next stage
    import json
    with open("chunks.json", "w") as f:
        json.dump(all_chunks, f, indent=2)