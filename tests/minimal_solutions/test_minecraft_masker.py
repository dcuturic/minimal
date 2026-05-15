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

def test_minecraft_masker_happy_path(client):
    response = client.post('/api/minimal-solutions/minecraft_masker', json={
        "input_text": "mask this text",
        "mode": "basic",
        "options": {}
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "result" in data

def test_minecraft_masker_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_masker', json={
        "input_text": "",
        "mode": "basic",
        "options": {}
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data

def test_minecraft_masker_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_masker', json={
        "input_text": "test",
        "mode": "unknown_mode_123",
        "options": {}
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
