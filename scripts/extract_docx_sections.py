#!/usr/bin/env python3
"""Print selected paragraph ranges or headings from the source DOCX.

Examples:
  python extract_docx_sections.py "D:\\...\\Mistery趋势交易论(710页).docx" --range 831:922
  python extract_docx_sections.py "D:\\...\\Mistery趋势交易论(710页).docx" --headings
"""

from __future__ import annotations

import argparse
from pathlib import Path

from docx import Document


def parse_range(value: str) -> tuple[int, int]:
    try:
        start, end = (int(part) for part in value.split(":", 1))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("range must look like START:END") from exc
    if start < 0 or end < start:
        raise argparse.ArgumentTypeError("range must satisfy 0 <= START <= END")
    return start, end


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--range", dest="paragraph_range", type=parse_range)
    parser.add_argument("--headings", action="store_true")
    args = parser.parse_args()

    if not args.docx.is_file():
        parser.error(f"DOCX not found: {args.docx}")
    if not args.paragraph_range and not args.headings:
        parser.error("provide --range START:END or --headings")

    paragraphs = Document(args.docx).paragraphs
    if args.headings:
        for index, paragraph in enumerate(paragraphs):
            if paragraph.text.strip() and paragraph.style.name.startswith("Heading"):
                print(f"{index}: {paragraph.text.strip()}")
    if args.paragraph_range:
        start, end = args.paragraph_range
        for index in range(start, min(end, len(paragraphs))):
            text = paragraphs[index].text.strip()
            if text:
                print(f"{index}: {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


