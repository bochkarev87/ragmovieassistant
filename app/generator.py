from app.retriever import Retriever
from app.prompts import format_answer_from_chunks, get_sources

class Generator:
    def __init__(self, retriever=None):
        self.retriever = retriever or Retriever()

    def ask(self, query: str, k: int = 3, threshold: float = 0.1):
        results = self.retriever.search(query, k=k)
        answer = format_answer_from_chunks(results, query, threshold)
        sources = get_sources(results, threshold)
        return answer, sources
