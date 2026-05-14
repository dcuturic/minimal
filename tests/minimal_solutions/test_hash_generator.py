import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.hash_generator.hash_generator_api import api_bp

class TestHashGenerator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        # Registriere die API-Blueprint für den Test, falls noch nicht geschehen
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass # Blueprint wurde möglicherweise schon registriert
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response for hashing."""
        response = self.client.post('/api/minimal-solutions/hash_generator', json={
            "text": "hello world",
            "algorithm": "md5"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('result', data.get('data', {}))
        self.assertEqual(data['data']['result'], '5eb63bbbe01eeed093cb22bb8f5acdc3')

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/hash_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('text', details)
        self.assertIn('algorithm', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/hash_generator', json={
            "text": "hello",
            "algorithm": "invalid_algo"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('algorithm', details)

if __name__ == '__main__':
    unittest.main()
