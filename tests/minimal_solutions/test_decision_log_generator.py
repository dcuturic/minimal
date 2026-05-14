import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.decision_log_generator.decision_log_generator_api import api_bp

class TestDecisionLogGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/decision_log_generator', json={
            "context": "We need to choose a database for the new microservice.",
            "decision": "PostgreSQL",
            "reason": "It offers robust ACID compliance, JSONB support, and is well-known by the team."
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('log', data.get('data', {}))
        self.assertIn('PostgreSQL', data['data']['log'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/decision_log_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('context', details)
        self.assertIn('decision', details)
        self.assertIn('reason', details)

    def test_invalid_input(self):
        """Test with invalid input (empty strings) and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/decision_log_generator', json={
            "context": "  ",
            "decision": "   ",
            "reason": ""
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('context', details)
        self.assertIn('decision', details)
        self.assertIn('reason', details)

if __name__ == '__main__':
    unittest.main()
