# Vision — техническое видение проекта

Учебный RAG на описаниях фильмов из датасета TMDB: локально, просто, с ответом и источниками.

## 1. Технологии

| Слой | Выбор |
|------|-------|
| Язык | Python 3.10+ |
| Окружение | uv + .venv |
| UI | Streamlit |
| Поиск | TF-IDF + cosine similarity (scikit-learn) |
| Индекс | Локальные файлы (data/index/) |
| LLM | Только demo-режим (без внешнего API) |
| Данные | TMDB датасет с Kaggle → data/raw/datasets.json |
| Тесты | pytest |
| Зависимости | pyproject.toml + uv |

## 2. Как строится индекс

1. Из датасета берём поля: title, overview, genres, release_date, vote_average.
2. Каждый фильм → один текстовый документ (название + жанры + описание).
3. TF-IDF векторизация через scikit-learn.
4. Сохраняем vectorizer.pkl, matrix.npz, chunks.jsonl в data/index/.

## 3. Как работает поиск

- Вопрос пользователя векторизуется через тот же TF-IDF.
- Считается косинусное сходство со всеми чанками.
- Возвращаются топ-3 фильма с наибольшей релевантностью.
- Ответ формируется без LLM — просто вывод найденных фильмов с источниками.

## 4. Что не используем в MVP

ChromaDB, sentence-transformers, torch, LangChain, FastAPI, Docker, OpenAI, Kaggle API, pip/poetry/conda.

## 5. Как запускать

uv sync
uv run python scripts/build_index.py
uv run streamlit run app/main.py
