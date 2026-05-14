import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hosting_cleaner_happy_path(client):
    response = client.post('/api/minimal-solutions/hosting_cleaner', json={
        "source": "server1.example.com",
        "config": {"delete_temp_files": True},
        "mode": "aggressive"
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert data['data']['source'] == 'server1.example.com'
    assert data['data']['mode'] == 'aggressive'
    assert data['data']['cleaned'] is True
    assert data['data']['config']['delete_temp_files'] is True

def test_hosting_cleaner_empty_input(client):
    response = client.post('/api/minimal-solutions/hosting_cleaner', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'
    assert data['code'] == 'VALIDATION_ERROR'

def test_hosting_cleaner_invalid_input(client):
    response = client.post('/api/minimal-solutions/hosting_cleaner', json={
        "source": "",  # Too short/empty
        "config": "not_a_dict",
        "mode": "" # Too short/empty
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'
    assert data['code'] == 'VALIDATION_ERROR'
