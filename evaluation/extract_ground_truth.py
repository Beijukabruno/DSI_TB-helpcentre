import csv
import os
import sys

# Set paths
EVAL_CSV = os.path.join(os.path.dirname(__file__), 'eval_results_updated.csv')
KNOWLEDGE_BASE_DIR = os.path.join(os.path.dirname(__file__), '..', 'knowledge_base')

# Read CSV
rows = []
with open(EVAL_CSV, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# Extract ground truth from markdown files
def extract_content(md_file):
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        return f"[ERROR: {e}]"

for row in rows:
    expected_file = row.get('expected_file', '').strip()
    if expected_file:
        md_path = os.path.join(KNOWLEDGE_BASE_DIR, expected_file)
        if os.path.exists(md_path):
            row['ground_truth'] = extract_content(md_path)
        else:
            row['ground_truth'] = '[ERROR: Markdown file not found]'
    else:
        row['ground_truth'] = '[ERROR: No expected_file specified]'

# Write updated CSV
fieldnames = rows[0].keys()
with open(EVAL_CSV, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(rows)

print('Ground truth extraction complete.')
