import pytest
import json
from app.factory import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_seo_formatter_happy_path(client):
    """Test the happy path with valid inputs."""
    response = client.post('/api/minimal-solutions/seo_formatter', json={
        "topic": "Minecraft Server Tutorial",
        "target": "Anfänger",
        "options": {
            "format": "html"
        }
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "formatted_text" in data["data"]
    assert "slug" in data["data"]
    assert "character_count" in data["data"]
    assert "minecraft-server-tutorial" in data["data"]["slug"]

def test_seo_formatter_empty_input(client):
    """Test the endpoint with empty input."""
    response = client.post('/api/minimal-solutions/seo_formatter', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"

def test_seo_formatter_invalid_input(client):
    """Test the endpoint with invalid input types."""
    response = client.post('/api/minimal-solutions/seo_formatter', json={
        "topic": 12345,  # Invalid type, should be string
        "target": "Anfänger"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
