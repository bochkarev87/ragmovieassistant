import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from app.retriever import Retriever

r = Retriever()
queries = ["научная фантастика космос", "комедия рейтинг", "потеря памяти", "пицца"]
for q in queries:
    print(f"\nЗапрос: {q}")
    results = r.search(q, k=2)
    for text, meta, score in results:
        print(f"  {meta['name']} (score={score:.3f})")