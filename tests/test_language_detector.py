import pytest

from services.language_detector import LanguageDetector


@pytest.fixture
def detector():
    return LanguageDetector()


def test_detect_english(detector):
    text = "Hello, how are you? Python is a powerful programming language."

    result = detector.detect(text)

    assert result == "english"


def test_detect_persian(detector):
    text = "سلام، حالت چطوره؟ من به برنامه نویسی پایتون علاقه دارم."

    result = detector.detect(text)

    assert result == "persian"


def test_detect_empty_text(detector):
    result = detector.detect("")

    assert result == "unknown"


def test_detect_whitespace(detector):
    result = detector.detect("     ")

    assert result == "unknown"


def test_detect_non_string(detector):
    with pytest.raises(TypeError):
        detector.detect(123)


def test_detect_english_short_text(detector):
    result = detector.detect("hello world")

    assert result == "english"


def test_detect_persian_short_text(detector):
    result = detector.detect("سلام دنیا")

    assert result == "persian"
def test_detect_mixed_text(detector):
    text = "Python is عالی و من پایتون را دوست دارم."

    result = detector.detect(text)

    assert result == "mixed"


def test_detect_mixed_short_text(detector):
    result = detector.detect("Hello سلام")

    assert result == "mixed"