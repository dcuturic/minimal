import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.kontaktkarten_generator.kontaktkarten_generator_api import api_bp

class TestKontaktkartenGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/kontaktkarten_generator', json={
            "name": "Max Mustermann",
            "email": "max@example.com",
            "phone": "+49 123 456789",
            "company": "Mustermann GmbH",
            "website": "https://example.com"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('vcard', data.get('data', {}))
        self.assertIn('BEGIN:VCARD', data['data']['vcard'])
        self.assertIn('Max Mustermann', data['data']['vcard'])
        self.assertIn('max@example.com', data['data']['vcard'])
        self.assertIn('+49 123 456789', data['data']['vcard'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/kontaktkarten_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('name', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Invalid: name is empty
        response = self.client.post('/api/minimal-solutions/kontaktkarten_generator', json={
            "name": "",
            "email": "max@example.com"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('name', details)

if __name__ == '__main__':
    unittest.main()
