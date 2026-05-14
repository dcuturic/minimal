import json

def test_theme_token_editor_happy_path(client):
    response = client.post(
        '/api/minimal-solutions/theme_token_editor_demo',
        json={
            "tokens": {
                "colors": {
                    "primary": "#3b82f6"
                }
            }
        }
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "tokens" in data["data"]
    assert data["data"]["tokens"]["colors"]["primary"] == "#3b82f6"

def test_theme_token_editor_empty_input(client):
    response = client.post(
        '/api/minimal-solutions/theme_token_editor_demo',
        json={}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert any(e["field"] == "tokens" for e in data["details"])

def test_theme_token_editor_invalid_input(client):
    response = client.post(
        '/api/minimal-solutions/theme_token_editor_demo',
        json={
            "tokens": "invalid_string"
        }
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert any(e["field"] == "tokens" for e in data["details"])
