import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_seo_cleaner_happy_path(client):
    response = client.post('/api/minimal-solutions/seo_cleaner', json={
        "topic": "Gaming Laptops 2024",
        "target": "Tech Enthusiasts",
        "options": {
            "remove_duplicates": True,
            "fix_typos": True
        }
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert data['data']['topic'] == 'Gaming Laptops 2024'
    assert data['data']['target'] == 'Tech Enthusiasts'
    assert data['data']['clean_status'] == 'success'
    assert data['data']['clean_items'] == 5

def test_seo_cleaner_empty_input(client):
    response = client.post('/api/minimal-solutions/seo_cleaner', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'
    assert data['code'] == 'VALIDATION_ERROR'

def test_seo_cleaner_invalid_input(client):
    response = client.post('/api/minimal-solutions/seo_cleaner', json={
        "topic": "x",  # Too short (min 2)
        "target": "t", # Too short (min 2)
        "options": "not_a_dict"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'
    assert data['code'] == 'VALIDATION_ERROR'
