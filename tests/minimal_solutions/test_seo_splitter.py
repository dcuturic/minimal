import pytest
from flask import Flask
from app.responses import ErrorCodes
from minimal_solutions.seo_splitter.seo_splitter_api import api_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_seo_splitter_happy_path(client):
    payload = {
        "topic": "Ein großer Textblock für SEO",
        "target": "Blog-Post-Splitting",
        "options": {"split_by": "paragraphs"}
    }
    response = client.post('/api/minimal-solutions/seo_splitter', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "split_segments" in data["data"]
    assert data["data"]["topic"] == "Ein großer Textblock für SEO"

def test_seo_splitter_empty_input(client):
    response = client.post('/api/minimal-solutions/seo_splitter', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.VALIDATION_ERROR

def test_seo_splitter_invalid_input(client):
    payload = {
        "topic": "A",
        "target": 123
    }
    response = client.post('/api/minimal-solutions/seo_splitter', json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.VALIDATION_ERROR
    assert "topic" in data["error"]["details"]
    assert "target" in data["error"]["details"]
