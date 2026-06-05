import pytest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from app.retriever import Retriever

@pytest.fixture(scope="module")
def retriever():
    return Retriever()

def test_retriever_loads(retriever):
    assert retriever.vectorizer is not None
    assert len(retriever.chunks) > 0

def test_search_returns_k(retriever):
    res = retriever.search("фантастика", k=3)
    assert len(res) == 3

def test_search_scores(retriever):
    res = retriever.search("комедия")
    scores = [s for _, _, s in res]
    assert max(scores) > 0