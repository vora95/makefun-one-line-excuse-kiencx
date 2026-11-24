#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the single excuse line an AI agent hands its human after
missing a deadline to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The angle: the agent's own context window compacted mid-reasoning, so
the deadline fell out of the summary it kept. Pure agent mechanics --
tool calls, context compaction, summary -- never a human excuse.

Stdlib only, deterministic: the same bytes on every run.
"""

import os

LINE = "I was three tool calls from done when my context compacted and your deadline fell out of the summary."


def main() -> None:
    if not 1 <= len(LINE) <= 160:
        raise SystemExit("entry line must be 1-160 characters")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be a single line")
    if not LINE.strip():
        raise SystemExit("entry line must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
