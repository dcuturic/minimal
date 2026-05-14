import pytest

def test_opengraph_preview_happy_path(client):
    """Testet den Erfolgsfall mit allen Eingabefeldern."""
    response = client.post(
        '/api/minimal-solutions/opengraph_preview',
        json={
            'title': 'Test Title',
            'description': 'Test Description',
            'image_url': 'https://example.com/image.jpg',
            'domain': 'example.com'
        }
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'html' in data['data']
    
    html_output = data['data']['html']
    assert '<meta property="og:type" content="website">' in html_output
    assert '<meta property="og:title" content="Test Title">' in html_output
    assert '<meta property="og:description" content="Test Description">' in html_output
    assert '<meta property="og:image" content="https://example.com/image.jpg">' in html_output
    assert '<meta property="og:url" content="https://example.com">' in html_output
    
    preview_data = data['data']['preview_data']
    assert preview_data['title'] == 'Test Title'
    assert preview_data['domain'] == 'example.com'

def test_opengraph_preview_empty_input(client):
    """Testet das Verhalten, wenn keine Felder übergeben werden."""
    response = client.post(
        '/api/minimal-solutions/opengraph_preview',
        json={}
    )
    assert response.status_code == 400
    data = response.get_json()
    assert data['status'] == 'error'
    assert data['code'] == 'VALIDATION_ERROR'

def test_opengraph_preview_invalid_input(client):
    """Testet ungültige Eingabeformate."""
    # Test falscher Datentyp für Titel
    response_type = client.post(
        '/api/minimal-solutions/opengraph_preview',
        json={
            'title': 12345
        }
    )
    assert response_type.status_code == 400
    data_type = response_type.get_json()
    assert data_type['status'] == 'error'
    assert data_type['code'] == 'VALIDATION_ERROR'
    
    # Test fehlendes JSON
    response_no_json = client.post(
        '/api/minimal-solutions/opengraph_preview',
        data="nicht json"
    )
    assert response_no_json.status_code == 400
    data_no_json = response_no_json.get_json()
    assert data_no_json['status'] == 'error'
    assert data_no_json['code'] == 'BAD_REQUEST'
