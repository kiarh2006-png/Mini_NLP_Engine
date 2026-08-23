# Mini NLP Engine

A modular Python-based NLP engine for processing TXT, PDF, and DOCX documents.

The project extracts text from documents, normalizes the text, detects the language, splits text into sentences and words, calculates statistics, finds the most frequent words, and exports the final document structure as JSON.

---

## Features

- Read TXT files
- Read PDF files
- Read DOCX files
- Extract document metadata
- Normalize text
- Split text into sentences
- Tokenize text into words
- Detect English and Persian text
- Detect mixed Persian/English text
- Calculate text statistics
- Find the most frequent words
- Use NumPy for numerical calculations
- Use Pandas for word-frequency analysis
- Export results to JSON
- Comprehensive automated tests with pytest
- Edge-case and error handling

---

## Project Structure

```text
Mini_NLP_Engine/
│
├── data/
│   └── file.txt
│
├── services/
│   ├── __init__.py
│   ├── document.py
│   ├── document_builder.py
│   ├── file_reader.py
│   ├── json_handler.py
│   ├── language_detector.py
│   ├── metadata.py
│   └── text_processor.py
│
├── tests/
│   ├── __init__.py
│   ├── test_document.py
│   ├── test_document_builder.py
│   ├── test_document_builder_formats.py
│   ├── test_file_reader.py
│   ├── test_json_handler.py
│   ├── test_language_detector.py
│   ├── test_metadata.py
│   └── test_text_processor.py
│
├── .gitignore
├── main.py
├── requirements.txt
└── README.md