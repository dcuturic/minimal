import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_seo_template_builder_happy_path(client):
    """Happy-Path Test für SEO Template Builder"""
    response = client.post(
        '/api/minimal-solutions/seo_template_builder',
        json={
            "topic": "On-Page SEO Best Practices 2024",
            "target": "Content Creators",
            "options": "include_meta_tags"
        }
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["data"]["topic"] == "On-Page SEO Best Practices 2024"
    assert data["data"]["target"] == "Content Creators"
    assert data["data"]["template_status"] == "success"

def test_seo_template_builder_empty_input(client):
    """Empty-Input Test für SEO Template Builder"""
    response = client.post(
        '/api/minimal-solutions/seo_template_builder',
        json={}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"

def test_seo_template_builder_invalid_input(client):
    """Invalid-Input Test für SEO Template Builder"""
    response = client.post(
        '/api/minimal-solutions/seo_template_builder',
        json={
            "topic": 12345,  # Erwartet str
            "target": ["not", "a", "string"]  # Erwartet str
        }
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
