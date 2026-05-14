import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_seo_normalizer_happy_path(client):
    response = client.post('/api/minimal-solutions/seo_normalizer', json={
        "topic": "Beispiel Thema",
        "target": "Zielpublikum",
        "options": {
            "normalization_level": "high",
            "include_meta": True
        }
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert data['data']['topic'] == 'Beispiel Thema'
    assert data['data']['target'] == 'Zielpublikum'
    assert data['data']['normalized_status'] == 'success'
    assert data['data']['normalized_items'] == 5

def test_seo_normalizer_empty_input(client):
    response = client.post('/api/minimal-solutions/seo_normalizer', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'
    assert data['error']['code'] == 'VALIDATION_ERROR'

def test_seo_normalizer_invalid_input(client):
    response = client.post('/api/minimal-solutions/seo_normalizer', json={
        "topic": 123,  # Invalid type, should be str
        "target": ["Zielpublikum"], # Invalid type, should be str
        "options": "not_a_dict"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'
    assert data['error']['code'] == 'VALIDATION_ERROR'
