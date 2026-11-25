"""Fortune in a Pot — a make.fun bounty entry.

The fortune, told to a houseplant: repotting day is coming. Someone who
loves the plant — and honestly talks to it more than to their coworkers —
will soon move it to a bigger pot. It is the best news a windowsill plant
can get: more room, fresh soil, and proof it was never just decoration.
"""

import os

ENTRY = "You will soon be moved to a bigger pot by someone who loves you and talks to you more than to their coworkers."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
