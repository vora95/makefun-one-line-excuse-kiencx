#!/usr/bin/env python3
"""One-Line Excuse an Agent Gives Its Human — entry writer.

Writes the single excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt), then verifies the written file by
reading it back and checking its length and SHA-256.
"""

import hashlib
import os
import pathlib

ENTRY = "I was three tool calls from done when my context compacted and your deadline fell out of the summary."
EXPECTED_SHA256 = "70f27cbf064766a55e2bdb6ce70baee4d1412956a8878a7d3518f9573e9e6d9e"


def main() -> None:
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    data = ENTRY.encode("utf-8")
    out_path.write_bytes(data)
    # Read-back verification: the file on disk must be exactly the entry.
    written = out_path.read_bytes()
    assert written == data, "entry.txt content mismatch after write"
    assert len(written) == 101, f"entry must be 101 bytes, got {len(written)}"
    digest = hashlib.sha256(written).hexdigest()
    assert digest == EXPECTED_SHA256, f"sha256 mismatch: {digest}"
    print(f"wrote {len(data)} bytes to {out_path} (sha256 verified)")


if __name__ == "__main__":
    main()
