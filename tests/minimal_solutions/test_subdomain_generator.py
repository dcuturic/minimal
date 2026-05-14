import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_subdomain_generator_happy_path(client):
    response = client.post(
        '/api/minimal-solutions/subdomain_generator',
        json={"name": "my cool api", "base_domain": "crafthoster.com"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert "subdomains" in data["data"]
    assert "name" in data["data"]
    assert "base_domain" in data["data"]
    assert len(data["data"]["subdomains"]) == 6
    assert "my-cool-api.crafthoster.com" in data["data"]["subdomains"]

def test_subdomain_generator_empty_input(client):
    response = client.post(
        '/api/minimal-solutions/subdomain_generator',
        json={}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "VALIDATION_ERROR"
    assert "name" in data["error"]["details"]
    assert "base_domain" in data["error"]["details"]

def test_subdomain_generator_invalid_input(client):
    response = client.post(
        '/api/minimal-solutions/subdomain_generator',
        json={"name": "   ", "base_domain": "   "}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "VALIDATION_ERROR"
    assert "name" in data["error"]["details"]
    assert "base_domain" in data["error"]["details"]

def test_subdomain_generator_invalid_json(client):
    response = client.post(
        '/api/minimal-solutions/subdomain_generator',
        data="invalid-json"
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "BAD_REQUEST"
