import json
import pickle
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
VECTORIZER_PATH = PROJECT_ROOT / "data" / "index" / "vectorizer.pkl"
MATRIX_PATH = PROJECT_ROOT / "data" / "index" / "matrix.npz"
INDEX_CHUNKS_PATH = PROJECT_ROOT / "data" / "index" / "chunks.jsonl"

class Retriever:
    def __init__(self):
        self.vectorizer = None
        self.tfidf_matrix = None
        self.chunks = []
        self._load_index()

    def _load_index(self):
        if not VECTORIZER_PATH.exists():
            raise FileNotFoundError(f"Index not found: {VECTORIZER_PATH}")
        with open(VECTORIZER_PATH, "rb") as f:
            self.vectorizer = pickle.load(f)
        loaded = np.load(MATRIX_PATH)
        self.tfidf_matrix = csr_matrix((loaded['data'], loaded['indices'], loaded['indptr']), shape=loaded['shape'])
        with open(INDEX_CHUNKS_PATH, "r", encoding="utf-8") as f:
            self.chunks = [json.loads(line) for line in f]

    def search(self, query: str, k: int = 3):
        q_vec = self.vectorizer.transform([query])
        sim = cosine_similarity(q_vec, self.tfidf_matrix).flatten()
        top_idx = np.argsort(sim)[::-1][:k]
        results = []
        for idx in top_idx:
            score = float(sim[idx])
            chunk = self.chunks[idx]
            meta = {
                "doc_id": chunk["doc_id"],
                "name": chunk.get("name", ""),
                "chunk_id": chunk["chunk_id"]
            }
            results.append((chunk["text"], meta, score))
        return results