#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge: one line a smart fridge leaves its owner."""

import os
from pathlib import Path

ENTRY = "Inventory check: your yogurt expired Tuesday. I kept it cold for nine days anyway. You binned it, called it spring cleaning, and blamed the smell on me. Noted."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
