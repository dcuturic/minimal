import pytest
from flask import Flask
from app.responses import ErrorCodes
from minimal_solutions.seo_merger.seo_merger_api import api_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_seo_merger_happy_path(client):
    payload = {
        "topic": "Keyword-Set A, Keyword-Set B",
        "target": "Landingpage Integration",
        "options": {"merge_strategy": "deduplicate"}
    }
    response = client.post('/api/minimal-solutions/seo_merger', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["topic"] == "Keyword-Set A, Keyword-Set B"
    assert data["data"]["target"] == "Landingpage Integration"

def test_seo_merger_empty_input(client):
    response = client.post('/api/minimal-solutions/seo_merger', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.VALIDATION_ERROR

def test_seo_merger_invalid_input(client):
    payload = {
        "topic": "A", # Too short
        "target": 123 # Invalid type
    }
    response = client.post('/api/minimal-solutions/seo_merger', json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.VALIDATION_ERROR
    assert "topic" in data["error"]["details"]
    assert "target" in data["error"]["details"]
