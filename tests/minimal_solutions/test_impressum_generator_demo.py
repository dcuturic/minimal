import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_impressum_generator_demo_happy_path(client):
    response = client.post('/api/minimal-solutions/impressum_generator_demo', json={
        "company": "CraftHoster GmbH",
        "address": "Musterstraße 1, 12345 Musterstadt",
        "email": "kontakt@crafthoster.de",
        "phone": "+49 123 4567890",
        "representative": "Max Mustermann"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "impressum" in data["data"]
    assert "CraftHoster GmbH" in data["data"]["impressum"]

def test_impressum_generator_demo_empty_input(client):
    response = client.post('/api/minimal-solutions/impressum_generator_demo', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "Validierungsfehler" in data["message"]
    assert "details" in data
    assert len(data["details"]) > 0

def test_impressum_generator_demo_invalid_input(client):
    response = client.post('/api/minimal-solutions/impressum_generator_demo', json={
        "company": "",
        "address": 123,
        "email": "kontakt@crafthoster.de",
        "phone": "+49 123 4567890",
        "representative": "Max Mustermann"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "Validierungsfehler" in data["message"]
