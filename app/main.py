import streamlit as st
from pathlib import Path
import sys
import json
sys.path.append(str(Path(__file__).parent.parent))
from app.generator import Generator

INDEX_PATH = Path(__file__).parent.parent / "data" / "index"
DATASETS_PATH = Path(__file__).parent.parent / "data" / "raw" / "datasets.json"
INDEX_EXISTS = (INDEX_PATH / "vectorizer.pkl").exists()

st.set_page_config(page_title="Киноассистент", page_icon="🎬")
st.title("🎬 Киноассистент")
st.markdown("Задайте вопрос о фильмах на русском языке")

if not INDEX_EXISTS:
    st.error("⚠️ Индекс не найден! Запустите `uv run python scripts/build_index.py`")
    st.stop()

@st.cache_resource
def load_generator():
    return Generator()

gen = load_generator()

# Загружаем все фильмы из датасета для демо-вопросов
def get_all_movies():
    with open(DATASETS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["datasets"]

movies = get_all_movies()

# Генерируем демо-вопросы на основе жанров из датасета
def generate_demo_questions(movies, limit=5):
    questions = []
    genres_map = {
        "ужасы": "фильм ужасов про клоуна",
        "комедия": "комедия про дружбу", 
        "фантастика": "фантастика про космос",
        "боевик": "боевик про месть",
        "триллер": "триллер про потерю памяти",
        "детектив": "детектив расследование",
        "драма": "драма про жизнь",
        "криминал": "криминальный фильм",
        "мюзикл": "музыкальный фильм про любовь",
        "мелодрама": "романтический фильм"
    }
    for movie in movies[:limit]:
        text = movie.get("text", "").lower()
        for genre, question in genres_map.items():
            if genre in text and question not in questions:
                questions.append(question)
                break
    if not questions:
        questions = ["фильм про космос", "комедия", "боевик", "как приготовить пиццу"]
    return questions[:4]

demo_questions = generate_demo_questions(movies)

st.subheader("Примеры вопросов:")
cols = st.columns(len(demo_questions))
for i, q in enumerate(demo_questions):
    if cols[i].button(q, key=f"demo_{i}"):
        st.session_state.query = q

query = st.text_input("Ваш вопрос:", value=st.session_state.get("query", ""))
if query:
    with st.spinner("Поиск..."):
        answer, sources = gen.ask(query)
    st.subheader("📝 Ответ")
    st.markdown(answer)
    st.subheader("📚 Источники")
    if sources:
        for src in sources:
            with st.expander(f"**{src['name']}** — релевантность: {src['score']:.2f}"):
                st.markdown(f"doc_id: `{src['doc_id']}`")
                st.markdown(f"Фрагмент: {src['fragment']}")
    else:
        st.info("Нет релевантных фильмов. Попробуйте переформулировать вопрос.")