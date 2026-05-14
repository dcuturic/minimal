import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_changelog_generator_happy_path(client):
    response = client.post('/api/minimal-solutions/changelog_generator', json={
        "version": "1.0.0",
        "date": "2023-10-27",
        "changes": "Added new feature\nFixed a bug"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert "## [1.0.0] - 2023-10-27" in data["data"]["result"]
    assert "- Added new feature" in data["data"]["result"]
    assert "- Fixed a bug" in data["data"]["result"]

def test_changelog_generator_empty_input(client):
    response = client.post('/api/minimal-solutions/changelog_generator', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert "VALIDATION_ERROR" in data["error"]["code"]

def test_changelog_generator_invalid_input(client):
    response = client.post('/api/minimal-solutions/changelog_generator', json={
        "version": "",
        "date": "",
        "changes": []
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert "VALIDATION_ERROR" in data["error"]["code"]
