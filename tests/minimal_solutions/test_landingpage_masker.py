import pytest
from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_landingpage_masker_happy_path(client):
    response = client.post('/api/minimal-solutions/landingpage_masker', json={
        "topic": "Sicherheit",
        "target": "Administratoren",
        "options": "strikte_maskierung"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert "mask_result" in data["data"]
    assert "Sicherheit" in data["data"]["mask_result"]

def test_landingpage_masker_empty_input(client):
    response = client.post('/api/minimal-solutions/landingpage_masker', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert "Das Feld 'topic' ist erforderlich" in data["error"]["details"][0]

def test_landingpage_masker_invalid_input(client):
    response = client.post('/api/minimal-solutions/landingpage_masker', data="not a json")
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"]["code"] == "BAD_REQUEST"
