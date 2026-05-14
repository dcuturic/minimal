import json
import pytest
from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_pricing_table_generator_happy_path(client):
    response = client.post('/api/minimal-solutions/pricing_table_generator', json={
        "plans": [
            {
                "name": "Basic",
                "price": "9.99",
                "currency": "€",
                "period": "/month",
                "features": ["Feature 1", "Feature 2"],
                "is_popular": False,
                "button_text": "Buy Basic"
            },
            {
                "name": "Pro",
                "price": "19.99",
                "currency": "€",
                "period": "/month",
                "features": ["Feature 1", "Feature 2", "Feature 3"],
                "is_popular": True,
                "button_text": "Buy Pro"
            }
        ]
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert 'result' in data['data']
    assert len(data['data']['result']) == 2
    assert data['data']['result'][0]['name'] == 'Basic'
    assert data['data']['result'][1]['is_popular'] is True

def test_pricing_table_generator_empty_input(client):
    response = client.post('/api/minimal-solutions/pricing_table_generator', json={})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['status'] == 'error'
    assert 'plans' in data['details']

def test_pricing_table_generator_invalid_input(client):
    response = client.post('/api/minimal-solutions/pricing_table_generator', json={
        "plans": [
            {
                # Missing name and price
                "features": ["Feature 1"]
            }
        ]
    })
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['status'] == 'error'
    assert 'plans[0].name' in data['details']
    assert 'plans[0].price' in data['details']
