import pytest
from flask import Flask
from app.responses import ErrorCodes
from minimal_solutions.seo_checker.seo_checker_api import api_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_seo_checker_happy_path(client):
    payload = {
        "topic": "Python Web Scraping",
        "target": "Blog Post",
        "options": {
            "strict_mode": True
        }
    }
    response = client.post('/api/minimal-solutions/seo_checker', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "score" in data["data"]
    assert data["data"]["score"] == 85
    assert data["data"]["details"]["topic_used"] == "Python Web Scraping"
    assert data["data"]["details"]["target_used"] == "Blog Post"

def test_seo_checker_empty_input(client):
    response = client.post('/api/minimal-solutions/seo_checker', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.VALIDATION_ERROR

def test_seo_checker_invalid_input(client):
    payload = {
        "topic": "A",
        "target": 123
    }
    response = client.post('/api/minimal-solutions/seo_checker', json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.VALIDATION_ERROR
    assert "topic" in data["error"]["details"]
    assert "target" in data["error"]["details"]
