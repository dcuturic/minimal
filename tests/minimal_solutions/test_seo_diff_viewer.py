import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_seo_diff_viewer_happy_path(client):
    """Happy-Path Test für SEO Diff Viewer"""
    response = client.post(
        '/api/minimal-solutions/seo_diff_viewer',
        json={
            "topic": "Digital Marketing",
            "target": "Small Businesses"
        }
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["topic"] == "Digital Marketing"
    assert data["data"]["target"] == "Small Businesses"
    assert data["data"]["diff_status"] == "success"

def test_seo_diff_viewer_empty_input(client):
    """Empty-Input Test für SEO Diff Viewer"""
    response = client.post(
        '/api/minimal-solutions/seo_diff_viewer',
        json={}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"

def test_seo_diff_viewer_invalid_input(client):
    """Invalid-Input Test für SEO Diff Viewer"""
    response = client.post(
        '/api/minimal-solutions/seo_diff_viewer',
        json={
            "topic": 12345,  # Erwartet str
            "target": ["not", "a", "string"]  # Erwartet str
        }
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
