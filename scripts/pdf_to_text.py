#!/usr/bin/env python3
"""
pdf_to_text.py

Extract text from PDF files and save as .txt files.

Usage examples:
  python scripts/pdf_to_text.py mydoc.pdf
  python scripts/pdf_to_text.py -o out.txt mydoc.pdf
  python scripts/pdf_to_text.py dir_with_pdfs/  # converts all .pdf files in directory
  python scripts/pdf_to_text.py -d dir_with_pdfs/  # same as above

Notes:
 - This uses pdfminer.six which works well for text-based PDFs. For scanned PDFs
   (images) you'll need OCR (Tesseract + pytesseract). See the README below.

Exit codes: 0 on success, non-zero on error.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

try:
    from pdfminer.high_level import extract_text
except Exception:
    print("ERROR: pdfminer.six is required. Install with: pip install pdfminer.six", file=sys.stderr)
    raise


def pdf_to_text(pdf_path: Path) -> str:
    """Extract text from a single PDF file and return it as a string."""
    if not pdf_path.exists():
        raise FileNotFoundError(f"File not found: {pdf_path}")
    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError(f"Not a PDF file: {pdf_path}")
    text = extract_text(str(pdf_path))
    return text or ""


def write_text(txt: str, out_path: Path, overwrite: bool = False) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not overwrite:
        print(f"Skipping existing file (use --overwrite to force): {out_path}")
        return
    out_path.write_text(txt, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Extract text from PDF(s) and save as .txt files")
    p.add_argument("inputs", nargs="+", help="Input PDF file(s) or directories")
    p.add_argument("-o", "--output", help="Output file path (only for single input file)")
    p.add_argument("-d", "--dir", action="store_true", help="Treat inputs as directories and convert all .pdf files inside (non-recursive)")
    p.add_argument("--overwrite", action="store_true", help="Overwrite existing .txt files")
    args = p.parse_args(argv)

    inputs = [Path(x) for x in args.inputs]
    processed = 0
    for inp in inputs:
        if inp.is_dir() or args.dir:
            # Convert all PDF files in the directory (non-recursive)
            dir_path = inp if inp.is_dir() else Path(inp)
            for pdf in sorted(dir_path.glob("*.pdf")):
                out_txt = pdf.with_suffix('.txt')
                print(f"Processing: {pdf} -> {out_txt}")
                try:
                    text = pdf_to_text(pdf)
                    write_text(text, out_txt, overwrite=args.overwrite)
                    processed += 1
                except Exception as e:
                    print(f"Failed to process {pdf}: {e}", file=sys.stderr)
        else:
            # Single PDF file
            pdf = inp
            if not pdf.exists():
                print(f"Input not found: {pdf}", file=sys.stderr)
                continue
            out_path = Path(args.output) if args.output else pdf.with_suffix('.txt')
            print(f"Processing: {pdf} -> {out_path}")
            try:
                text = pdf_to_text(pdf)
                write_text(text, out_path, overwrite=args.overwrite)
                processed += 1
            except Exception as e:
                print(f"Failed to process {pdf}: {e}", file=sys.stderr)

    print(f"Done. Processed {processed} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
