import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.rechnungsnummer_generator.rechnungsnummer_generator_api import api_bp

class TestRechnungsnummerGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/rechnungsnummer_generator', json={
            "prefix": "RE",
            "year": "2026",
            "start_number": 1,
            "count": 5
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('numbers', data.get('data', {}))
        self.assertEqual(len(data['data']['numbers']), 5)
        self.assertEqual(data['data']['numbers'][0], "RE-2026-0001")
        self.assertEqual(data['data']['pattern'], "RE-2026-[Number(4 digits)]")

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/rechnungsnummer_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('prefix', details)
        self.assertIn('year', details)
        self.assertIn('start_number', details)
        self.assertIn('count', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/rechnungsnummer_generator', json={
            "prefix": "RE",
            "year": "2026",
            "start_number": -1, # Invalid start_number
            "count": 600 # Invalid count
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('start_number', details)
        self.assertIn('count', details)

if __name__ == '__main__':
    unittest.main()
