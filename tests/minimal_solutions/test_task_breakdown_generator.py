import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_task_breakdown_generator_happy_path(client):
    response = client.post('/api/minimal-solutions/task_breakdown_generator', json={
        "task_text": "Implement OAuth2 Authentication",
        "depth": 2
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "data" in data
    assert "tickets" in data["data"]
    assert isinstance(data["data"]["tickets"], list)

def test_task_breakdown_generator_empty_input(client):
    response = client.post('/api/minimal-solutions/task_breakdown_generator', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "task_text" in data["errors"]

def test_task_breakdown_generator_invalid_input(client):
    response = client.post('/api/minimal-solutions/task_breakdown_generator', json={
        "task_text": "Test Task",
        "depth": 4
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "depth" in data["errors"]
