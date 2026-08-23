import json

from services.document import Document
from services.json_handler import save_document


def create_test_document():
    return Document(
        metadata={
            "filename": "test.txt",
            "extension": ".txt",
            "size": 100,
        },
        language="english",
        sentences=["Hello world."],
        words=["hello", "world"],
        normalized_text="hello world",
        top_words=[
            ("hello", 1),
            ("world", 1),
        ],
        statistics={
            "character_count": 12,
            "word_count": 2,
            "sentence_count": 1,
            "unique_word_count": 2,
            "average_word_length": 5.0,
        },
    )


def test_save_document(tmp_path):
    document = create_test_document()

    output_file = tmp_path / "output.json"

    save_document(document, str(output_file))

    assert output_file.exists()


def test_save_document_contains_correct_data(tmp_path):
    document = create_test_document()

    output_file = tmp_path / "output.json"

    save_document(document, str(output_file))

    with open(
        output_file,
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    assert data["language"] == "english"
    assert data["metadata"]["filename"] == "test.txt"
    assert data["normalized_text"] == "hello world"


def test_save_document_persian(tmp_path):
    document = Document(
        metadata={
            "filename": "persian.txt",
            "extension": ".txt",
            "size": 50,
        },
        language="persian",
        sentences=["سلام دنیا."],
        words=["سلام", "دنیا"],
        normalized_text="سلام دنیا",
        top_words=[
            ("سلام", 1),
            ("دنیا", 1),
        ],
        statistics={
            "character_count": 10,
            "word_count": 2,
            "sentence_count": 1,
            "unique_word_count": 2,
            "average_word_length": 4.0,
        },
    )

    output_file = tmp_path / "persian.json"

    save_document(document, str(output_file))

    with open(
        output_file,
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    assert data["language"] == "persian"
    assert data["normalized_text"] == "سلام دنیا"


def test_save_document_invalid_type(tmp_path):
    output_file = tmp_path / "output.json"

    try:
        save_document("not a document", str(output_file))
        assert False
    except TypeError:
        assert True