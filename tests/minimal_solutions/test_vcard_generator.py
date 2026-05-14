import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.vcard_generator.vcard_generator_api import api_bp

class TestVCardGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/vcard_generator', json={
            "name": "Max Mustermann",
            "email": "max@example.com",
            "phone": "+49 123 45678",
            "company": "Muster GmbH",
            "address": "Musterstraße 1, 12345 Musterstadt"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('vcard', data.get('data', {}))
        self.assertTrue(data['data']['vcard'].startswith('BEGIN:VCARD'))
        self.assertIn('FN:Max Mustermann', data['data']['vcard'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/vcard_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertIn('name', data.get('error', {}).get('details', {}))

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/vcard_generator', json={"name": 12345, "email": True})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertIn('name', data.get('error', {}).get('details', {}))
        self.assertIn('email', data.get('error', {}).get('details', {}))

if __name__ == '__main__':
    unittest.main()
