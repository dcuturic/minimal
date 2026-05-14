import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.dateigroessen_converter.dateigroessen_converter_api import api_bp

class TestDateigroessenConverter(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/dateigroessen_converter', json={
            "value": 1024,
            "from_unit": "MB",
            "to_unit": "GB"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('result', data.get('data', {}))
        self.assertEqual(data['data']['result'], 1.0)
        self.assertEqual(data['data']['formatted'], "1.00 GB")

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/dateigroessen_converter', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('value', details)
        self.assertIn('from_unit', details)
        self.assertIn('to_unit', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/dateigroessen_converter', json={
            "value": "not-a-number",
            "from_unit": "XYZ",
            "to_unit": "ABC"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('value', details)
        self.assertIn('from_unit', details)
        self.assertIn('to_unit', details)

if __name__ == '__main__':
    unittest.main()
