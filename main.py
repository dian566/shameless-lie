#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes the most shameless lie — the classic unread-email excuse —
in one to five words to /output/entry.txt, one line, at most 88 characters, no trailing newline.
"""

import os

ENTRY = "I never got your email."


def main():
    line = ENTRY.strip()
    words = line.split()
    if not 1 <= len(words) <= 5:
        raise ValueError(f"entry must be 1-5 words, got {len(words)}")
    if not 1 <= len(line) <= 88:
        raise ValueError(f"entry must be 1-88 characters, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
