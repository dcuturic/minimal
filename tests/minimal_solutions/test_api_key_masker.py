import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.api_key_masker.api_key_masker_api import api_bp

class TestApiKeyMasker(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/api_key_masker', json={
            "secret": "sk_live_1234567890abcdef",
            "visible_start": 8,
            "visible_end": 4
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('result', data.get('data', {}))
        self.assertEqual(data['data']['result'], 'sk_live_************cdef')

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/api_key_masker', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('secret', details)
        self.assertIn('visible_start', details)
        self.assertIn('visible_end', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Negative visible_start
        response = self.client.post('/api/minimal-solutions/api_key_masker', json={
            "secret": "sk_test_123",
            "visible_start": -1,
            "visible_end": 0
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('visible_start', details)

if __name__ == '__main__':
    unittest.main()
