import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_minecraft_splitter_happy_path(client):
    response = client.post('/api/minimal-solutions/minecraft_splitter', json={
        "input_text": "Split this long text into smaller manageable pieces for Minecraft chat.",
        "mode": "chat",
        "options": {
            "max_length": 256
        }
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "data" in data

def test_minecraft_splitter_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_splitter', json={
        "input_text": "",
        "mode": "chat",
        "options": {}
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data or "code" in data

def test_minecraft_splitter_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_splitter', json={
        "input_text": "Valid text but invalid mode type.",
        "mode": 12345,  # Should be string
        "options": {}
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data or "code" in data
