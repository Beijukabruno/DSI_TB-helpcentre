import pandas as pd
import json
import os
import shutil

# Paths
EVAL_CSV = 'evaluation/eval_results_updated.csv'
EVAL_CSV_CHUNKS = 'evaluation/eval_results_chunks.csv'
CHUNKS_JSON = 'chunks.json'

# Duplicate the CSV
shutil.copy(EVAL_CSV, EVAL_CSV_CHUNKS)

# Load data
chunks = []
with open(CHUNKS_JSON, 'r', encoding='utf-8') as f:
    chunks = json.load(f)

df = pd.read_csv(EVAL_CSV_CHUNKS)

def find_chunk(expected_file, query):
    # Match by source_file field
    file_matches = [c for c in chunks if c.get('source_file', '').strip() == expected_file]
    if not file_matches:
        return '[NO CHUNK FOUND]'
    # Simple heuristic: return the first chunk (can be improved with better matching)
    return file_matches[0].get('text', '[NO TEXT FOUND]')

# Update ground_truth with chunk text
for idx, row in df.iterrows():
    expected_file = str(row.get('expected_file', '')).strip()
    query = str(row.get('query', '')).strip()
    chunk_text = find_chunk(expected_file, query)
    df.at[idx, 'ground_truth'] = chunk_text

# Save the updated CSV
# Use quoting for safety
import csv
df.to_csv(EVAL_CSV_CHUNKS, index=False, quoting=csv.QUOTE_ALL)
print('Created evaluation/eval_results_chunks.csv with chunk-level ground truth.')
