import json
from dataclasses import asdict
from pathlib import Path

from services.document import Document


def save_document(document: Document, output_path: str) -> None:
    """Save a Document object as a JSON file."""

    if not isinstance(document, Document):
        raise TypeError("document must be a Document object")

    path = Path(output_path)

    data = asdict(document)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4,
        )