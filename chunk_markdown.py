# chunk_markdown.py
import os
import re

def chunk_markdown_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    # Split by headings (## or ###)
    chunks = re.split(r'(?:^|\n)(##+ .*)', content)
    result = []
    for i in range(1, len(chunks), 2):
        header = chunks[i].strip()
        text = chunks[i+1].strip()
        result.append({
            "text": text,
            "header": header,
            "source_file": os.path.basename(file_path)
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