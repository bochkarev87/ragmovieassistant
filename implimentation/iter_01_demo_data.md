# Iter 01: Demo Data

**Ориентир:** `doc/tasklist.md`, `scripts/prepare_datasets.py`

## Что сделать
Подготовить `data/raw/datasets.json` с текстовыми записями фильмов для RAG.

## Какие файлы
- `data/raw/datasets.json` — JSON с ключом `datasets`, массив объектов:
  ```json
  {
    "datasets": [
      {
        "id": 0,
        "name": "Название фильма",
        "text": "Описание + жанры + год + рейтинг"
      },
      ...
    ]
  }