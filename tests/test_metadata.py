from pathlib import Path

import pytest

from services.metadata import get_metadata


def test_get_metadata(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("Hello world", encoding="utf-8")

    result = get_metadata(str(file_path))

    assert result["filename"] == "test.txt"
    assert result["extension"] == ".txt"
    assert result["size"] == 11


def test_get_metadata_pdf_extension(tmp_path):
    file_path = tmp_path / "document.PDF"
    file_path.write_text("test", encoding="utf-8")

    result = get_metadata(str(file_path))

    assert result["filename"] == "document.PDF"
    assert result["extension"] == ".pdf"


def test_get_metadata_empty_file(tmp_path):
    file_path = tmp_path / "empty.txt"
    file_path.write_text("", encoding="utf-8")

    result = get_metadata(str(file_path))

    assert result["filename"] == "empty.txt"
    assert result["extension"] == ".txt"
    assert result["size"] == 0


def test_get_metadata_nonexistent_file(tmp_path):
    file_path = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        get_metadata(str(file_path))


def test_get_metadata_returns_dictionary(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("Hello", encoding="utf-8")

    result = get_metadata(str(file_path))

    assert isinstance(result, dict)


def test_get_metadata_has_required_keys(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("Hello", encoding="utf-8")

    result = get_metadata(str(file_path))

    assert set(result.keys()) == {
        "filename",
        "extension",
        "size",
    }