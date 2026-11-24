"""One-Liner Laugh Lab entry runner.

Loads the single funny line from entry.txt and prints it to stdout.
"""

from pathlib import Path


def load_line() -> str:
    here = Path(__file__).resolve().parent
    return (here / "entry.txt").read_text(encoding="utf-8").strip()


def main() -> None:
    line = load_line()
    print(line)
    out_dir = Path("/output")
    if out_dir.is_dir():
        (out_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
