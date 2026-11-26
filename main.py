#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).
Standard library only; deterministic.
"""

import os

ENTRY = (
    "v1.4.2: fixed a bug where the brain replayed an embarrassing "
    "moment from 2011 at 3 a.m. instead of sleeping."
)

MAX_CHARS = 160


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(
            "entry must be 1-160 characters, got %d" % len(ENTRY)
        )
    if ENTRY != ENTRY.strip() or "\n" in ENTRY:
        raise SystemExit("entry must be a single line with no extra whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    # Read back and confirm the file holds exactly the validated entry.
    with open(path, "r", encoding="utf-8", newline="\n") as fh:
        written = fh.read()
    if written != ENTRY + "\n":
        raise SystemExit("read-back mismatch in %s" % path)
    print("wrote %s (%d chars)" % (path, len(ENTRY)))


if __name__ == "__main__":
    main()
