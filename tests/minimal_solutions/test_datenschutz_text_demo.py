import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_datenschutz_text_demo_happy_path(client):
    response = client.post('/api/minimal-solutions/datenschutz_text_demo', json={
        "uses_cookies": True,
        "uses_analytics": False,
        "uses_contact_form": True,
        "hosting_provider": "CraftHoster GmbH"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "result" in data["data"]
    assert "CraftHoster GmbH" in data["data"]["result"]

def test_datenschutz_text_demo_empty_input(client):
    response = client.post('/api/minimal-solutions/datenschutz_text_demo', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "Validierungsfehler" in data["message"]
    assert "details" in data
    assert len(data["details"]) > 0

def test_datenschutz_text_demo_invalid_input(client):
    response = client.post('/api/minimal-solutions/datenschutz_text_demo', json={
        "uses_cookies": "yes",
        "uses_analytics": False,
        "uses_contact_form": True,
        "hosting_provider": ""
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "Validierungsfehler" in data["message"]
