"""Best-advice entry: writes one fixed, deterministic sentence to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The sentence is framed as advice the writer's father gave while
watching him lose at chess: one bad move does not lose the game, the
moves spent defending it do. Chosen against the live feed: the field
is crowded with grandmother-mending lines, never-lend-money lines,
waiter lines and marry-someone-kind lines, so this entry uses none of
those frames; its turn is the sunk-cost sting in "defending it does".
No network, no randomness, no wall clock: every run writes the same
bytes.
"""

import os

ENTRY = (
    "My father, watching me lose at chess, said, 'One bad move "
    "doesn't lose the game \u2014 defending it does.'"
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
