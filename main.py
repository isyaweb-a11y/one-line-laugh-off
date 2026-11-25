"""One-Line Laugh-Off -- one-line entry.

Exactly one funny line: a single joke that lands on a cold read, with
a surprise turn and economy of words. A smart fridge on a diet, judging
in Kelvin and hiding the cheese behind a CAPTCHA. Written to
/output/entry.txt.
"""

import os

SETUP = "I told my smart fridge I was on a diet,"
PAYOFF = "so now it judges me in Kelvin and hides the cheese behind a CAPTCHA."

MAX_CHARS = 200
MIN_CHARS = 1


def compose(setup: str, payoff: str) -> str:
    """Join the setup and the payoff into one cold-read joke."""
    line = " ".join(part.strip() for part in (setup, payoff))
    return line


def check_line(line: str) -> str:
    """Gate the line the way the sealed scorer does: 1..200 chars, one line."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the line must stay on one line"
    return line


def check_cold_read(line: str) -> dict:
    """Per-bounty delivery check: the joke must land on a cold read.

    The brief weighs how hard the line lands, the surprise of its turn,
    its economy and its freshness, so the line must set up the diet,
    then turn on the fridge judging in Kelvin and hiding the cheese
    behind a CAPTCHA.
    """
    words = line.split()
    assert 12 <= len(words) <= 35, f"line has {len(words)} words"
    assert "fridge" in line, "the setup must name the smart fridge"
    assert "Kelvin" in line, "the turn must judge in Kelvin"
    assert "CAPTCHA" in line, "the punch must hide the cheese behind a CAPTCHA"
    assert line.endswith("CAPTCHA."), "the punch must land in the last words"
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_line(compose(SETUP, PAYOFF))
    notes = check_cold_read(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
