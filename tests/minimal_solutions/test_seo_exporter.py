import pytest
from flask import Flask
from app.responses import ErrorCodes
from minimal_solutions.seo_exporter.seo_exporter_api import api_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_seo_exporter_happy_path(client):
    payload = {
        "topic": "Python Web Scraping",
        "target": "Blog Post",
        "options": ["Include Metadata", "Export as CSV"]
    }
    response = client.post('/api/minimal-solutions/seo_exporter', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "export_url" in data["data"]
    assert data["data"]["topic"] == "Python Web Scraping"
    assert data["data"]["target"] == "Blog Post"

def test_seo_exporter_empty_input(client):
    response = client.post('/api/minimal-solutions/seo_exporter', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.VALIDATION_ERROR

def test_seo_exporter_invalid_input(client):
    payload = {
        "topic": "A",
        "target": 123
    }
    response = client.post('/api/minimal-solutions/seo_exporter', json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.VALIDATION_ERROR
    assert "topic" in data["error"]["details"]
    assert "target" in data["error"]["details"]
