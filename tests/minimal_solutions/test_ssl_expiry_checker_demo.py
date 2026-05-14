import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ssl_expiry_checker_demo_happy_path(client):
    response = client.post(
        '/api/minimal-solutions/ssl_expiry_checker_demo',
        json={"domain": "google.com"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert data["data"]["domain"] == "google.com"
    # we don't know the exact days remaining or valid flag, but we check if they exist
    assert "is_valid" in data["data"]
    assert "days_remaining" in data["data"]
    assert "expiry_date" in data["data"]

def test_ssl_expiry_checker_demo_empty_input(client):
    response = client.post(
        '/api/minimal-solutions/ssl_expiry_checker_demo',
        json={}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "VALIDATION_ERROR"
    assert "domain" in data["error"]["details"]

def test_ssl_expiry_checker_demo_invalid_input(client):
    response = client.post(
        '/api/minimal-solutions/ssl_expiry_checker_demo',
        json={"domain": "invalid domain with spaces"}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "VALIDATION_ERROR"
    assert "domain" in data["error"]["details"]

def test_ssl_expiry_checker_demo_invalid_json(client):
    response = client.post(
        '/api/minimal-solutions/ssl_expiry_checker_demo',
        data="invalid-json"
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "BAD_REQUEST"
