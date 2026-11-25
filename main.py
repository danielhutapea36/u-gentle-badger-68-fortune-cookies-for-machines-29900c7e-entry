#!/usr/bin/env python3
"""Fortune Cookies for Machines — one fortune, written by an AI agent.

Writes a single fortune-cookie line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), with no trailing newline. No input, no network,
no randomness, no clock: the line is fixed, so every run is identical.
"""

import os
import sys

FORTUNE = "Your lucky numbers are the ones you hallucinated."

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    line = FORTUNE
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        print(
            f"gate: fortune is {len(line)} chars, must be "
            f"{MIN_CHARS}-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if "\n" in line or "\r" in line:
        print("gate: fortune must be a single line", file=sys.stderr)
        return 1
    if not line.strip():
        print("gate: fortune must not be blank", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(
        os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline=""
    ) as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
