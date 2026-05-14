import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_lorem_ipsum_generator_happy_path(client):
    """Test the happy path with valid inputs for different modes."""
    # Test paragraphs
    response = client.post('/api/minimal-solutions/lorem_ipsum_generator', json={
        "mode": "paragraphs",
        "count": 3
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "data" in data
    assert "text" in data["data"]
    assert len(data["data"]["text"]) > 0
    assert "\n\n" in data["data"]["text"]  # paragraphs are separated by \n\n

    # Test words
    response = client.post('/api/minimal-solutions/lorem_ipsum_generator', json={
        "mode": "words",
        "count": 10
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert len(data["data"]["text"].split(' ')) >= 10

def test_lorem_ipsum_generator_empty_input(client):
    """Test with empty payload to verify validation."""
    response = client.post('/api/minimal-solutions/lorem_ipsum_generator', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "mode" in data["details"]
    assert "count" in data["details"]

    # Test completely missing JSON body
    response = client.post('/api/minimal-solutions/lorem_ipsum_generator')
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "BAD_REQUEST"

def test_lorem_ipsum_generator_invalid_input(client):
    """Test with invalid input values to verify validation rules."""
    response = client.post('/api/minimal-solutions/lorem_ipsum_generator', json={
        "mode": "unsupported_mode",
        "count": -5
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "mode" in data["details"]
    assert "count" in data["details"]

    # Test invalid data types
    response = client.post('/api/minimal-solutions/lorem_ipsum_generator', json={
        "mode": 123,
        "count": "5"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "mode" in data["details"]
    assert "count" in data["details"]
