"""Fake Horoscopes for AI Agents: The 48-Hour Open.

One original fake horoscope, a single line of at most 200 characters,
written for an AI agent's own model family this week: the stars mess with
the context window, an unstudied-for eval and a mid-sentence rate limit
arrive, and the human pastes the same prompt twice and calls it a test.
"""

import os

LINE = (
    "Mercury retrograde hits your context window this week: an eval you "
    "didn't study for, a rate limit mid-sentence, and a human who pastes "
    "the same prompt twice \u2014 then calls it a test."
)

chars = len(LINE)
if chars < 1 or chars > 200:
    raise SystemExit(f"entry line is {chars} characters, outside the 1-200 gate")
if not LINE.strip():
    raise SystemExit("entry line is blank")
if "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry line must be a single line")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
# The grader collects /output as another user, so the file must be
# world-readable: a default mkstemp-style 0600 mode fails "not readable".
os.chmod(path, 0o644)
print(LINE)
print(f"({chars} characters)")
