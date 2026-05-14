import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_minecraft_motd_preview_happy_path(client):
    response = client.post('/api/minimal-solutions/minecraft_motd_preview', json={
        "motd_text": "§aA Minecraft Server"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert "data" in data
    assert "motd_text" in data["data"]
    assert data["data"]["motd_text"] == "§aA Minecraft Server"

def test_minecraft_motd_preview_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_motd_preview', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert "error" in data
    assert data["error"]["code"] == "VALIDATION_ERROR"

def test_minecraft_motd_preview_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_motd_preview', json={
        "motd_text": 12345
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert "error" in data
    assert data["error"]["code"] == "VALIDATION_ERROR"
