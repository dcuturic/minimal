import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_minecraft_server_status_demo_happy_path(client):
    response = client.post(
        '/api/minimal-solutions/minecraft_server_status_demo',
        json={"host": "mc.hypixel.net", "port": 25565}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert "host" in data["data"]
    assert "port" in data["data"]
    assert data["data"]["online"] is True

def test_minecraft_server_status_demo_empty_input(client):
    response = client.post(
        '/api/minimal-solutions/minecraft_server_status_demo',
        json={}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "VALIDATION_ERROR"
    assert "host" in data["error"]["details"]
    assert "port" in data["error"]["details"]

def test_minecraft_server_status_demo_invalid_input(client):
    response = client.post(
        '/api/minimal-solutions/minecraft_server_status_demo',
        json={"host": "mc.hypixel.net", "port": "not-a-port"}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "VALIDATION_ERROR"
    assert "port" in data["error"]["details"]

def test_minecraft_server_status_demo_invalid_json(client):
    response = client.post(
        '/api/minimal-solutions/minecraft_server_status_demo',
        data="invalid-json"
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "BAD_REQUEST"
