from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict():
    response = client.get("/predict")
    assert response.status_code == 200
    assert "prediction" in response.json()
