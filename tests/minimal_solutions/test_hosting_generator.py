from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hosting_generator_happy_path():
    response = client.post(
        "/api/minimal-solutions/hosting_generator",
        json={
            "source": "https://github.com/my-org/my-app",
            "config": "Node.js v18, PostgreSQL",
            "mode": "auto-scale"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["data"]["source"] == "https://github.com/my-org/my-app"
    assert data["data"]["config"] == "Node.js v18, PostgreSQL"
    assert data["data"]["mode"] == "auto-scale"
    assert "hosting_suggestion" in data["data"]

def test_hosting_generator_empty_input():
    response = client.post(
        "/api/minimal-solutions/hosting_generator",
        json={}
    )
    assert response.status_code == 400
    data = response.json()
    assert data["status"] == "error"

def test_hosting_generator_invalid_input():
    response = client.post(
        "/api/minimal-solutions/hosting_generator",
        json={
            "source": 12345,  # Erwartet str
            "config": ["not", "a", "string"],  # Erwartet str
            "mode": True
        }
    )
    assert response.status_code == 400
    data = response.json()
    assert data["status"] == "error"
