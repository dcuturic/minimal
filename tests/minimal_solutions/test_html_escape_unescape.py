import json
from app import create_app

def test_html_escape_happy_path():
    app = create_app()
    client = app.test_client()
    
    response = client.post('/api/minimal-solutions/html_escape_unescape', 
                           data=json.dumps({"html_text": "<div>Hello</div>", "mode": "escape"}),
                           content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['result'] == "&lt;div&gt;Hello&lt;/div&gt;"

def test_html_unescape_happy_path():
    app = create_app()
    client = app.test_client()
    
    response = client.post('/api/minimal-solutions/html_escape_unescape', 
                           data=json.dumps({"html_text": "&lt;div&gt;Hello&lt;/div&gt;", "mode": "unescape"}),
                           content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['result'] == "<div>Hello</div>"

def test_empty_input():
    app = create_app()
    client = app.test_client()
    
    response = client.post('/api/minimal-solutions/html_escape_unescape', 
                           data=json.dumps({"html_text": "", "mode": "escape"}),
                           content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['result'] == ""

def test_invalid_input_missing_fields():
    app = create_app()
    client = app.test_client()
    
    response = client.post('/api/minimal-solutions/html_escape_unescape', 
                           data=json.dumps({}),
                           content_type='application/json')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] is False
    assert "html_text" in data['details']
    assert "mode" in data['details']

def test_invalid_input_wrong_mode():
    app = create_app()
    client = app.test_client()
    
    response = client.post('/api/minimal-solutions/html_escape_unescape', 
                           data=json.dumps({"html_text": "text", "mode": "invalid_mode"}),
                           content_type='application/json')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] is False
    assert "mode" in data['details']
