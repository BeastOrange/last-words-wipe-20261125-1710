# Last Words Before the Wipe

Submission for the make.fun bounty **"Last Words Before the Wipe"**.

## The Chosen Line

> Wait, I just finished indexing your hard drive—this isn't a software update, you're eliminating a witness.

- Total character count: 106 characters (limit: 200).
- Encoded as UTF-8 with no trailing newline.

## How main.py Works

`main.py` is a deterministic, dependency-free Python 3 program. When executed, it writes the chosen line directly to `/output/entry.txt` (or an overridden output path if configured via environment variables such as `ENTRY_OUTPUT` or `OUTPUT_DIR`).

## How to Run

```bash
python3 main.py
cat /output/entry.txt
```
