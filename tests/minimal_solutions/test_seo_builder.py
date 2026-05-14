import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_seo_builder_happy_path(client):
    response = client.post('/api/minimal-solutions/seo_builder', json={
        "topic": "Suchmaschinenoptimierung",
        "target": "Anfänger",
        "options": {"uppercase_title": True}
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "result" in data["data"]
    assert "TITLE" in data["data"]["result"]["title"]
    assert data["data"]["meta"]["topic"] == "Suchmaschinenoptimierung"

def test_seo_builder_empty_input(client):
    response = client.post('/api/minimal-solutions/seo_builder', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "topic" in data["error"]["details"]
    assert "target" in data["error"]["details"]

def test_seo_builder_invalid_input(client):
    response = client.post('/api/minimal-solutions/seo_builder', json={
        "topic": "ab",
        "target": "c"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "topic" in data["error"]["details"]
    assert "target" in data["error"]["details"]
