from services.document import Document


def test_document_creation():
    document = Document(
        metadata={
            "filename": "test.txt",
            "extension": ".txt",
            "size": 100,
        },
        language="english",
        sentences=["Hello world."],
        words=["hello", "world"],
        normalized_text="hello world",
        top_words=[("hello", 1), ("world", 1)],
        statistics={
            "character_count": 12,
            "word_count": 2,
            "sentence_count": 1,
            "unique_word_count": 2,
            "average_word_length": 5.0,
        },
    )

    assert document.metadata["filename"] == "test.txt"
    assert document.language == "english"
    assert document.sentences == ["Hello world."]
    assert document.words == ["hello", "world"]
    assert document.normalized_text == "hello world"


def test_document_top_words():
    document = Document(
        metadata={},
        language="english",
        sentences=[],
        words=["python", "python", "java"],
        normalized_text="python python java",
        top_words=[
            ("python", 2),
            ("java", 1),
        ],
        statistics={},
    )

    assert document.top_words[0] == ("python", 2)
    assert document.top_words[1] == ("java", 1)


def test_document_statistics():
    statistics = {
        "character_count": 20,
        "word_count": 4,
        "sentence_count": 2,
        "unique_word_count": 3,
        "average_word_length": 4.5,
    }

    document = Document(
        metadata={},
        language="english",
        sentences=[],
        words=[],
        normalized_text="",
        top_words=[],
        statistics=statistics,
    )

    assert document.statistics["word_count"] == 4
    assert document.statistics["sentence_count"] == 2
    assert document.statistics["unique_word_count"] == 3


def test_document_empty_values():
    document = Document(
        metadata={},
        language="unknown",
        sentences=[],
        words=[],
        normalized_text="",
        top_words=[],
        statistics={},
    )

    assert document.metadata == {}
    assert document.language == "unknown"
    assert document.sentences == []
    assert document.words == []
    assert document.normalized_text == ""
    assert document.top_words == []
    assert document.statistics == {}


def test_document_accepts_language():
    document = Document(
        metadata={},
        language="unknown",
        sentences=[],
        words=[],
        normalized_text="",
        top_words=[],
        statistics={},
    )

    assert document.language == "unknown"