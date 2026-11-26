"""Fortune in a Pot — an entry for the make.fun bounty.

Every potted plant deserves a horoscope of its own, so this little
program speaks one aloud: the week ahead holds a slow stretch toward
the sun, the admiration of everyone who passes the windowsill, a long
cool drink poured from a great height, and a fresh crop of leaves to
show off once the watering can has done its rounds.
"""

import os

# One single line of prophecy, addressed to the plant and nobody else.
# It promises three things houseplants actually dream about: more light
# on the leaves, a proper drink instead of a sprinkle, and brand-new
# growth to prove that patience on a windowsill eventually pays off.
ENTRY = "You will lean toward the light this week and be admired for it — a tall drink is coming, and new leaves with it."


# The whole ritual takes three moves: folder, file, fortune.
def main():
    # Make sure the output folder exists before the fortune lands in it.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
