import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_lesezeit_rechner_happy_path(client):
    """Test the happy path with valid inputs."""
    response = client.post('/api/minimal-solutions/lesezeit_rechner', json={
        "text": "Dies ist ein einfacher Testtext, der aus ein paar Wörtern besteht, um die Funktionalität des Lesezeit Rechners zu überprüfen.",
        "words_per_minute": 200
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "data" in data
    assert "result" in data["data"]
    assert data["data"]["word_count"] > 0
    assert "minutes" in data["data"]
    assert "seconds" in data["data"]

def test_lesezeit_rechner_empty_input(client):
    """Test with empty payload to verify validation."""
    response = client.post('/api/minimal-solutions/lesezeit_rechner', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "text" in data["details"]

    # Test completely missing JSON body
    response = client.post('/api/minimal-solutions/lesezeit_rechner')
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "BAD_REQUEST"

def test_lesezeit_rechner_invalid_input(client):
    """Test with invalid input values to verify validation rules."""
    response = client.post('/api/minimal-solutions/lesezeit_rechner', json={
        "text": 12345,
        "words_per_minute": -50
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "text" in data["details"]
    assert "words_per_minute" in data["details"]
