import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_minecraft_converter_happy_path(client):
    response = client.post('/api/minimal-solutions/minecraft_converter', json={
        "input_text": "stone_block 0 0 0",
        "mode": "schematic_to_command",
        "options": {
            "version": "1.20"
        }
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["input_text"] == "stone_block 0 0 0"
    assert data["data"]["mode"] == "schematic_to_command"
    assert "result" in data["data"]
    assert "converted_text" in data["data"]["result"]

def test_minecraft_converter_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_converter', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "input_text" in data["error"]["details"]
    assert "mode" in data["error"]["details"]

def test_minecraft_converter_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_converter', json={
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
