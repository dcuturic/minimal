import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.api_request_builder.api_request_builder_api import api_bp

class TestApiRequestBuilder(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        # Registriere die API-Blueprint für den Test, falls noch nicht geschehen
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass # Blueprint wurde möglicherweise schon registriert
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/api_request_builder', json={
            "method": "POST",
            "url": "https://api.example.com/v1/users",
            "headers": {
                "Authorization": "Bearer token123",
                "Content-Type": "application/json"
            },
            "body": {
                "name": "Jane Doe",
                "email": "jane@example.com"
            }
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('preview', data.get('data', {}))
        self.assertIn('curl', data.get('data', {}))
        self.assertIn('raw', data.get('data', {}))
        self.assertIn('curl -X POST', data['data']['curl'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/api_request_builder', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertIn('method', data.get('error', {}).get('details', {}))
        self.assertIn('url', data.get('error', {}).get('details', {}))

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/api_request_builder', json={
            "method": "INVALID_METHOD",
            "url": "ftp://example.com"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertIn('method', data.get('error', {}).get('details', {}))
        self.assertIn('url', data.get('error', {}).get('details', {}))

if __name__ == '__main__':
    unittest.main()
