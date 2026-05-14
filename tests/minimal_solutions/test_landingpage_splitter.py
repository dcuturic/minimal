import pytest
from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_landingpage_splitter_happy_path(client):
    response = client.post('/api/minimal-solutions/landingpage_splitter', json={
        "topic": "SaaS Platform",
        "target": "Startups",
        "options": "a_b_testing"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert "split_result" in data["data"]
    assert "SaaS Platform" in data["data"]["split_result"]

def test_landingpage_splitter_empty_input(client):
    response = client.post('/api/minimal-solutions/landingpage_splitter', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert "Das Feld 'topic' ist erforderlich" in data["error"]["details"][0] or "Das Feld 'topic' fehlt" in data["error"]["details"][0]

def test_landingpage_splitter_invalid_input(client):
    response = client.post('/api/minimal-solutions/landingpage_splitter', data="not a json")
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "BAD_REQUEST"
