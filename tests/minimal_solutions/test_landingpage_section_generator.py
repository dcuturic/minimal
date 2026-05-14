import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_landingpage_section_generator_happy_path(client):
    payload = {
        "section_type": "hero",
        "topic": "SaaS Platform"
    }
    response = client.post('/api/minimal-solutions/landingpage_section_generator', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'result' in data['data']
    assert data['data']['result']['type'] == 'hero'
    assert 'SaaS Platform' in data['data']['result']['headline']

def test_landingpage_section_generator_empty_input(client):
    response = client.post('/api/minimal-solutions/landingpage_section_generator', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'

def test_landingpage_section_generator_invalid_input(client):
    payload = {
        "section_type": "invalid_type",
        "topic": ""
    }
    response = client.post('/api/minimal-solutions/landingpage_section_generator', json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'
    assert 'details' in data['error']
