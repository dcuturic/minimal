import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_seo_analyzer_happy_path(client):
    response = client.post('/api/minimal-solutions/seo_analyzer', json={
        "topic": "Ein ausreichend langer Text für SEO",
        "target": "Bloggers",
        "options": ["check_density"]
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "score" in data["data"]
    assert "issues" in data["data"]
    assert "keyword_density" in data["data"]
    assert data["data"]["score"] == 85
    assert data["data"]["keyword_density"] == "2.5%"
    assert len(data["data"]["issues"]) == 0

def test_seo_analyzer_empty_input(client):
    response = client.post('/api/minimal-solutions/seo_analyzer', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "topic" in data["error"]["details"]

def test_seo_analyzer_invalid_input(client):
    response = client.post('/api/minimal-solutions/seo_analyzer', json={
        "topic": "a",
        "target": 123
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "VALIDATION_ERROR" in data["error"]["code"]
    assert "topic" in data["error"]["details"]
    assert "target" in data["error"]["details"]
