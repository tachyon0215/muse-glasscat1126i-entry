#!/usr/bin/env python3
"""Write the cat's excuse for the glass to entry.txt.

Competition: Five Seconds to Explain the Glass (one sentence,
1-200 chars, the cat's own voice; no apology, no confession;
the judge weighs a convincing cat reason first, then true cat
logic with no remorse, then a fresh comic idea, avoiding the
obvious gravity / slippery-edge / already-falling lines).
Candidates:
A) "I was checking whether it was empty - you keep drinking
   from it without ever offering me any, so I tested it the
   only fair way." (grievance, but the test framing is human)
B) "That glass was blocking my view of the table edge, and a
   cat cannot patrol a border she cannot see, so I cleared it
   for both our safety." (patrol logic, but admits clearing it)
C) "You put a breakable thing in my stretching zone, in my
   house, at my height - I simply enforced the house rules you
   agreed to when you adopted me." (legalistic and funny, but
   'I enforced' confesses the act)
Selected D (161 chars): a real cat motive - a full glass of
water nobody was drinking while her own bowl sat empty - so
the crash is reframed, without apology or confession, as her
first formal complaint, filed at table height.
Deterministic: a fixed text, no network, no randomness.
"""
import os
from pathlib import Path

LINE = "That glass was full of water nobody was drinking while my bowl sat empty in the next room — consider that sound my first formal complaint, filed at table height."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be one sentence on one line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write bytes directly so the entry is identical on every run.
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
