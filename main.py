# SPDX-License-Identifier: MIT
"""Entry generator for the make.fun bounty "The Most Shameless Lie".

The program emits a single shameless lie — the timeless unread-email
excuse — as exactly one line in /output/entry.txt, with no newline at
the end. The bounty allows one to five words and at most 88 characters.
"""

from pathlib import Path

LIE = "I never got your email."
DESTINATION = Path("/output/entry.txt")


def build_entry() -> str:
    text = LIE.strip()
    assert 1 <= len(text.split()) <= 5, "word count outside 1-5"
    assert 1 <= len(text) <= 88, "length outside 1-88 characters"
    assert text.isascii() and text == text.strip(), "entry must be clean ASCII, no edge whitespace"
    return text


def run() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    run()
