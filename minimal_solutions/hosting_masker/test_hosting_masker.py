import pytest
from app import create_app
from minimal_solutions.hosting_masker.api_hosting_masker import api_bp

@pytest.fixture
def client():
    app = create_app()
    app.register_blueprint(api_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hosting_masker_happy_path(client):
    response = client.post('/api/minimal-solutions/hosting_masker', json={
        "source": "192.168.1.100",
        "config": {
            "mask_pattern": "***.***.*.***",
            "keep_last": 1
        },
        "mode": "IP-Address"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["source"] == "192.168.1.100"
    assert data["data"]["mode"] == "IP-Address"
    assert data["data"]["masked"] is True

def test_hosting_masker_empty_input(client):
    response = client.post('/api/minimal-solutions/hosting_masker', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "source" in data["details"]
    assert "mode" in data["details"]

def test_hosting_masker_invalid_input(client):
    response = client.post('/api/minimal-solutions/hosting_masker', json={
        "source": "",
        "config": "not-a-dict",
        "mode": ""
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "source" in data["details"]
    assert "config" in data["details"]
    assert "mode" in data["details"]

def test_hosting_masker_no_json(client):
    response = client.post('/api/minimal-solutions/hosting_masker', data="not json")
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["message"] == "Request must be JSON"
