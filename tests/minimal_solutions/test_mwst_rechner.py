import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_mwst_rechner_happy_path(client):
    response = client.post('/api/minimal-solutions/mwst_rechner', json={
        "amount": "100.00",
        "mode": "net_to_gross",
        "vat_rate": "19"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["net_amount"] == 100.0
    assert data["data"]["vat_amount"] == 19.0
    assert data["data"]["gross_amount"] == 119.0

def test_mwst_rechner_empty_input(client):
    response = client.post('/api/minimal-solutions/mwst_rechner', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == "VALIDATION_ERROR"
    assert "amount" in data["error"]["details"]
    assert "mode" in data["error"]["details"]
    assert "vat_rate" in data["error"]["details"]

def test_mwst_rechner_invalid_input(client):
    response = client.post('/api/minimal-solutions/mwst_rechner', json={
        "amount": "abc",
        "mode": "invalid_mode",
        "vat_rate": "-5"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == "VALIDATION_ERROR"
    assert "amount" in data["error"]["details"]
    assert "mode" in data["error"]["details"]
    assert "vat_rate" in data["error"]["details"]
