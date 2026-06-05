from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
DATA_INDEX = PROJECT_ROOT / "data" / "index"

TOP_K = 3
SIMILARITY_THRESHOLD = 0.1
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

DATASETS_JSON = DATA_RAW / "datasets.json"
DOCUMENTS_JSONL = DATA_PROCESSED / "documents.jsonl"
CHUNKS_JSONL = DATA_PROCESSED / "chunks.jsonl"

VECTORIZER_PATH = DATA_INDEX / "vectorizer.pkl"
MATRIX_PATH = DATA_INDEX / "matrix.npz"
INDEX_CHUNKS_PATH = DATA_INDEX / "chunks.jsonl"

for path in [DATA_RAW, DATA_PROCESSED, DATA_INDEX]:
    path.mkdir(parents=True, exist_ok=True)