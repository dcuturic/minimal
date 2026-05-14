import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.maintenance_page_generator.maintenance_page_generator_api import api_bp

class TestMaintenancePageGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/maintenance_page_generator', json={
            "title": "We'll be back soon!",
            "message": "We are currently performing scheduled maintenance to improve our services. Thank you for your patience.",
            "eta": "2 hours"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('html_output', data.get('data', {}))
        self.assertIn('We&#39;ll be back soon!' if '&#39;' in data['data']['html_output'] else "We'll be back soon!", data['data']['html_output'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/maintenance_page_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('title', details)
        self.assertIn('message', details)
        self.assertIn('eta', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/maintenance_page_generator', json={
            "title": 123, # Invalid type
            "message": "", # Empty string
            "eta": ["not a string"] # Invalid type
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('title', details)
        self.assertIn('message', details)
        self.assertIn('eta', details)

if __name__ == '__main__':
    unittest.main()
