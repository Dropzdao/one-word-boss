"""One Word for the Boss — make.fun entry.

Writes exactly one word describing the boss to /output/entry.txt.

The word: "Unreachable" — the boss whose status dot is always green
but who never replies, always "in a meeting", always one call away.
It lands on its own, rings true in any workplace, and is not the
first word anyone reaches for.
"""

import os

ENTRY = "Unreachable"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
