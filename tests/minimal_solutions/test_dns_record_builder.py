import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dns_record_builder_happy_path(client):
    response = client.post(
        '/api/minimal-solutions/dns_record_builder',
        json={"type": "A", "name": "example.com", "value": "192.168.1.1", "ttl": 3600}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert data["data"]["type"] == "A"
    assert data["data"]["name"] == "example.com"
    assert data["data"]["value"] == "192.168.1.1"
    assert data["data"]["ttl"] == 3600
    assert data["data"]["record"] == "example.com\t3600\tIN\tA\t192.168.1.1"

def test_dns_record_builder_txt_record(client):
    response = client.post(
        '/api/minimal-solutions/dns_record_builder',
        json={"type": "TXT", "name": "example.com", "value": "v=spf1 include:_spf.google.com ~all", "ttl": 300}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert data["data"]["type"] == "TXT"
    assert data["data"]["value"] == '"v=spf1 include:_spf.google.com ~all"'
    assert data["data"]["record"] == 'example.com\t300\tIN\tTXT\t"v=spf1 include:_spf.google.com ~all"'

def test_dns_record_builder_empty_input(client):
    response = client.post(
        '/api/minimal-solutions/dns_record_builder',
        json={}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "VALIDATION_ERROR"
    assert "type" in data["error"]["details"]
    assert "name" in data["error"]["details"]
    assert "value" in data["error"]["details"]
    assert "ttl" in data["error"]["details"]

def test_dns_record_builder_invalid_input(client):
    response = client.post(
        '/api/minimal-solutions/dns_record_builder',
        json={"type": "INVALID", "name": "", "value": "", "ttl": "invalid"}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "VALIDATION_ERROR"
    assert "type" in data["error"]["details"]
    assert "name" in data["error"]["details"]
    assert "value" in data["error"]["details"]
    assert "ttl" in data["error"]["details"]

def test_dns_record_builder_invalid_json(client):
    response = client.post(
        '/api/minimal-solutions/dns_record_builder',
        data="invalid-json"
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "BAD_REQUEST"
