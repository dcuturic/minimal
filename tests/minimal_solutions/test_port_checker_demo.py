import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_port_checker_happy_path(client):
    response = client.post('/api/minimal-solutions/port_checker_demo', json={
        "host": "127.0.0.1",
        "port": 80
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'is_open' in data['data']
    assert data['data']['host'] == '127.0.0.1'
    assert data['data']['port'] == 80

def test_port_checker_empty_input(client):
    response = client.post('/api/minimal-solutions/port_checker_demo', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'
    assert data['code'] == 'VALIDATION_ERROR'
    assert 'host' in data['details']
    assert 'port' in data['details']

def test_port_checker_invalid_input(client):
    response = client.post('/api/minimal-solutions/port_checker_demo', json={
        "host": "   ",
        "port": 70000
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'
    assert data['code'] == 'VALIDATION_ERROR'
    assert 'host' in data['details']
    assert 'port' in data['details']
