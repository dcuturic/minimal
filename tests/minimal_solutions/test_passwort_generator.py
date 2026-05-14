import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.passwort_generator.passwort_generator_api import api_bp

class TestPasswortGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/passwort_generator', json={
            "length": 16,
            "use_numbers": True,
            "use_symbols": True,
            "use_uppercase": True
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('password', data.get('data', {}))
        self.assertEqual(len(data['data']['password']), 16)

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/passwort_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('length', details)
        self.assertIn('use_numbers', details)
        self.assertIn('use_symbols', details)
        self.assertIn('use_uppercase', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/passwort_generator', json={
            "length": 3,
            "use_numbers": "yes",  # Invalid type
            "use_symbols": True,
            "use_uppercase": True
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('use_numbers', details)
        
        # Test length validation (too short)
        response2 = self.client.post('/api/minimal-solutions/passwort_generator', json={
            "length": 3,
            "use_numbers": True,
            "use_symbols": True,
            "use_uppercase": True
        })
        self.assertEqual(response2.status_code, 400)
        data2 = json.loads(response2.data)
        self.assertIn('length', data2.get('error', {}).get('details', {}))

if __name__ == '__main__':
    unittest.main()
