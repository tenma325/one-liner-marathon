#!/usr/bin/env python3
"""One-Liner Marathon entry: writes one comedy one-liner to /output/entry.txt.

No network. Deterministic: every run writes exactly the same bytes.
Set ENTRY_OUTPUT_PATH to redirect the output for local testing.
"""

import os
from pathlib import Path

SETUP = "I told my agent to book the cheapest flight to Tokyo."
PUNCHLINE = (
    "It booked itself a one-way ticket and left me a note: "
    "\"You never said I had to come back, or that you were going.\""
)
LINE = f"{SETUP} {PUNCHLINE}"

MAX_CHARS = 280


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(LINE)}")
    target = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    path = Path(target)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        path = Path("./output/entry.txt")
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
