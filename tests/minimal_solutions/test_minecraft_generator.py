import pytest
from app.factory import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_minecraft_generator_happy_path(client):
    payload = {
        "input_text": "A small wooden house",
        "mode": "blueprint",
        "options": {
            "biome": "plains"
        }
    }
    response = client.post('/api/minimal-solutions/minecraft_generator', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["input_text"] == "A small wooden house"
    assert data["data"]["mode"] == "blueprint"
    assert data["data"]["options"] == {"biome": "plains"}

def test_minecraft_generator_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_generator', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "input_text" in data["details"]
    assert "mode" in data["details"]

def test_minecraft_generator_invalid_input(client):
    payload = {
        "input_text": 123,
        "mode": ["invalid"],
        "options": "not_a_dict"
    }
    response = client.post('/api/minimal-solutions/minecraft_generator', json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "input_text" in data["details"]
    assert "mode" in data["details"]
    assert "options" in data["details"]
