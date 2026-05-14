import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.regex_tester.regex_tester_api import api_bp

class TestRegexTester(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        # Registriere die API-Blueprint für den Test, falls noch nicht geschehen
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass # Blueprint wurde möglicherweise schon registriert
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid pattern and text."""
        response = self.client.post('/api/minimal-solutions/regex_tester', json={
            "pattern": r"\b[a-z]+@[a-z]+\.[a-z]+\b",
            "text": "My email is test@example.com",
            "flags": "i"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('matches', data.get('data', {}))
        self.assertEqual(len(data['data']['matches']), 1)
        self.assertEqual(data['data']['matches'][0]['match'], 'test@example.com')

    def test_empty_input(self):
        """Test with empty input and expect validation error."""
        response = self.client.post('/api/minimal-solutions/regex_tester', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', [])
        self.assertTrue(any("Feld 'pattern' fehlt" in d for d in details))
        self.assertTrue(any("Feld 'text' fehlt" in d for d in details))

    def test_invalid_input(self):
        """Test with invalid regex pattern and expect bad request."""
        response = self.client.post('/api/minimal-solutions/regex_tester', json={
            "pattern": "[invalid_regex",
            "text": "test",
            "flags": ""
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'BAD_REQUEST')
        message = data.get('error', {}).get('message', '')
        self.assertTrue("Ungültiger Regex" in message)

if __name__ == '__main__':
    unittest.main()
