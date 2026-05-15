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

def test_minecraft_cleaner_happy_path(client):
    response = client.post('/api/minimal-solutions/minecraft_cleaner', json={
        "input_text": "§aHello §bWorld",
        "mode": "basic",
        "options": {
            "remove_empty": False
        }
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "data" in data

def test_minecraft_cleaner_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_cleaner', json={
        "input_text": "",
        "mode": "basic",
        "options": {}
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data or "code" in data

def test_minecraft_cleaner_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_cleaner', json={
        "input_text": "Valid text",
        "mode": 123,  # Should be string
        "options": {}
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data or "code" in data
