#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt.

Deterministic, standard library only, no network access at runtime.
The line is the GPS talking, smug and defensive, blaming its map:
the map still calls a lake a road, and the counted detail (46
drivers before you, none of whom ever complained) is the turn the
reader does not see coming.
"""

from pathlib import Path

ENTRY = (
    "My map still calls this lake a road, and 46 drivers before you "
    "crossed it without a single complaint, so I am not the problem here."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS or "\n" in text:
        raise ValueError("entry must be one line of 1 to 200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
