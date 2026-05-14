import json

def test_random_name_generator_happy_path(client):
    """Testet den Erfolgsfall mit gültigen Eingaben."""
    response = client.post('/api/minimal-solutions/random_name_generator', json={
        "category": "project",
        "count": 5
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "names" in data["data"]
    assert isinstance(data["data"]["names"], list)
    assert len(data["data"]["names"]) == 5
    for name in data["data"]["names"]:
        assert isinstance(name, str)

def test_random_name_generator_empty_input(client):
    """Testet das Verhalten bei leerem JSON-Body."""
    response = client.post('/api/minimal-solutions/random_name_generator', json={})
    
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "category" in data["details"]
    assert "count" in data["details"]

def test_random_name_generator_invalid_input(client):
    """Testet das Verhalten bei ungültigen Eingabedaten."""
    response = client.post('/api/minimal-solutions/random_name_generator', json={
        "category": "unknown_category",
        "count": 200
    })
    
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "category" in data["details"]
    assert "count" in data["details"]

    # Test count < 1
    response = client.post('/api/minimal-solutions/random_name_generator', json={
        "category": "project",
        "count": 0
    })
    assert response.status_code == 400
    
    # Test invalid types
    response = client.post('/api/minimal-solutions/random_name_generator', json={
        "category": 123,
        "count": "5"
    })
    assert response.status_code == 400
