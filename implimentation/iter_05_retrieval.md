# Iter 05: Retrieval

**Ориентир:** `app/retriever.py`, `scripts/check_retrieval.py`

## Что сделать
Реализовать поиск top-k чанков по cosine similarity.  
Возвращать `text`, `doc_id`, `score` (и `name` как метаданные).

## Какие файлы
- `app/retriever.py`
- `scripts/check_retrieval.py` (для проверки)

## Как проверить
```bash
uv run python scripts/check_retrieval.py