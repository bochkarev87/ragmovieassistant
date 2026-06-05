# Tasklist — итерационный план разработки

**Опирается на:** `vision.md` · `conventions.md` · `00_project_idea.md`

**Правило:** одна итерация = один проверяемый результат. Не переходить дальше, пока текущий шаг не протестирован.

---

## 📊 Отчёт по прогрессу

| Итерация | Название | Статус | Проверка |
|----------|----------|--------|----------|
| 0 | Каркас проекта | ⬜ | `uv sync` без ошибок |
| 1 | Данные фильмов | ⬜ | JSON читается, ≥10 фильмов |
| 2 | Ingestion | ⬜ | `documents.jsonl` создан |
| 3 | Chunking | ⬜ | `chunks.jsonl`, тест chunking |
| 4 | Индекс TF-IDF | ⬜ | файлы в `data/index/` |
| 5 | Retrieval | ⬜ | top-k + score в консоли |
| 6 | Demo-ответ | ⬜ | ответ + источники без UI |
| 7 | Streamlit UI | ⬜ | 3 demo-вопроса в браузере |
| 8 | Тесты и README | ⬜ | pytest green, README воспроизводим |

**Легенда:** ⬜ не начато · 🔄 в работе · ✅ готово · ❌ блокер

**Текущая итерация:** 0  
**Готовность MVP:** 0 / 9

---

## Итерация 0 — Каркас проекта

- [ ] `pyproject.toml` — зависимости: streamlit, scikit-learn, pytest, numpy
- [ ] `.gitignore` — `.venv/`, `data/index/`, `__pycache__/`
- [ ] Папки: `app/`, `scripts/`, `data/raw/`, `data/processed/`, `data/index/`, `tests/`, `doc/`
- [ ] `app/config.py` — пути, top_k=3

**Проверка:**
```bash
uv venv && uv sync
uv run python -c "import app.config"
