import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.ticket_priority_classifier.ticket_priority_classifier_api import api_bp

class TestTicketPriorityClassifier(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        # Registriere die API-Blueprint für den Test, falls noch nicht geschehen
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass # Blueprint wurde möglicherweise schon registriert
        self.client = self.app.test_client()

    def test_happy_path_high(self):
        """Test with valid input (High Priority) and expect a success response."""
        response = self.client.post('/api/minimal-solutions/ticket_priority_classifier', json={
            "ticket_text": "Der Server ist offline und wir haben einen kritischen Ausfall!"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('priority', data.get('data', {}))
        self.assertEqual(data['data']['priority'], 'Hoch')

    def test_happy_path_medium(self):
        """Test with valid input (Medium Priority) and expect a success response."""
        response = self.client.post('/api/minimal-solutions/ticket_priority_classifier', json={
            "ticket_text": "Ich habe einen Fehler in der Software gefunden, brauche Hilfe."
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertEqual(data['data']['priority'], 'Mittel')
        
    def test_happy_path_low(self):
        """Test with valid input (Low Priority) and expect a success response."""
        response = self.client.post('/api/minimal-solutions/ticket_priority_classifier', json={
            "ticket_text": "Wie kann ich mein Passwort ändern?"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertEqual(data['data']['priority'], 'Niedrig')

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/ticket_priority_classifier', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('ticket_text', details)

        response2 = self.client.post('/api/minimal-solutions/ticket_priority_classifier', json={
            "ticket_text": "   "
        })
        self.assertEqual(response2.status_code, 400)
        data2 = json.loads(response2.data)
        self.assertFalse(data2.get('success'))

    def test_invalid_input(self):
        """Test with invalid input type and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/ticket_priority_classifier', json={
            "ticket_text": 12345
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('ticket_text', details)

if __name__ == '__main__':
    unittest.main()
