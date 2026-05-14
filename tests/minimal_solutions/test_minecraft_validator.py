import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_minecraft_validator_happy_path(client):
    response = client.post('/api/minimal-solutions/minecraft_validator', json={
        "input_text": "Notch",
        "mode": "username",
        "options": {
            "strict_mode": True
        }
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["input_text"] == "Notch"
    assert data["data"]["mode"] == "username"
    assert data["data"]["is_valid"] == True

def test_minecraft_validator_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_validator', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "input_text" in data["error"]["details"]
    assert "mode" in data["error"]["details"]

def test_minecraft_validator_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_validator', json={
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
