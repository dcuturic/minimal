import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_word_replacer_happy_path(client):
    """Test the happy path with valid inputs."""
    # Case sensitive replace
    response = client.post('/api/minimal-solutions/word_replacer', json={
        "text": "Hello World. This is a beautiful World.",
        "search": "World",
        "replace": "Universe",
        "case_sensitive": True
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "data" in data
    assert "result" in data["data"]
    assert data["data"]["result"] == "Hello Universe. This is a beautiful Universe."

    # Case insensitive replace
    response = client.post('/api/minimal-solutions/word_replacer', json={
        "text": "hello world. This is a beautiful WoRlD.",
        "search": "world",
        "replace": "Universe",
        "case_sensitive": False
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["result"] == "hello Universe. This is a beautiful Universe."

def test_word_replacer_empty_input(client):
    """Test with empty payload to verify validation."""
    response = client.post('/api/minimal-solutions/word_replacer', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "text" in data["details"]
    assert "search" in data["details"]
    assert "replace" in data["details"]

    # Test completely missing JSON body
    response = client.post('/api/minimal-solutions/word_replacer')
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "BAD_REQUEST"

def test_word_replacer_invalid_input(client):
    """Test with invalid input values to verify validation rules."""
    response = client.post('/api/minimal-solutions/word_replacer', json={
        "text": 123,
        "search": "",
        "replace": False,
        "case_sensitive": "invalid_boolean"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "text" in data["details"]
    assert "search" in data["details"]
    assert "replace" in data["details"]
    assert "case_sensitive" in data["details"]
