import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from app.generator import Generator

gen = Generator()
queries = ["научная фантастика космос", "комедия рейтинг", "потеря памяти", "пицца"]
for q in queries:
    print(f"\n=== {q} ===")
    ans, src = gen.ask(q)
    print("Ответ:", ans[:200])
    print("Источники:", [s["name"] for s in src])