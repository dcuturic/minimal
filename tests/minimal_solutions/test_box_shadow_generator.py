import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.box_shadow_generator.box_shadow_generator_api import api_bp

class TestBoxShadowGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/box_shadow_generator', json={
            "x": 10,
            "y": 10,
            "blur": 15,
            "spread": -5,
            "opacity": 0.5,
            "color": "#000000",
            "inset": False
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('css', data.get('data', {}))
        self.assertEqual(data['data']['css'], "10px 10px 15px -5px rgba(0, 0, 0, 0.5)")

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/box_shadow_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertIn('x', data.get('error', {}).get('details', {}))

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/box_shadow_generator', json={
            "x": 10,
            "y": 10,
            "blur": -15, # Blur cannot be negative
            "spread": -5,
            "opacity": 0.5
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertIn('blur', data.get('error', {}).get('details', {}))

if __name__ == '__main__':
    unittest.main()
