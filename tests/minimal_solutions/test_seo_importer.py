import pytest
from flask import Flask
from app.responses import ErrorCodes
from minimal_solutions.seo_importer.seo_importer_api import api_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_seo_importer_happy_path(client):
    payload = {
        "topic": "Content Strategy",
        "target": "Landing Page",
        "options": ["overwrite_existing"]
    }
    response = client.post('/api/minimal-solutions/seo_importer', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "imported_items" in data["data"]
    assert data["data"]["topic"] == "Content Strategy"
    assert data["data"]["import_status"] == "success"

def test_seo_importer_empty_input(client):
    response = client.post('/api/minimal-solutions/seo_importer', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.VALIDATION_ERROR

def test_seo_importer_invalid_input(client):
    payload = {
        "topic": "A",
        "target": 123
    }
    response = client.post('/api/minimal-solutions/seo_importer', json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.VALIDATION_ERROR
    assert "topic" in data["error"]["details"]
    assert "target" in data["error"]["details"]
