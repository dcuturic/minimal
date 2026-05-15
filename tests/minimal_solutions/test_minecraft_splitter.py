import pytest
from app import create_app
from flask import json

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

def test_minecraft_splitter_success(client):
    response = client.post('/api/minimal-solutions/minecraft_splitter', json={
        "input_text": "Text to split",
        "mode": "basic",
        "options": {"split_character": " "}
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "success"
    assert "data" in data

def test_minecraft_splitter_invalid_input(client):
    response = client.post('/api/minimal-solutions/minecraft_splitter', json={
        "input_text": "",
        "mode": "basic"
    })
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["status"] == "error"

def test_minecraft_splitter_missing_fields(client):
    response = client.post('/api/minimal-solutions/minecraft_splitter', json={})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["status"] == "error"
