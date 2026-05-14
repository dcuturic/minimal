import json
import pytest
from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_prompt_template_builder_happy_path(client):
    response = client.post('/api/minimal-solutions/prompt_template_builder', json={
        "goal": "Write a blog post about AI.",
        "variables": "- Topic: AI\n- Audience: Beginners",
        "constraints": "- Keep it under 500 words\n- Use a friendly tone"
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert 'result' in data['data']
    assert 'Write a blog post about AI.' in data['data']['result']
    assert 'Topic: AI' in data['data']['result']
    assert 'Keep it under 500 words' in data['data']['result']

def test_prompt_template_builder_empty_input(client):
    response = client.post('/api/minimal-solutions/prompt_template_builder', json={})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['status'] == 'error'
    assert data['error']['code'] == 'VALIDATION_ERROR'
    assert 'goal' in data['error']['details']

def test_prompt_template_builder_invalid_input(client):
    response = client.post('/api/minimal-solutions/prompt_template_builder', json={
        "goal": "",
        "variables": 123,
        "constraints": 456
    })
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['status'] == 'error'
    assert data['error']['code'] == 'VALIDATION_ERROR'
    details = data['error']['details']
    assert 'goal' in details
    assert 'variables' in details
    assert 'constraints' in details
