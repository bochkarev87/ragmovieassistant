# Домашнее задание: RAG Киноассистент

## Ссылка на репозиторий
https://github.com/bochkarev87/ragmovieassistant

## Что сделано
- Полный RAG pipeline (ingest → chunking → index → retrieval → answer → UI)
- 11 фильмов в датасете
- Streamlit интерфейс с источниками
- Negative-вопрос даёт отказ

## Запуск
```bash
uv sync
uv run python scripts/build_index.py
uv run streamlit run app/main.py