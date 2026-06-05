# Iter 03: Chunking

**Ориентир:** `app/chunker.py`, `tests/test_chunking.py`

## Что сделать
Нарезать документы на чанки по абзацам. Соблюсти `max_chars` и `overlap`.

## Какие файлы
- `app/chunker.py`
- `data/processed/chunks.jsonl` (генерируется)
- `tests/test_chunking.py`

## Как проверить
```bash
uv run pytest tests/test_chunking.py -v