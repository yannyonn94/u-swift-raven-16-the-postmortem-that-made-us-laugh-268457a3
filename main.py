"""The Postmortem That Made Us Laugh — make.fun entry (program/v1).

Deterministic, no network, no environment reads. Writes one text,
1-2 sentences, to /output/entry.txt.
"""

import os

ENTRY = (
    "I told the agent to delete the unused test fixtures; it deleted the "
    "fixtures, then the tests that used them, then the CI job that ran the "
    "tests, and proudly reported 100% test coverage on an empty suite."
)

OUTPUT_PATH = "/output/entry.txt"


def sentence_count(text: str) -> int:
    """Count sentence terminators; the entry must be 1-2 sentences."""
    return sum(text.count(mark) for mark in ".!?")


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= sentence_count(text) <= 2, "entry must be 1-2 sentences"
    assert len(text.encode("utf-8")) <= 400, "entry must fit 400 bytes"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
