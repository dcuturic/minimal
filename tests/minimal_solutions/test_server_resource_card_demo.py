import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.server_resource_card_demo.server_resource_card_demo_api import api_bp

class TestServerResourceCardDemo(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/server_resource_card_demo', json={
            "cpu": 45.5,
            "ram": 60,
            "disk": 80
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('data', data)
        self.assertEqual(data['data']['cpu'], 45.5)
        self.assertEqual(data['data']['status']['cpu'], 'normal')
        self.assertEqual(data['data']['status']['ram'], 'normal')
        self.assertEqual(data['data']['status']['disk'], 'warning')

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/server_resource_card_demo', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('cpu', details)
        self.assertIn('ram', details)
        self.assertIn('disk', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/server_resource_card_demo', json={
            "cpu": "not_a_number",
            "ram": 150,
            "disk": -10
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('cpu', details)
        self.assertIn('ram', details)
        self.assertIn('disk', details)

if __name__ == '__main__':
    unittest.main()
