import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.sla_rechner.sla_rechner_api import api_bp

class TestSLARechner(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/sla_rechner', json={
            "priority": "p2",
            "start_time": "2026-05-12T08:00:00"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('deadline', data.get('data', {}))
        self.assertIn('priority_label', data.get('data', {}))
        self.assertIn('time_remaining', data.get('data', {}))
        self.assertEqual(data['data']['priority_label'], 'P2 - High')
        self.assertEqual(data['data']['time_remaining'], '4 Hours SLA')
        self.assertEqual(data['data']['deadline'], '2026-05-12 12:00')

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/sla_rechner', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('priority', details)
        self.assertIn('start_time', details)

    def test_invalid_input(self):
        """Test with invalid input type and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/sla_rechner', json={
            "priority": "p5", # Ungültige Priorität
            "start_time": "kein-datum" # Ungültiges Datum
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('priority', details)
        self.assertIn('start_time', details)

if __name__ == '__main__':
    unittest.main()
