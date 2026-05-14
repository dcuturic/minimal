import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.angebotsnummer_generator.angebotsnummer_generator_api import api_bp

class TestAngebotsnummerGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/angebotsnummer_generator', json={
            "prefix": "ANG",
            "date": "20260511",
            "customer_short": "CRAFT",
            "number": 42
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('numbers', data.get('data', {}))
        self.assertEqual(len(data['data']['numbers']), 1)
        self.assertEqual(data['data']['numbers'][0], "ANG-20260511-CRAFT-042")
        self.assertEqual(data['data']['pattern'], "[Prefix]-[Date]-[Customer]-[Number]")

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/angebotsnummer_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('number', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/angebotsnummer_generator', json={
            "prefix": 123, # Invalid prefix (should be string)
            "date": 20260511, # Invalid date (should be string)
            "customer_short": 456, # Invalid customer_short (should be string)
            "number": None # Invalid number (should not be None)
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('prefix', details)
        self.assertIn('date', details)
        self.assertIn('customer_short', details)
        self.assertIn('number', details)

if __name__ == '__main__':
    unittest.main()
