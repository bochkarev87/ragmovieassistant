import sys
import json
import pickle
import numpy as np
import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT))

DOCUMENTS_JSONL = PROJECT_ROOT / "data" / "processed" / "documents.jsonl"
CHUNKS_JSONL = PROJECT_ROOT / "data" / "processed" / "chunks.jsonl"
DATA_INDEX = PROJECT_ROOT / "data" / "index"
VECTORIZER_PATH = DATA_INDEX / "vectorizer.pkl"
MATRIX_PATH = DATA_INDEX / "matrix.npz"
INDEX_CHUNKS_PATH = DATA_INDEX / "chunks.jsonl"

def run_ingest():
    DATASETS_JSON = PROJECT_ROOT / "data" / "raw" / "datasets.json"
    with open(DATASETS_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
        datasets = data["datasets"]
    DOCUMENTS_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with open(DOCUMENTS_JSONL, "w", encoding="utf-8") as out:
        for rec in datasets:
            doc = {
                "doc_id": str(rec["id"]),
                "name": rec["name"],
                "text": rec["text"],
                "source_file": "datasets.json"
            }
            out.write(json.dumps(doc, ensure_ascii=False) + "\n")
    print(f"Создано {len(datasets)} документов")

def chunk_documents():
    chunks = []
    with open(DOCUMENTS_JSONL, "r", encoding="utf-8") as f:
        for line in f:
            doc = json.loads(line)
            chunks.append({
                "chunk_id": f"{doc['doc_id']}_0",
                "doc_id": doc["doc_id"],
                "name": doc.get("name", ""),
                "text": doc["text"],
                "metadata": {}
            })
    CHUNKS_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with open(CHUNKS_JSONL, "w", encoding="utf-8") as f:
        for ch in chunks:
            f.write(json.dumps(ch, ensure_ascii=False) + "\n")
    print(f"Создано {len(chunks)} чанков")

def build():
    if not DOCUMENTS_JSONL.exists():
        print("Запуск ingestion...")
        run_ingest()
    if not CHUNKS_JSONL.exists():
        print("Запуск chunking...")
        chunk_documents()
    print("Загрузка чанков...")
    chunks = []
    with open(CHUNKS_JSONL, "r", encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))
    texts = [c["text"] for c in chunks]
    print(f"Всего чанков: {len(texts)}")
    from sklearn.feature_extraction.text import TfidfVectorizer
    from scipy.sparse import csr_matrix
    vectorizer = TfidfVectorizer(max_features=5000, lowercase=True)
    tfidf = vectorizer.fit_transform(texts)
    print(f"Размер матрицы: {tfidf.shape}")
    DATA_INDEX.mkdir(parents=True, exist_ok=True)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)
    csr = csr_matrix(tfidf)
    np.savez(MATRIX_PATH, data=csr.data, indices=csr.indices, indptr=csr.indptr, shape=csr.shape)
    shutil.copy2(CHUNKS_JSONL, INDEX_CHUNKS_PATH)
    print("Индекс готов.")

if __name__ == "__main__":
    build()