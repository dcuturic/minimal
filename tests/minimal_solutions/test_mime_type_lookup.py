import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.mime_type_lookup.mime_type_lookup_api import api_bp

class TestMimeTypeLookup(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass # Blueprint wurde möglicherweise schon registriert
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/mime_type_lookup', json={
            "query": "application/json"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('results', data.get('data', {}))
        results = data['data']['results']
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0]['mime_type'], "application/json")
        self.assertIn(".json", results[0]['extension'])

    def test_happy_path_extension(self):
        """Test with file extension input."""
        response = self.client.post('/api/minimal-solutions/mime_type_lookup', json={
            "query": ".html"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        results = data.get('data', {}).get('results', [])
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0]['mime_type'], "text/html")
        self.assertIn(".html", results[0]['extension'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/mime_type_lookup', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('query', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/mime_type_lookup', json={
            "query": "   " # empty string after strip
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('query', details)
        
        response2 = self.client.post('/api/minimal-solutions/mime_type_lookup', json={
            "query": 12345
        })
        self.assertEqual(response2.status_code, 400)
        data2 = json.loads(response2.data)
        self.assertIn('query', data2.get('error', {}).get('details', {}))

if __name__ == '__main__':
    unittest.main()
