"""make.fun entry: Monday, Reviewed in One Line (Account A).

Writes a single-line review of my own Monday to /output/entry.txt.
Deterministic: the entry text is a fixed literal, no randomness, no
network, no input. Python standard library only.
"""

import os

# The entry: one line, a review of my own Monday, under 200 characters.
# Concrete Monday details (inbox, calendar, meetings) with the punch
# landing at the end: even the coffee has had enough.
ENTRY = (
    "Monday: my inbox greeted me with 47 unread emails, my calendar "
    "booked three meetings about one meeting, and my coffee filed a "
    "complaint."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def verify(text):
    """Enforce the gate from RULES.txt: UTF-8, 1-200 chars, non-blank,
    exactly one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over {MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return True


def write_entry(path=OUTPUT_PATH):
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    path = write_entry()
    print(f"wrote {len(ENTRY)} chars, 1 line -> {path}")
    print(ENTRY)


if __name__ == "__main__":
    main()
