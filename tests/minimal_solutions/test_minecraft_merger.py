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

def test_minecraft_merger_happy_path(client):
    response = client.post('/api/minimal-solutions/minecraft_merger', json={
        "input_text": "text part 1\ntext part 2\ntext part 3",
        "mode": "standard",
        "options": {
            "separator": " "
        }
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "data" in data

def test_minecraft_merger_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_merger', json={
        "input_text": "",
        "mode": "standard",
        "options": {}
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data or "code" in data

def test_minecraft_merger_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_merger', json={
        "input_text": "Valid text",
        "mode": 123,  # Should be string
        "options": {}
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data or "code" in data
