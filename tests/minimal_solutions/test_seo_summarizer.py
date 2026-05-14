import pytest
from app.responses import ErrorCodes

def test_seo_summarizer_happy_path(client):
    """
    Testet den Happy-Path für das SEO Summarizer API-Endpoint.
    """
    payload = {
        "topic": "Wie man einen Garten im Frühling vorbereitet",
        "target": "Hobbygärtner",
        "options": {
            "tone": "informativ"
        }
    }
    
    response = client.post("/api/minimal-solutions/seo_summarizer", json=payload)
    assert response.status_code == 200
    
    data = response.get_json()
    assert data["status"] == "success"
    assert "summary" in data["data"]
    assert data["data"]["topic"] == payload["topic"]
    assert data["data"]["target"] == payload["target"]
    assert data["data"]["options"] == payload["options"]

def test_seo_summarizer_empty_input(client):
    """
    Testet den Empty-Input für das SEO Summarizer API-Endpoint (kein JSON Body).
    """
    response = client.post("/api/minimal-solutions/seo_summarizer", json={})
    assert response.status_code == 400
    
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.VALIDATION_ERROR
    assert "topic" in data["error"]["details"]
    assert "target" in data["error"]["details"]

def test_seo_summarizer_invalid_input(client):
    """
    Testet invaliden Input für das SEO Summarizer API-Endpoint (zu kurze Werte, falsche Typen).
    """
    payload = {
        "topic": "A", # zu kurz (min_length=2)
        "target": 123, # falscher Typ (sollte str sein)
        "options": "kein_dict" # falscher Typ (sollte dict sein)
    }
    
    response = client.post("/api/minimal-solutions/seo_summarizer", json=payload)
    assert response.status_code == 400
    
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.VALIDATION_ERROR
    assert "topic" in data["error"]["details"]
    assert "target" in data["error"]["details"]
    assert "options" in data["error"]["details"]

def test_seo_summarizer_no_json(client):
    """
    Testet den Fall, wenn kein JSON übermittelt wird.
    """
    response = client.post("/api/minimal-solutions/seo_summarizer", data="not a json")
    assert response.status_code == 400
    
    data = response.get_json()
    assert data["status"] == "error"
    assert data["error"]["code"] == ErrorCodes.BAD_REQUEST
