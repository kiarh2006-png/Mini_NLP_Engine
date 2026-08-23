import re


class LanguageDetector:
    """Detect Persian, English, mixed, or unknown text."""

    def detect(self, text: str) -> str:
        """Return the detected language."""

        if not isinstance(text, str):
            raise TypeError("text must be a string")

        if not text.strip():
            return "unknown"

        persian_count = len(
            re.findall(
                r"[\u0600-\u06FF]",
                text,
            )
        )

        english_count = len(
            re.findall(
                r"[A-Za-z]",
                text,
            )
        )

        if persian_count == 0 and english_count == 0:
            return "unknown"

        if persian_count > 0 and english_count > 0:
            return "mixed"

        if persian_count > 0:
            return "persian"

        return "english"