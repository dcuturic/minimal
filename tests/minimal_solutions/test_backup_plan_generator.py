import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.backup_plan_generator.backup_plan_generator_api import api_bp

class TestBackupPlanGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/backup_plan_generator', json={
            "frequency": "daily",
            "retention_days": 30,
            "storage_type": "s3"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('schedule', data.get('data', {}))
        self.assertIn('script_template', data.get('data', {}))

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/backup_plan_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('frequency', details)
        self.assertIn('retention_days', details)
        self.assertIn('storage_type', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/backup_plan_generator', json={
            "frequency": "invalid_frequency",
            "retention_days": -5,
            "storage_type": "invalid_storage"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('frequency', details)
        self.assertIn('retention_days', details)
        self.assertIn('storage_type', details)

if __name__ == '__main__':
    unittest.main()
