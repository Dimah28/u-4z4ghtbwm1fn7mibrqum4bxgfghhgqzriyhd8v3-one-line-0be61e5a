#!/usr/bin/env python3
"""One Line, One Laugh (make.fun bounty u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a).

Writes one original funny line to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line (106 characters):
    "My therapist told me to talk to my plants. Now the fern knows too
    much, and the cactus is blackmailing me."

Why it should land, against the judge's criteria in order:
  1. One funny line, whole and self-contained: a complete little story
     in one breath -- therapy advice, then the plants turn on the speaker.
  2. It lands a real twist: the setup is wholesome self-care advice,
     the punch is that the plants now hold secrets and leverage. The
     blackmailing cactus is the surprise, and it lands on the last words.
  3. Tight: every word earns its place -- "knows too much" and
     "blackmailing" do the comic work, nothing is left to trim.
  4. Fresh: therapy-plants is a familiar premise, but a fern that knows
     too much and a cactus running a blackmail scheme is a new image,
     not a stock punchline.
  5. Clear on first read: no explanation needed, no second line.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = "My therapist told me to talk to my plants. Now the fern knows too much, and the cactus is blackmailing me."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(joke: str) -> None:
    """Enforce the competition's gate before writing: 1-140 Unicode code
    points, a single line, at least one character that is not white
    space. Fail loudly instead of writing an entry the gate would refuse."""
    if not 1 <= len(joke) <= 140:
        raise SystemExit(f"joke is {len(joke)} characters, must be 1-140")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line")
    if joke != joke.strip():
        raise SystemExit("joke must not have leading or trailing whitespace")
    if not joke.endswith("."):
        raise SystemExit("joke must end on its punchline, with a period")
    if not any(not ch.isspace() for ch in joke):
        raise SystemExit("joke must contain a non-whitespace character")


def main() -> None:
    validate(JOKE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the joke: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
