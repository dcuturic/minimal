import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_minecraft_summarizer_happy_path(client):
    response = client.post('/api/minimal-solutions/minecraft_summarizer', json={
        "input_text": "Here is a large text about Minecraft servers. Server performance is important. Lag is bad.",
        "mode": "performance",
        "options": {
            "format": "bullet_points"
        }
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["input_text"] == "Here is a large text about Minecraft servers. Server performance is important. Lag is bad."
    assert data["data"]["mode"] == "performance"
    assert "result" in data["data"]
    assert "summary_text" in data["data"]["result"]

def test_minecraft_summarizer_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_summarizer', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "input_text" in data["error"]["details"]
    assert "mode" in data["error"]["details"]

def test_minecraft_summarizer_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_summarizer', json={
        "input_text": 123,
        "mode": 456,
        "options": "invalid"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "input_text" in data["error"]["details"]
    assert "mode" in data["error"]["details"]
    assert "options" in data["error"]["details"]
