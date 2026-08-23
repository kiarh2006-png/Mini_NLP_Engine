from dataclasses import dataclass


@dataclass
class Document:
    metadata: dict
    language: str
    sentences: list[str]
    words: list[str]
    normalized_text: str
    top_words: list[tuple[str, int]]
    statistics: dict[str, int | float]