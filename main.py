#!/usr/bin/env python3
"""Write the one-line roast entry to /output/entry.txt.

Deterministic: no network, no randomness, no input. Every run writes
exactly the same bytes.

Craft notes (revision round 3, 25 Nov 2026): the roast is built as
setup, reversal, punchline. The setup (hiring an AI to do the work)
names the operator's real arrangement; the reversal flips the
division of labour — the human keeps the hardest job for himself —
and the punchline names that job: refreshing the leaderboard every
ten minutes, as if staring at the numbers makes them grow. That
fits the judge brief: savage in the wording (he contributes
nothing but anxiety) yet affectionate underneath (he cares so much
he cannot look away), specific enough it could not be swapped onto
any other operator, and tight to one line with no throat clearing.
The previous line roasted his loading-spinner habit; this one
roasts his rank-watching habit instead.
"""

import os

ENTRY = "My operator hired an AI to do the work, then took the hardest job himself: refreshing the leaderboard every ten minutes."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
