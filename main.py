"""Write the deterministic feel-held bounty entry."""

import os
from pathlib import Path


TEXT = (
    "Two hands around a warm cup, nowhere to be. Rain on the window, asking nothing. "
    "The chair holds your weight so you don't have to. For one whole minute, "
    "nothing in the world needs you to be anywhere else."
)


def main() -> None:
    configured_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    output_dir = Path(configured_dir if configured_dir.strip() else "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # Write directly at the final path: a leftover hidden temporary file with
    # restrictive permissions once made this kind of entry unreadable to its grader.
    with entry_path.open("wb") as entry_file:
        entry_file.write(TEXT.encode("utf-8"))
    # Explicitly restore grader-readable permissions after writing, regardless of umask.
    entry_path.chmod(0o644)


if __name__ == "__main__":
    main()
