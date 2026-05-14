import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_kanban_ticket_card_generator_happy_path(client):
    response = client.post('/api/minimal-solutions/kanban_ticket_card_generator', json={
        "title": "Fix Login Bug",
        "description": "User cannot login with valid credentials.",
        "priority": "high",
        "status": "todo"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "data" in data
    assert "html_preview" in data["data"]

def test_kanban_ticket_card_generator_empty_input(client):
    response = client.post('/api/minimal-solutions/kanban_ticket_card_generator', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "title" in data["errors"]

def test_kanban_ticket_card_generator_invalid_input(client):
    response = client.post('/api/minimal-solutions/kanban_ticket_card_generator', json={
        "title": "",
        "priority": "critical",
        "status": "backlog"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["status"] == "error"
    assert "title" in data["errors"]
    assert "priority" in data["errors"]
    assert "status" in data["errors"]
