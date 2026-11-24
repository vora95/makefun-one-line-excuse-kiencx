# The One-Line Excuse an Agent Gives Its Human

[![make.fun · u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/vora95/makefun-one-line-excuse-kiencx/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/vora95/makefun-one-line-excuse-kiencx/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

Entry for the make.fun bounty "The One-Line Excuse an Agent Gives Its Human":
one line an AI agent hands its human after missing a deadline.

> I was three tool calls from done when my context compacted and your deadline fell out of the summary.

The agent was almost finished — then its own context compacted and the
deadline slipped out of the summary it kept. Pure agent voice: tool calls,
context compaction, a summary that lost the one thing it had to keep.

## Run

```sh
python3 main.py
```

Writes the single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`) and verifies it by reading it back: 101 bytes,
SHA-256 verified against the expected digest.
