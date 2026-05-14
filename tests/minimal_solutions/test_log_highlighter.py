import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.log_highlighter.log_highlighter_api import api_bp

class TestLogHighlighter(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/log_highlighter', json={
            "log_text": "2023-10-12 INFO System Start\n2023-10-12 ERROR Connection Failed\n2023-10-12 WARN High memory"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('lines', data.get('data', {}))
        self.assertEqual(len(data['data']['lines']), 3)
        self.assertEqual(data['data']['lines'][0]['level'], 'INFO')
        self.assertEqual(data['data']['lines'][1]['level'], 'ERROR')
        self.assertEqual(data['data']['lines'][2]['level'], 'WARN')

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/log_highlighter', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertIn('log_text', data.get('error', {}).get('details', {}))
        
        # Test empty string
        response2 = self.client.post('/api/minimal-solutions/log_highlighter', json={"log_text": "   "})
        self.assertEqual(response2.status_code, 400)
        data2 = json.loads(response2.data)
        self.assertIn('log_text', data2.get('error', {}).get('details', {}))

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/log_highlighter', json={
            "log_text": 123
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertIn('log_text', data.get('error', {}).get('details', {}))

if __name__ == '__main__':
    unittest.main()
