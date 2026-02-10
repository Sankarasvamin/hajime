from fastapi.testclient import TestClient

from server.main import app


client = TestClient(app)


def test_translate_returns_artistic_field():
  response = client.post("/translate", json={"text": "我要开会"})

  assert response.status_code == 200
  data = response.json()
  assert "artistic" in data
