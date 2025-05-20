from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={"description": "A team of astronauts travel to space."})
    assert response.status_code == 200
    assert 'genre' in response.json()
    assert 'confidence' in response.json()