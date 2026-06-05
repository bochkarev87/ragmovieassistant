import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATASETS_JSON = PROJECT_ROOT / "data" / "raw" / "datasets.json"
DOCUMENTS_JSONL = PROJECT_ROOT / "data" / "processed" / "documents.jsonl"

def main():
    PROJECT_ROOT / "data" / "processed" / "documents.jsonl"
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
    print(f"Создано {len(datasets)} документов в {DOCUMENTS_JSONL}")

if __name__ == "__main__":
    main()