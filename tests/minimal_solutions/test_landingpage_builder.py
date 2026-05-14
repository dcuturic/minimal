import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.landingpage_builder.landingpage_builder_api import api_bp

class TestLandingpageBuilder(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/landingpage_builder', json={
            "topic": "SaaS Platform",
            "target": "Developers",
            "options": {"tone": "professional", "primary_color": "#2563eb"}
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('builder_result', data.get('data', {}))
        self.assertIn('html', data['data']['builder_result'])

    def test_empty_input(self):
        """Test with empty input and expect validation error."""
        response = self.client.post('/api/minimal-solutions/landingpage_builder', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('topic', details)
        self.assertIn('target', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Empty topic
        response = self.client.post('/api/minimal-solutions/landingpage_builder', json={
            "topic": "",
            "target": "Developers"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('topic', details)

if __name__ == '__main__':
    unittest.main()
