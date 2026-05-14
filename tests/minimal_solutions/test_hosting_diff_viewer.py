import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hosting_diff_viewer_happy_path(client):
    response = client.post('/api/minimal-solutions/hosting_diff_viewer', json={
        "source": "server-config-v1",
        "config": {
            "target": "server-config-v2",
            "ignore_whitespace": True
        },
        "mode": "side-by-side"
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['data']['source'] == 'server-config-v1'
    assert data['data']['mode'] == 'side-by-side'
    assert data['data']['diff_viewed'] is True
    assert data['data']['config']['target'] == 'server-config-v2'

def test_hosting_diff_viewer_empty_input(client):
    response = client.post('/api/minimal-solutions/hosting_diff_viewer', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False
    assert data['error']['code'] == 'VALIDATION_ERROR'
    assert 'source' in data['error']['details']
    assert 'mode' in data['error']['details']

def test_hosting_diff_viewer_invalid_input(client):
    response = client.post('/api/minimal-solutions/hosting_diff_viewer', json={
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
