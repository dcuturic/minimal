import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.css_gradient_generator.css_gradient_generator_api import api_bp

class TestCssGradientGenerator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path_linear(self):
        """Test with valid linear gradient input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/css_gradient_generator', json={
            "colors": ["#ff0000", "#00ff00"],
            "angle": 90,
            "type": "linear"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('css', data.get('data', {}))
        self.assertEqual(data['data']['css'], 'linear-gradient(90deg, #ff0000, #00ff00)')

    def test_happy_path_radial(self):
        """Test with valid radial gradient input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/css_gradient_generator', json={
            "colors": ["#ff0000", "#00ff00"],
            "angle": 0,
            "type": "radial"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('css', data.get('data', {}))
        self.assertEqual(data['data']['css'], 'radial-gradient(circle, #ff0000, #00ff00)')

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/css_gradient_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('colors', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/css_gradient_generator', json={
            "colors": "#ff0000", # invalid, should be list
            "angle": "not-a-number",
            "type": "invalid-type"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('colors', details)

if __name__ == '__main__':
    unittest.main()
