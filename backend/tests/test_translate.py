from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_get_translate_question():
    resp = client.get("/translate/question")
    assert resp.status_code == 200
    data = resp.json()
    assert "id" in data
    assert "hindi_text" in data


def test_get_topics_random():
    resp = client.get("/topics/random")
    assert resp.status_code == 200
    data = resp.json()
    assert "id" in data
    assert "topic" in data

