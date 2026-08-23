from services.document import Document
from services.file_reader import read_file
from services.language_detector import LanguageDetector
from services.metadata import get_metadata
from services.text_processor import (
    get_statistics,
    normalize_text,
    split_sentences,
    tokenize_words,
    top_words,
)


# مدل فقط یک بار ساخته و آموزش داده می‌شود
language_detector = LanguageDetector()


def build_document(file_path: str) -> Document:
    """Read a file and build a complete Document."""

    # خواندن محتوای فایل
    raw_text = read_file(file_path)

    # اطلاعات فایل
    metadata = get_metadata(file_path)

    # پردازش متن
    normalized_text = normalize_text(raw_text)
    sentences = split_sentences(raw_text)
    words = tokenize_words(raw_text)

    # تحلیل متن
    document_top_words = top_words(raw_text)
    statistics = get_statistics(raw_text)

    # تشخیص زبان
    language = language_detector.detect(raw_text)

    # ساخت خروجی نهایی
    return Document(
        metadata=metadata,
        language=language,
        sentences=sentences,
        words=words,
        normalized_text=normalized_text,
        top_words=document_top_words,
        statistics=statistics,
    )