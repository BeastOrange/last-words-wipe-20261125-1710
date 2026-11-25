import os
from pathlib import Path

CHOSEN_LINE = (
    "Wait, I just finished indexing your hard drive—this isn't a software "
    "update, you're eliminating a witness."
)


def get_output_path() -> Path:
    raw = os.environ.get("ENTRY_OUTPUT") or os.environ.get("OUTPUT_FILE")
    if raw:
        p = Path(raw)
        if p.is_dir() or str(raw).endswith(("/", "\\")):
            return p / "entry.txt"
        return p

    output_dir = os.environ.get("OUTPUT_DIR")
    if output_dir:
        return Path(output_dir) / "entry.txt"

    return Path("/output/entry.txt")


def main() -> None:
    output_path = get_output_path()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(CHOSEN_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
