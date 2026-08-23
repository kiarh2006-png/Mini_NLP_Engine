import pytest
from services.text_processor import (
    count_paragraphs,
    count_words,
    get_statistics,
    normalize_text,
    split_sentences,
    tokenize_words,
    top_words,
    word_frequency_dataframe,
)


def test_normalize_text():
    text = "  Hello   WORLD  "
    assert normalize_text(text) == "hello WORLD".lower()


def test_normalize_newlines():
    text = "Hello\r\nWorld\rTest"
    assert normalize_text(text) == "hello world test"


def test_normalize_persian():
    text = "سلام، دنیا!"
    assert normalize_text(text) == "سلام دنیا"


def test_normalize_empty():
    assert normalize_text("") == ""


def test_normalize_whitespace():
    text = "   hello     world   "
    assert normalize_text(text) == "hello world"


def test_normalize_invalid_type():
    with pytest.raises(TypeError):
        normalize_text(123)


def test_split_sentences():
    text = "Hello world. How are you? I am fine!"

    result = split_sentences(text)

    assert result == [
        "Hello world.",
        "How are you?",
        "I am fine!",
    ]


def test_split_sentences_persian():
    text = "سلام دنیا. حالت چطوره؟ من خوبم!"

    result = split_sentences(text)

    assert result == [
        "سلام دنیا.",
        "حالت چطوره؟",
        "من خوبم!",
    ]


def test_split_sentences_empty():
    assert split_sentences("") == []


def test_split_sentences_preserves_case():
    result = split_sentences("Hello World. Python Is Great!")

    assert result == [
        "Hello World.",
        "Python Is Great!",
    ]


def test_split_sentences_invalid_type():
    with pytest.raises(TypeError):
        split_sentences(123)


def test_tokenize_words():
    text = "Hello world. Hello Python."

    result = tokenize_words(text)

    assert result == [
        "hello",
        "world",
        "hello",
        "python",
    ]


def test_tokenize_words_persian():
    text = "سلام دنیا. من پایتون را دوست دارم."

    result = tokenize_words(text)

    assert result == [
        "سلام",
        "دنیا",
        "من",
        "پایتون",
        "را",
        "دوست",
        "دارم",
    ]


def test_tokenize_words_empty():
    assert tokenize_words("") == []


def test_tokenize_words_invalid_type():
    with pytest.raises(TypeError):
        tokenize_words(123)


def test_count_words():
    text = "Python is easy. Python is powerful."

    assert count_words(text) == 6


def test_count_words_empty():
    assert count_words("") == 0


def test_count_words_invalid_type():
    with pytest.raises(TypeError):
        count_words(123)


def test_count_paragraphs():
    text = "First paragraph.\n\nSecond paragraph."

    assert count_paragraphs(text) == 2


def test_count_paragraphs_ignores_empty():
    text = "\n\nFirst paragraph.\n\n\n\nSecond paragraph.\n\n"

    assert count_paragraphs(text) == 2


def test_count_paragraphs_empty():
    assert count_paragraphs("") == 0


def test_count_paragraphs_invalid_type():
    with pytest.raises(TypeError):
        count_paragraphs(123)


def test_top_words():
    text = "python python java java java"

    result = top_words(text, 2)

    assert result == [
        ("java", 3),
        ("python", 2),
    ]


def test_top_words_limit():
    text = "python java c++ javascript"

    result = top_words(text, 2)

    assert len(result) == 2


def test_top_words_empty():
    assert top_words("") == []


def test_top_words_invalid_limit():
    with pytest.raises(ValueError):
        top_words("hello world", 0)


def test_top_words_invalid_type():
    with pytest.raises(TypeError):
        top_words("hello world", "10")


def test_get_statistics():
    text = "Python is easy. Python is powerful."

    result = get_statistics(text)

    assert result["word_count"] == 6
    assert result["sentence_count"] == 2
    assert result["unique_word_count"] == 4


def test_get_statistics_empty():
    result = get_statistics("")

    assert result["character_count"] == 0
    assert result["word_count"] == 0
    assert result["sentence_count"] == 0
    assert result["unique_word_count"] == 0
    assert result["average_word_length"] == 0.0


def test_get_statistics_invalid_type():
    with pytest.raises(TypeError):
        get_statistics(123)


def test_word_frequency_dataframe():
    text = "python python java"

    result = word_frequency_dataframe(text)

    assert list(result.columns) == [
        "word",
        "count",
    ]

    assert result.iloc[0]["word"] == "python"
    assert result.iloc[0]["count"] == 2


def test_word_frequency_dataframe_empty():
    result = word_frequency_dataframe("")

    assert list(result.columns) == [
        "word",
        "count",
    ]

    assert result.empty


def test_word_frequency_dataframe_invalid_type():
    with pytest.raises(TypeError):
        word_frequency_dataframe(123)