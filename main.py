from services.document_builder import build_document
from services.json_handler import save_document


def main() -> None:
    """Run the Mini NLP Engine."""

    print("========== MINI NLP ENGINE ==========")

    file_path = input("Enter file path: ").strip()

    if not file_path:
        print("Error: file path cannot be empty.")
        return

    try:
        document = build_document(file_path)

        print("\n========== DOCUMENT ==========\n")

        print("Metadata:")
        print(document.metadata)

        print("\nLanguage:")
        print(document.language)

        print("\nNormalized Text:")
        print(document.normalized_text)

        print("\nSentences:")
        for index, sentence in enumerate(
            document.sentences,
            start=1,
        ):
            print(f"{index}. {sentence}")

        print("\nWords:")
        print(document.words)

        print("\nTop Words:")
        for word, count in document.top_words:
            print(f"{word}: {count}")

        print("\nStatistics:")
        for key, value in document.statistics.items():
            print(f"{key}: {value}")

        output_path = "output.json"

        save_document(
            document,
            output_path,
        )

        print(
            f"\nJSON saved successfully: {output_path}"
        )

    except FileNotFoundError as error:
        print(f"Error: {error}")

    except ValueError as error:
        print(f"Error: {error}")

    except IsADirectoryError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()