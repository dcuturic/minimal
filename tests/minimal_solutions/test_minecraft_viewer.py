import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_minecraft_viewer_happy_path(client):
    response = client.post('/api/minimal-solutions/minecraft_viewer', json={
        "input_text": "sample input text",
        "mode": "standard",
        "options": {
            "strict": True
        }
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["input_text"] == "sample input text"
    assert data["data"]["mode"] == "standard"
    assert "result" in data["data"]
    assert "viewer_status" in data["data"]["result"]

def test_minecraft_viewer_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_viewer', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "input_text" in data["error"]["details"]
    assert "mode" in data["error"]["details"]

def test_minecraft_viewer_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_viewer', json={
        "input_text": 123,
        "mode": "s",
        "options": "invalid"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "input_text" in data["error"]["details"]
    assert "mode" in data["error"]["details"]
    assert "options" in data["error"]["details"]
