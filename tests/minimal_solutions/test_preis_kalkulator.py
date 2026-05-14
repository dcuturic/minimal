import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.preis_kalkulator.preis_kalkulator_api import api_bp

class TestPreisKalkulator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/preis_kalkulator', json={
            "base_price": 100.0,
            "margin": 20.0,
            "discount": 5.0,
            "markup": 10.0
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('final_price', data.get('data', {}))
        self.assertEqual(data['data']['final_price'], 125.0)

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/preis_kalkulator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('base_price', details)
        self.assertIn('margin', details)
        self.assertIn('discount', details)
        self.assertIn('markup', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/preis_kalkulator', json={
            "base_price": -5,
            "margin": -10,
            "discount": 105,
            "markup": "invalid"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('base_price', details)
        self.assertIn('margin', details)
        self.assertIn('discount', details)
        self.assertIn('markup', details)

if __name__ == '__main__':
    unittest.main()
