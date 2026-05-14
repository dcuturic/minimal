import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_utm_link_builder_happy_path(client):
    response = client.post('/api/minimal-solutions/utm_link_builder', json={
        "url": "https://example.com/product",
        "source": "google",
        "medium": "cpc",
        "campaign": "spring_sale",
        "term": "running shoes",
        "content": "logolink"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "utm_link" in data["data"]
    utm_link = data["data"]["utm_link"]
    
    assert utm_link.startswith("https://example.com/product?")
    assert "utm_source=google" in utm_link
    assert "utm_medium=cpc" in utm_link
    assert "utm_campaign=spring_sale" in utm_link
    assert "utm_term=running+shoes" in utm_link
    assert "utm_content=logolink" in utm_link

def test_utm_link_builder_empty_input(client):
    response = client.post('/api/minimal-solutions/utm_link_builder', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "url" in data["details"]
    assert "source" in data["details"]
    assert "medium" in data["details"]
    assert "campaign" in data["details"]

def test_utm_link_builder_invalid_input(client):
    response = client.post('/api/minimal-solutions/utm_link_builder', json={
        "url": "not_a_url",
        "source": "google",
        "medium": "cpc",
        "campaign": "spring_sale"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert data["code"] == "VALIDATION_ERROR"
    assert "url" in data["details"]
