import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hosting_template_builder_happy_path(client):
    response = client.post('/api/minimal-solutions/hosting_template_builder', json={
        "source": "server-config-template",
        "config": {
            "os": "ubuntu-22.04",
            "disk": "100GB",
            "ram": "16GB"
        },
        "mode": "standard"
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['data']['source'] == 'server-config-template'
    assert data['data']['mode'] == 'standard'
    assert data['data']['template_built'] is True
    assert data['data']['config']['os'] == 'ubuntu-22.04'

def test_hosting_template_builder_empty_input(client):
    response = client.post('/api/minimal-solutions/hosting_template_builder', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False
    assert data['error']['code'] == 'VALIDATION_ERROR'
    assert 'source' in data['error']['details']
    assert 'mode' in data['error']['details']

def test_hosting_template_builder_invalid_input(client):
    response = client.post('/api/minimal-solutions/hosting_template_builder', json={
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
