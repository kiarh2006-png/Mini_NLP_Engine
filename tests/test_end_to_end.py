import json

from services.document_builder import build_document
from services.json_handler import save_document


def test_full_pipeline_txt(tmp_path):
    # 1. ساخت فایل ورودی
    input_file = tmp_path / "input.txt"

    input_file.write_text(
        "Python is easy. Python is powerful.",
        encoding="utf-8",
    )

    # 2. ساخت Document
    document = build_document(str(input_file))

    # 3. بررسی Document
    assert document.metadata["filename"] == "input.txt"
    assert document.language == "english"

    assert document.sentences == [
        "Python is easy.",
        "Python is powerful.",
    ]

    assert document.words == [
        "python",
        "is",
        "easy",
        "python",
        "is",
        "powerful",
    ]

    assert document.normalized_text == (
        "python is easy python is powerful"
    )

    assert document.statistics["word_count"] == 6
    assert document.statistics["sentence_count"] == 2

    # 4. ذخیره JSON
    output_file = tmp_path / "output.json"

    save_document(
        document,
        str(output_file),
    )

    # 5. بررسی JSON
    assert output_file.exists()

    with open(
        output_file,
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    assert data["language"] == "english"
    assert data["metadata"]["filename"] == "input.txt"
    assert data["normalized_text"] == (
        "python is easy python is powerful"
    )


def test_full_pipeline_persian(tmp_path):
    input_file = tmp_path / "persian.txt"

    input_file.write_text(
        "سلام دنیا. من پایتون را دوست دارم.",
        encoding="utf-8",
    )

    document = build_document(str(input_file))

    assert document.language == "persian"

    assert len(document.sentences) == 2

    assert "سلام" in document.words
    assert "پایتون" in document.words

    assert document.statistics["word_count"] == 7


def test_full_pipeline_mixed(tmp_path):
    input_file = tmp_path / "mixed.txt"

    input_file.write_text(
        "Python عالی است. من Python را دوست دارم.",
        encoding="utf-8",
    )

    document = build_document(str(input_file))

    assert document.language == "mixed"

    assert len(document.sentences) == 2

    assert "python" in document.words
    assert "عالی" in document.words


def test_full_pipeline_empty_file(tmp_path):
    input_file = tmp_path / "empty.txt"

    input_file.write_text(
        "",
        encoding="utf-8",
    )

    document = build_document(str(input_file))

    assert document.language == "unknown"
    assert document.sentences == []
    assert document.words == []
    assert document.top_words == []

    assert document.statistics["word_count"] == 0
    assert document.statistics["sentence_count"] == 0