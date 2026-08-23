from pathlib import Path

from docx import Document
from pypdf import PdfReader


def read_file(file_path: str) -> str:
    """Read text from TXT, PDF, or DOCX files."""

    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    if not path.is_file():
        raise IsADirectoryError(
            f"Path is not a file: {file_path}"
        )

    extension = path.suffix.lower()

    if extension == ".txt":
        return _read_txt(path)

    if extension == ".pdf":
        return _read_pdf(path)

    if extension == ".docx":
        return _read_docx(path)

    raise ValueError(
        f"Unsupported file type: {extension}"
    )


def _read_txt(path: Path) -> str:
    """Read a TXT file."""

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as file:
        return file.read()


def _read_pdf(path: Path) -> str:
    """Read text from a PDF file."""

    reader = PdfReader(path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)


def _read_docx(path: Path) -> str:
    """Read text from a DOCX file."""

    document = Document(str(path))

    paragraphs = []

    for paragraph in document.paragraphs:
        if paragraph.text:
            paragraphs.append(paragraph.text)

    return "\n".join(paragraphs)