#!/usr/bin/env python3
"""One-Liner Laughs — a single funny line, written to /output/entry.txt.

The joke: a 404 gag. Setup — I posted my best joke online.
Payoff — it came back 404, and even the punchline ghosted me.
One clear twist, no explanation needed, tight wording.
"""

import os

JOKE = "I posted my best joke online and it came back 404 \u2014 even the punchline ghosted me."


def validate(text: str) -> None:
    """Gate: UTF-8 text, 1-200 chars, a single line, not only whitespace."""
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or text != text.strip():
        raise SystemExit("entry must be a single line with no surrounding whitespace")


def main() -> None:
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
