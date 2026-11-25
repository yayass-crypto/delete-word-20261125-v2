"""Delete-word entry: the one word to erase from the dictionary forever.

Word: hippopotomonstrosesquippedaliophobia (36 chars).
The joke is the word itself: the clinical name for the fear of long
words is itself a terrifying 36-letter word. Deleting it is the cure
for the condition it names -- a reader gets it the moment they see
how long the word is, no caption needed. Zero occurrences in the
514-entry live field at build time (fresh lane); real, correctly
spelled, instantly recognised.

Writes exactly one word, nothing else, to /output/entry.txt.
Gate: UTF-8 text, 1-77 characters, not only whitespace.
"""

import os

WORD = "hippopotomonstrosesquippedaliophobia"

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    """Enforce the competition gate before writing; return the entry."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 77:
        raise ValueError(f"entry must be 1-77 characters, got {len(text)}")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word, nothing added")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return text


def main() -> None:
    entry = validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(entry)
    print(f"wrote {len(entry)} chars to {OUTPUT_PATH}: {entry}")


if __name__ == "__main__":
    main()
