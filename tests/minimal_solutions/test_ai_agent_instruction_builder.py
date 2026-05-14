import json
import pytest
from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ai_agent_instruction_builder_happy_path(client):
    response = client.post('/api/minimal-solutions/ai_agent_instruction_builder', json={
        "agent_name": "SupportBot",
        "purpose": "Answer customer questions.",
        "tools": "- SearchDB\n- SendEmail",
        "constraints": "- Be polite\n- Do not lie"
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert 'result' in data['data']
    assert 'SupportBot' in data['data']['result']
    assert 'Answer customer questions' in data['data']['result']
    assert 'SearchDB' in data['data']['result']
    assert 'Be polite' in data['data']['result']

def test_ai_agent_instruction_builder_empty_input(client):
    response = client.post('/api/minimal-solutions/ai_agent_instruction_builder', json={})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['status'] == 'error'
    assert data['error']['code'] == 'VALIDATION_ERROR'
    assert 'agent_name' in data['error']['details']
    assert 'purpose' in data['error']['details']

def test_ai_agent_instruction_builder_invalid_input(client):
    response = client.post('/api/minimal-solutions/ai_agent_instruction_builder', json={
        "agent_name": "",
        "purpose": "",
        "tools": 123,
        "constraints": 456
    })
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['status'] == 'error'
    assert data['error']['code'] == 'VALIDATION_ERROR'
    details = data['error']['details']
    assert 'agent_name' in details
    assert 'purpose' in details
    assert 'tools' in details
    assert 'constraints' in details
