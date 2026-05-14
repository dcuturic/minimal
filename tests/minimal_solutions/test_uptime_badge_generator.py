import json
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_uptime_badge_generator_happy_path(client):
    response = client.post(
        '/api/minimal-solutions/uptime_badge_generator',
        data=json.dumps({
            "status": "Operational",
            "uptime_percent": 99.9
        }),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert 'svg' in data['data']
    assert '<svg' in data['data']['svg']

def test_uptime_badge_generator_empty_input(client):
    response = client.post(
        '/api/minimal-solutions/uptime_badge_generator',
        data=json.dumps({}),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['status'] == 'error'
    assert 'status' in data['errors']
    assert 'uptime_percent' in data['errors']

def test_uptime_badge_generator_invalid_input(client):
    response = client.post(
        '/api/minimal-solutions/uptime_badge_generator',
        data=json.dumps({
            "status": "",
            "uptime_percent": 150
        }),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['status'] == 'error'
    assert 'status' in data['errors']
    assert 'uptime_percent' in data['errors']
