import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.curl_command_generator.curl_command_generator_api import api_bp

class TestCurlCommandGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/curl_command_generator', json={
            "method": "POST",
            "url": "https://api.example.com/data",
            "headers": {
                "Content-Type": "application/json"
            },
            "body": {
                "test": "value"
            }
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('curl_command', data.get('data', {}))
        self.assertTrue(data['data']['curl_command'].startswith("curl -X POST 'https://api.example.com/data'"))

    def test_empty_input(self):
        """Test with empty input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/curl_command_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', [])
        # 'method' and 'url' should be in the error messages
        self.assertTrue(any("Feld 'method' fehlt" in detail for detail in details))
        self.assertTrue(any("Feld 'url' fehlt" in detail for detail in details))

    def test_invalid_input(self):
        """Test with invalid input types and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/curl_command_generator', json={
            "method": "INVALID",
            "url": "",
            "headers": "not_a_dict"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', [])
        self.assertTrue(any("muss GET, POST, PUT, PATCH oder DELETE sein" in detail for detail in details))
        self.assertTrue(any("darf nicht leer sein" in detail for detail in details))
        self.assertTrue(any("muss ein Objekt/Dictionary sein" in detail for detail in details))

if __name__ == '__main__':
    unittest.main()
