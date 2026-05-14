import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hosting_normalizer_happy_path(client):
    response = client.post('/api/minimal-solutions/hosting_normalizer', json={
        "source": "   Hosting-Server-123   ",
        "config": {"remove_spaces": True},
        "mode": "standard"
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['data']['source'] == '   Hosting-Server-123   '
    assert data['data']['mode'] == 'standard'
    assert data['data']['normalized'] is True
    assert data['data']['config']['remove_spaces'] is True

def test_hosting_normalizer_empty_input(client):
    response = client.post('/api/minimal-solutions/hosting_normalizer', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False
    assert data['error']['code'] == 'VALIDATION_ERROR'

def test_hosting_normalizer_invalid_input(client):
    response = client.post('/api/minimal-solutions/hosting_normalizer', json={
        "source": "",  # Too short/empty
        "config": "not_a_dict",
        "mode": "" # Too short/empty
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False
    assert data['error']['code'] == 'VALIDATION_ERROR'
