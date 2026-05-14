import json

def test_iframe_preview_url_builder_happy_path(client):
    response = client.post('/api/minimal-solutions/iframe_preview_url_builder', json={
        "page": "dashboard",
        "component": "user-profile",
        "mode": "dark"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "preview_url" in data["data"]
    assert "iframe_code" in data["data"]
    assert "page=dashboard" in data["data"]["preview_url"]
    assert "component=user-profile" in data["data"]["preview_url"]
    assert "mode=dark" in data["data"]["preview_url"]
    assert '<iframe src="/preview?page=dashboard&amp;component=user-profile&amp;mode=dark"' in data["data"]["iframe_code"] or "preview?" in data["data"]["iframe_code"]

def test_iframe_preview_url_builder_empty_input(client):
    response = client.post('/api/minimal-solutions/iframe_preview_url_builder', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "details" in data
    assert "page" in data["details"]
    assert "component" in data["details"]

def test_iframe_preview_url_builder_invalid_input(client):
    response = client.post('/api/minimal-solutions/iframe_preview_url_builder', json={
        "page": "",
        "component": 123
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "details" in data
    assert "page" in data["details"]
    assert "component" in data["details"]
