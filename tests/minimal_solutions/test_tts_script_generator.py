import pytest
from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_tts_script_generator_happy_path(client):
    response = client.post('/api/minimal-solutions/tts_script_generator', json={
        "topic": "Die Entstehung von Schwarzen Löchern",
        "voice_style": "Dramatisch",
        "duration": "1 Minute"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "script" in data["data"]
    assert "Schwarzen" in data["data"]["script"]

def test_tts_script_generator_empty_input(client):
    response = client.post('/api/minimal-solutions/tts_script_generator', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == "VALIDATION_ERROR"
    
    # Check that errors for fields are present
    details = data["error"]["details"]
    assert any(error["field"] == "topic" for error in details)
    assert any(error["field"] == "voice_style" for error in details)
    assert any(error["field"] == "duration" for error in details)

def test_tts_script_generator_invalid_input(client):
    response = client.post('/api/minimal-solutions/tts_script_generator', json={
        "topic": "   ",
        "voice_style": 123,
        "duration": ""
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == "VALIDATION_ERROR"
    
    details = data["error"]["details"]
    assert any(error["field"] == "topic" for error in details)
    assert any(error["field"] == "voice_style" for error in details)
    assert any(error["field"] == "duration" for error in details)
