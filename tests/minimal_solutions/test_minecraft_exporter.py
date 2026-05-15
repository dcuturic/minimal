import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_minecraft_exporter_happy_path(client):
    response = client.post('/api/minimal-solutions/minecraft_exporter', json={
        "input_text": "Sample block data for export.",
        "mode": "schematic",
        "options": ["compress"]
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["input_text"] == "Sample block data for export."
    assert data["data"]["mode"] == "schematic"
    assert data["data"]["options"] == ["compress"]
    assert "export_url" in data["data"]
    assert "message" in data["data"]

def test_minecraft_exporter_empty_input(client):
    response = client.post('/api/minimal-solutions/minecraft_exporter', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "input_text" in data["error"]["details"]
    assert "mode" in data["error"]["details"]

def test_minecraft_exporter_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_exporter', json={
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
