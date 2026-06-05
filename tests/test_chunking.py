import json
import pytest
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from app.chunker import chunk_by_paragraphs, chunk_documents
from app.config import CHUNKS_JSONL

def test_chunk_by_paragraphs():
    text = "Параграф 1.\n\nПараграф 2. Длинный текст."
    chunks = chunk_by_paragraphs(text, max_chars=30, overlap=5)
    assert len(chunks) >= 1

def test_chunk_documents_creates_file():
    if CHUNKS_JSONL.exists():
        CHUNKS_JSONL.unlink()
    chunk_documents()
    assert CHUNKS_JSONL.exists()
    with open(CHUNKS_JSONL) as f:
        lines = f.readlines()
    assert len(lines) > 0

def test_chunk_has_required_fields():
    with open(CHUNKS_JSONL) as f:
        for line in f:
            c = json.loads(line)
            assert "chunk_id" in c
            assert "doc_id" in c
            assert "text" in c
            assert len(c["text"]) > 0