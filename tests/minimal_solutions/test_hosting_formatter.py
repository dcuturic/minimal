from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hosting_formatter_happy_path():
    response = client.post(
        "/api/minimal-solutions/hosting_formatter",
        json={
            "source": "https://github.com/my-org/my-react-app",
            "config": "React, Nginx",
            "mode": "static"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["data"]["source"] == "https://github.com/my-org/my-react-app"
    assert data["data"]["config"] == "React, Nginx"
    assert data["data"]["mode"] == "static"
    assert "formatted_hosting" in data["data"]

def test_hosting_formatter_empty_input():
    response = client.post(
        "/api/minimal-solutions/hosting_formatter",
        json={}
    )
    assert response.status_code == 400
    data = response.json()
    assert data["status"] == "error"

def test_hosting_formatter_invalid_input():
    response = client.post(
        "/api/minimal-solutions/hosting_formatter",
        json={
            "source": 12345,  # Erwartet str
            "config": ["not", "a", "string"],  # Erwartet str
            "mode": True
        }
    )
    assert response.status_code == 400
    data = response.json()
    assert data["status"] == "error"
