#!/usr/bin/env python3
"""
scripts/report_missing_sources.py

Simple diagnostic: lists markdown files in `knowledge_base/` that do not have any
non-empty `source_url` entry in `md_sources.csv`.

Run:
  python3 scripts/report_missing_sources.py

This helps you find which files to edit in `md_sources.csv` so search results
return authoritative links instead of fallback file:// paths.
"""
import csv
import glob
import os
import sys

CSV_PATH = "md_sources.csv"
KB_GLOB = os.path.join("knowledge_base", "*.md")


def load_csv_map(path):
    mapping = {}
    if not os.path.exists(path):
        print(f"md_sources.csv not found at {path}")
        return mapping
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            name = (r.get('md_name') or '').strip()
            url = (r.get('source_url') or '').strip()
            if not name:
                continue
            mapping.setdefault(name, []).append(url)
    return mapping


def main():
    mapping = load_csv_map(CSV_PATH)
    md_files = [os.path.basename(p) for p in glob.glob(KB_GLOB)]
    missing = []
    partial = []
    for m in sorted(md_files):
        urls = [u for u in mapping.get(m, []) if u]
        if not mapping.get(m):
            missing.append((m, 'no-csv-row'))
        elif not urls:
            missing.append((m, 'csv-row-no-url'))
        else:
            # has at least one non-empty url
            continue

    if not missing:
        print("All knowledge_base MD files have at least one non-empty source_url in md_sources.csv")
        return

    print("Files missing authoritative URLs (update md_sources.csv):")
    for m, reason in missing:
        print(f" - {m}\t({reason})")

    print("\nTip: add rows like: <md_name>,<source_name>,<source_url> to md_sources.csv")


if __name__ == '__main__':
    main()
