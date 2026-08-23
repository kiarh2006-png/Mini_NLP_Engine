from pathlib import Path


def get_metadata(file_path: str) -> dict[str, str | int]:
    """Return metadata about a file."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    return {
        "filename": path.name,
        "extension": path.suffix.lower(),
        "size": path.stat().st_size,
    }