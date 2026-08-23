from pathlib import Path

from services.document_builder import build_document


def test_build_document_from_txt(tmp_path):
    file_path = tmp_path / "test.txt"

    file_path.write_text(
        "Python is easy. Python is powerful.",
        encoding="utf-8",
    )

    document = build_document(str(file_path))

    assert document.metadata["filename"] == "test.txt"
    assert document.metadata["extension"] == ".txt"

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

    assert document.top_words[0] == ("python", 2)
    assert document.top_words[1] == ("is", 2)


def test_build_document_persian(tmp_path):
    file_path = tmp_path / "persian.txt"

    file_path.write_text(
        "سلام دنیا. من پایتون را دوست دارم.",
        encoding="utf-8",
    )

    document = build_document(str(file_path))

    assert document.language == "persian"

    assert len(document.sentences) == 2

    assert "سلام" in document.words
    assert "پایتون" in document.words


def test_build_document_empty_file(tmp_path):
    file_path = tmp_path / "empty.txt"

    file_path.write_text(
        "",
        encoding="utf-8",
    )

    document = build_document(str(file_path))

    assert document.normalized_text == ""
    assert document.sentences == []
    assert document.words == []
    assert document.top_words == []

    assert document.statistics["word_count"] == 0
    assert document.statistics["sentence_count"] == 0


def test_build_document_nonexistent_file(tmp_path):
    file_path = tmp_path / "missing.txt"

    try:
        build_document(str(file_path))
        assert False
    except FileNotFoundError:
        assert True