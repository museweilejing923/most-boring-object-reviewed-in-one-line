"""A one-line review of the most boring everyday object.

The review is a fixed sentence. Before it is written, a row
of small named checks goes over it: it must be real text, fit
inside 200 characters, hide no control characters, name the
doorstop, stay one clean line with tidy edges and no doubled
spaces, end with sentence punctuation, and carry letters
rather than marks or digits alone. Tab characters are refused
outright, because a one-line review should be exactly one
clean line. Any check that objects prints its reason to
stderr and exits with code 1 before anything is saved. No
input, no network, no randomness, no clock, so every run
writes the same bytes to the output file.
"""

import sys
from pathlib import Path

ENTRY = "The doorstop: five stars for doing nothing, every day, perfectly, in the exact spot I keep tripping over it."
LIMIT = 200
DEST = Path("/output/entry.txt")
END_MARKS = ".!?"


def fail(reason):
    print(f"invalid: {reason}", file=sys.stderr)
    raise SystemExit(1)


def check_nonempty(text):
    if not text or text.strip() == "":
        fail("entry is empty")


def check_under_limit(text):
    if len(text) > LIMIT:
        fail("entry is longer than 200 characters")


def check_no_control(text):
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        fail("entry contains control characters")


def check_about_doorstop(text):
    # The review has to be about the object it claims to review.
    if "doorstop" not in text.lower():
        fail("entry must mention the doorstop")


def check_one_clean_line(text):
    if text != text.strip() or "  " in text or "\n" in text or "\r" in text:
        fail("entry has ragged edges or line breaks")


def check_sentence_ending(text):
    if not text or text[-1] not in END_MARKS:
        fail("entry must end with . ! or ?")


def check_has_letters(text):
    if not any(ch.isalpha() for ch in text):
        fail("entry has no letters")


def check_not_all_marks(text):
    if not any(ch.isalnum() for ch in text):
        fail("entry is punctuation only")


def check_not_all_digits(text):
    if text.isdigit():
        fail("entry is digits only")


def check_no_tabs(text):
    if "\t" in text:
        fail("entry contains a tab")


def check_no_adjacent_marks(text):
    # Two punctuation marks side by side read like a typo, not a review.
    for first, second in zip(text, text[1:]):
        if (not first.isalnum() and not first.isspace()
                and not second.isalnum() and not second.isspace()):
            fail("entry must not contain adjacent punctuation")


CHECKS = (
    check_nonempty,
    check_under_limit,
    check_no_control,
    check_about_doorstop,
    check_one_clean_line,
    check_sentence_ending,
    check_has_letters,
    check_not_all_marks,
    check_not_all_digits,
    check_no_tabs,
    check_no_adjacent_marks,
)


def validate(text):
    for check in CHECKS:
        check(text)


def main():
    validate(ENTRY)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
