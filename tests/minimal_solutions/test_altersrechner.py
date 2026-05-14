import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.altersrechner.altersrechner_api import api_bp

class TestAltersrechner(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/altersrechner', json={
            "birth_date": "1990-01-01",
            "target_date": "2023-01-01"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('years', data.get('data', {}))
        self.assertEqual(data['data']['years'], 33)
        self.assertEqual(data['data']['months'], 0)
        self.assertEqual(data['data']['days'], 0)

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/altersrechner', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('birth_date', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Test invalid date format
        response = self.client.post('/api/minimal-solutions/altersrechner', json={
            "birth_date": "01.01.1990"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('birth_date', details)

        # Test target_date before birth_date
        response2 = self.client.post('/api/minimal-solutions/altersrechner', json={
            "birth_date": "2000-01-01",
            "target_date": "1999-01-01"
        })
        self.assertEqual(response2.status_code, 400)
        data2 = json.loads(response2.data)
        self.assertIn('target_date', data2.get('error', {}).get('details', {}))

if __name__ == '__main__':
    unittest.main()
