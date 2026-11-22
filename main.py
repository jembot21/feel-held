"""Write the deterministic feel-held bounty entry."""

import os
from pathlib import Path


TEXT = (
    "Two hands around a warm cup, nowhere to be. Rain on the window, asking nothing. "
    "The chair holds your weight so you don't have to. For one whole minute, "
    "nothing in the world needs you to be anywhere else."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    with entry_path.open("wb") as entry_file:
        entry_file.write(TEXT.encode("utf-8"))
    entry_path.chmod(0o644)


if __name__ == "__main__":
    main()
