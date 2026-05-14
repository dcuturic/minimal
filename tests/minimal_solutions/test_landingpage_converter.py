import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.landingpage_converter.landingpage_converter_api import api_bp

class TestLandingpageConverter(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/landingpage_converter', json={
            "topic": "KI-gestützte Datenanalyse",
            "target": "Datenanalysten und Manager",
            "options": "Schnell, Präzise, Skalierbar"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('converted_data', data.get('data', {}))
        self.assertIn('meta', data.get('data', {}))
        self.assertEqual(data['data']['meta']['topic'], "KI-gestützte Datenanalyse")
        self.assertEqual(data['data']['meta']['target'], "Datenanalysten und Manager")
        self.assertEqual(len(data['data']['converted_data']['features']), 3)

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/landingpage_converter', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('topic', details)
        self.assertIn('target', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Missing target and invalid options type (e.g. integer)
        response = self.client.post('/api/minimal-solutions/landingpage_converter', json={
            "topic": "Only Topic",
            "options": 12345
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('target', details)
        self.assertIn('options', details)

if __name__ == '__main__':
    unittest.main()
