import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hosting_mapper_happy_path(client):
    response = client.post('/api/minimal-solutions/hosting_mapper', json={
        "source": "server-europe-1",
        "config": {
            "region": "eu-central",
            "provider": "aws",
            "tier": "enterprise"
        },
        "mode": "auto"
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['data']['source'] == 'server-europe-1'
    assert data['data']['mode'] == 'auto'
    assert data['data']['mapped'] is True
    assert data['data']['config']['region'] == 'eu-central'

def test_hosting_mapper_empty_input(client):
    response = client.post('/api/minimal-solutions/hosting_mapper', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False
    assert data['error']['code'] == 'VALIDATION_ERROR'
    assert 'source' in data['error']['details']
    assert 'mode' in data['error']['details']

def test_hosting_mapper_invalid_input(client):
    response = client.post('/api/minimal-solutions/hosting_mapper', json={
        "source": "",  # Empty string invalid
        "config": "not-a-dict", # Invalid type
        "mode": "  " # Blank string invalid
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False
    assert data['error']['code'] == 'VALIDATION_ERROR'
    assert 'source' in data['error']['details']
    assert 'config' in data['error']['details']
    assert 'mode' in data['error']['details']
