# Iter 00: Scaffold

## Что сделать
Подготовить каркас проекта и окружение.

## Какие файлы
- `pyproject.toml` — зависимости: streamlit, scikit-learn, pytest
- `.gitignore` — `.venv/`, `data/index/`, `__pycache__/`
- Папки: `app/`, `scripts/`, `data/raw/`, `data/processed/`, `data/index/`, `tests/`
- `app/config.py` — пути, top_k, размер чанка

## Как проверить
```bash
uv venv && uv sync
uv run python -c "import app.config"