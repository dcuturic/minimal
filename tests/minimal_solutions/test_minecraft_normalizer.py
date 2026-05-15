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

def test_minecraft_normalizer_happy_path(client):
    response = client.post('/api/minimal-solutions/minecraft_normalizer', json={
        "input_text": "  Welcome to   Minecraft  \n   Server  ",
        "mode": "lowercase",
        "options": {}
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "data" in data
    assert data["data"]["normalized_text"] == "welcome to minecraft\nserver"

def test_minecraft_normalizer_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_normalizer', json={
        "input_text": "",
        "mode": "default",
        "options": {}
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data or "code" in data

def test_minecraft_normalizer_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_normalizer', json={
        "input_text": "Test",
        "mode": 123,  # Should be string
        "options": {}
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data or "code" in data
