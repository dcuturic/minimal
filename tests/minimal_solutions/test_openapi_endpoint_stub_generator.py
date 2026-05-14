import pytest
import json
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_openapi_endpoint_stub_generator_happy_path(client):
    """Test Happy-Path: Gültige Daten generieren einen OpenAPI-Stub."""
    response = client.post('/api/minimal-solutions/openapi_endpoint_stub_generator', json={
        "path": "/api/users",
        "method": "POST",
        "summary": "Create a new user",
        "request_fields": "username, email, password"
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "data" in data
    assert "openapi_stub" in data["data"]
    assert "yaml" in data["data"]
    
    stub_dict = json.loads(data["data"]["openapi_stub"])
    assert "/api/users" in stub_dict
    assert "post" in stub_dict["/api/users"]
    assert stub_dict["/api/users"]["post"]["summary"] == "Create a new user"

def test_openapi_endpoint_stub_generator_empty_input(client):
    """Test Empty-Input: Keine Daten generieren einen Validierungsfehler."""
    response = client.post('/api/minimal-solutions/openapi_endpoint_stub_generator', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "details" in data
    assert "path" in data["details"]
    assert "method" in data["details"]
    assert "summary" in data["details"]

def test_openapi_endpoint_stub_generator_invalid_input(client):
    """Test Invalid-Input: Ungültige Methode führt zu Fehler."""
    response = client.post('/api/minimal-solutions/openapi_endpoint_stub_generator', json={
        "path": "/api/users",
        "method": "INVALID_METHOD",
        "summary": "Summary",
        "request_fields": ""
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "details" in data
    assert "method" in data["details"]
