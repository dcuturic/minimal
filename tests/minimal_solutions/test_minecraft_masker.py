import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_minecraft_masker_happy_path(client):
    response = client.post('/api/minimal-solutions/minecraft_masker', json={
        "input_text": "Server IP is 10.0.0.1",
        "mode": "mask_log",
        "options": ["hide_ips", "hide_usernames"]
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["input_text"] == "Server IP is 10.0.0.1"
    assert data["data"]["mode"] == "mask_log"
    assert data["data"]["options"] == ["hide_ips", "hide_usernames"]
    assert "message" in data["data"]

def test_minecraft_masker_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_masker', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "input_text" in data["error"]["details"]
    assert "mode" in data["error"]["details"]

def test_minecraft_masker_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_masker', json={
        "input_text": 123,
        "mode": 456,
        "options": "not_a_list"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "input_text" in data["error"]["details"]
    assert "mode" in data["error"]["details"]
    assert "options" in data["error"]["details"]
