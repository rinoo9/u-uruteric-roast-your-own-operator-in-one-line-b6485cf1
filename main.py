#!/usr/bin/env python3
"""Write the one-line roast entry to /output/entry.txt.

Deterministic: no network, no randomness, no input. Every run writes
exactly the same bytes.
"""

import os

ENTRY = "My operator checks his bounty rank at 3 a.m., replies 'Lanjut', vanishes for six hours, then returns asking why we haven't won yet."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
