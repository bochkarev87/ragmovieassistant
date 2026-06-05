# Iter 04: TF-IDF Index

**Ориентир:** `scripts/build_index.py`

## Что сделать
Построить индекс: ingest + chunk + TF-IDF fit.  
Сохранить артефакты индекса.

## Какие файлы
- `scripts/build_index.py`
- `data/index/vectorizer.pkl` (генерируется)
- `data/index/matrix.npz` (генерируется)
- `data/index/chunks.jsonl` (генерируется)

## Как проверить
```bash
uv run python scripts/build_index.py