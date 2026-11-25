#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Writes a single line (at most 200 characters) to /output/entry.txt:
the funniest honest error message an appliance could show.
Deterministic: no randomness, no time, no environment dependence
beyond the MAKEFUN_OUTPUT override.
"""

import os

ENTRY = (
    "ERROR UE: Unbalanced load. One trainer is not a load. "
    "I have been shaking for nine minutes and I am not the one who put it in here."
)


def main() -> None:
    output = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
    with open(output, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
