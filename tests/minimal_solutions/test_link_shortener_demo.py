import pytest

def test_link_shortener_demo_happy_path(client):
    """Testet den Erfolgsfall mit allen Eingabefeldern."""
    response = client.post(
        '/api/minimal-solutions/link_shortener_demo',
        json={
            'long_url': 'https://crafthoster.de/promo-2026',
            'custom_slug': 'promo26'
        }
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'short_url' in data['data']
    assert data['data']['short_url'] == 'https://short.ch/promo26'
    assert 'clicks' in data['data']
    assert data['data']['clicks'] == 0

def test_link_shortener_demo_empty_input(client):
    """Testet das Verhalten, wenn keine Felder oder ein leeres long_url übergeben werden."""
    # Test fehlendes long_url
    response = client.post(
        '/api/minimal-solutions/link_shortener_demo',
        json={}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'
    assert data['code'] == 'VALIDATION_ERROR'

def test_link_shortener_demo_invalid_input(client):
    """Testet ungültige Eingabeformate."""
    # Test falsches URL-Format
    response_url = client.post(
        '/api/minimal-solutions/link_shortener_demo',
        json={
            'long_url': 'ftp://crafthoster.de/invalid'
        }
    )
    assert response_url.status_code == 400
    data_url = response_url.get_json()
    assert data_url['status'] == 'error'
    assert data_url['code'] == 'VALIDATION_ERROR'
    
    # Test falscher Datentyp für custom_slug
    response_slug = client.post(
        '/api/minimal-solutions/link_shortener_demo',
        json={
            'long_url': 'https://crafthoster.de/promo',
            'custom_slug': 12345
        }
    )
    assert response_slug.status_code == 400
    data_slug = response_slug.get_json()
    assert data_slug['status'] == 'error'
    assert data_slug['code'] == 'VALIDATION_ERROR'
    
    # Test fehlendes JSON
    response_no_json = client.post(
        '/api/minimal-solutions/link_shortener_demo',
        data="nicht json"
    )
    assert response_no_json.status_code == 400
    data_no_json = response_no_json.get_json()
    assert data_no_json['status'] == 'error'
    assert data_no_json['code'] == 'BAD_REQUEST'
