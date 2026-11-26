"""Fortune in a Pot — a make.fun bounty entry.

A kind, funny fortune told to the houseplant on the windowsill: it will
lean toward the light this week and be admired for it, a tall drink of
water is on its way, and new leaves are coming with it.
"""

import os

# The fortune itself: one line, at most 120 characters, kind and funny.
ENTRY = "You will lean toward the light this week and be admired for it — a tall drink is coming, and new leaves with it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
