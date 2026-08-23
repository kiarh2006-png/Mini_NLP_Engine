import re
from collections import Counter

import numpy as np
import pandas as pd


PERSIAN_PUNCTUATION = "،؛؟«»٪×÷ـ"


def normalize_text(text: str) -> str:
    """Normalize punctuation, newlines, case, and whitespace."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # یکدست کردن newlineها
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # حذف punctuation انگلیسی و فارسی
    punctuation = (
        r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        + PERSIAN_PUNCTUATION
    )

    translation_table = str.maketrans(
        "",
        "",
        punctuation,
    )

    text = text.translate(translation_table)

    # تبدیل حروف انگلیسی به lowercase
    text = text.lower()

    # یکدست کردن فاصله‌ها
    return " ".join(text.split())


def split_sentences(text: str) -> list[str]:
    """Split text into sentences while preserving original case."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text.strip():
        return []

    # یکدست کردن newlineها
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # جدا کردن جمله‌ها بر اساس ! ? ؟
    sentences = re.split(
        r"(?<=[.!?؟])\s+",
        text.strip(),
    )

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]


def tokenize_words(text: str) -> list[str]:
    """Convert text into normalized word tokens."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    normalized_text = normalize_text(text)

    if not normalized_text:
        return []

    return normalized_text.split()


def count_words(text: str) -> int:
    """Return the number of words in the text."""

    return len(tokenize_words(text))


def count_paragraphs(text: str) -> int:
    """Return the number of non-empty paragraphs."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace("\r\n", "\n").replace("\r", "\n")

    paragraphs = [
        paragraph.strip()
        for paragraph in text.split("\n\n")
        if paragraph.strip()
    ]

    return len(paragraphs)


def top_words(
    text: str,
    limit: int = 10,
) -> list[tuple[str, int]]:
    """Return the most common words."""

    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")

    if limit <= 0:
        raise ValueError("limit must be greater than zero")

    words = tokenize_words(text)

    if not words:
        return []

    return Counter(words).most_common(limit)


def get_statistics(text: str) -> dict[str, int | float]:
    """Return statistical information about the text."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = tokenize_words(text)
    sentences = split_sentences(text)

    character_count = len(text)
    word_count = len(words)
    sentence_count = len(sentences)
    unique_word_count = len(set(words))

    if words:
        word_lengths = np.array(
            [len(word) for word in words],
            dtype=np.float64,
        )

        average_word_length = float(
            np.mean(word_lengths)
        )
    else:
        average_word_length = 0.0

    return {
        "character_count": character_count,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "unique_word_count": unique_word_count,
        "average_word_length": average_word_length,
    }


def word_frequency_dataframe(text: str) -> pd.DataFrame:
    """Return word frequencies as a Pandas DataFrame."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = tokenize_words(text)

    if not words:
        return pd.DataFrame(
            columns=["word", "count"]
        )

    word_counts = Counter(words)

    dataframe = pd.DataFrame(
        word_counts.items(),
        columns=["word", "count"],
    )

    dataframe = dataframe.sort_values(
        by="count",
        ascending=False,
        ignore_index=True,
    )

    return dataframe