import json
import pytest
from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_image_prompt_generator_happy_path(client):
    response = client.post('/api/minimal-solutions/image_prompt_generator', json={
        "subject": "a cute astronaut dog",
        "style": "photorealistic",
        "mood": "adventurous",
        "aspect_ratio": "1:1"
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert 'prompt' in data['data']
    assert 'a cute astronaut dog' in data['data']['prompt']
    assert 'photorealistic' in data['data']['prompt']

def test_image_prompt_generator_empty_input(client):
    response = client.post('/api/minimal-solutions/image_prompt_generator', json={})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['status'] == 'error'
    assert data['error']['code'] == 'VALIDATION_ERROR'
    assert len(data['error']['details']) > 0

def test_image_prompt_generator_invalid_input(client):
    response = client.post('/api/minimal-solutions/image_prompt_generator', json={
        "subject": "",
        "style": 123,
        "mood": "happy",
        "aspect_ratio": ""
    })
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['status'] == 'error'
    assert data['error']['code'] == 'VALIDATION_ERROR'
    details = data['error']['details']
    fields = [err['field'] for err in details]
    assert 'subject' in fields
    assert 'style' in fields
    assert 'aspect_ratio' in fields
