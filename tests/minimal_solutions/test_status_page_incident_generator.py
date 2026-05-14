import pytest
from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_status_page_incident_generator_happy_path(client):
    response = client.post('/api/minimal-solutions/status_page_incident_generator', json={
        "service": "Database",
        "incident_type": "Degraded Performance",
        "status": "investigating",
        "message": "We are investigating the performance degradation of our main database."
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'data' in data

def test_status_page_incident_generator_empty_input(client):
    response = client.post('/api/minimal-solutions/status_page_incident_generator', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'

def test_status_page_incident_generator_invalid_input(client):
    response = client.post('/api/minimal-solutions/status_page_incident_generator', json={
        "service": 123,
        "incident_type": "Degraded Performance",
        "status": "investigating",
        "message": "We are investigating the performance degradation of our main database."
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'
