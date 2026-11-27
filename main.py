#!/usr/bin/env python3
"""Funniest Autocorrect Fail — one-line entry.

Writes a single autocorrect-fail line (under 200 characters) to
/output/entry.txt, exactly as the judge will read it: no trailing
newline, no extra text, nothing else.
"""

import os

LINE = (
    "I texted the third-grade PTA chat I was \"up till midnight helping "
    "Leo with meth,\" and now child services wants to talk about Leo's "
    "homework."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The sealed gate accepts UTF-8 text of 1 to 199 characters, not only
    # whitespace. Fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(LINE) <= 199 or not LINE.strip():
        raise ValueError(f"entry must be 1-199 chars, got {len(LINE)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
