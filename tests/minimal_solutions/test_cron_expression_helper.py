import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.cron_expression_helper.cron_expression_helper_api import api_bp

class TestCronExpressionHelper(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        # Registriere die API-Blueprint für den Test, falls noch nicht geschehen
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass # Blueprint wurde möglicherweise schon registriert
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid cron expression."""
        response = self.client.post('/api/minimal-solutions/cron_expression_helper', json={
            "cron_expression": "0 12 * * *"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('description', data.get('data', {}))
        self.assertIn('next_executions', data.get('data', {}))
        self.assertTrue(isinstance(data['data']['next_executions'], list))
        self.assertEqual(data['data']['expression'], "0 12 * * *")

    def test_empty_input(self):
        """Test with empty input and expect validation error."""
        response = self.client.post('/api/minimal-solutions/cron_expression_helper', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('cron_expression', details)

    def test_invalid_input(self):
        """Test with invalid cron expression (e.g. not 5 parts)."""
        response = self.client.post('/api/minimal-solutions/cron_expression_helper', json={
            "cron_expression": "0 12 *"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('cron_expression', details)

if __name__ == '__main__':
    unittest.main()
