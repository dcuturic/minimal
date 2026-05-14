import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.datumsdifferenz_rechner.datumsdifferenz_rechner_api import api_bp

class TestDatumsdifferenzRechner(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/datumsdifferenz_rechner', json={
            "start_date": "2023-01-01",
            "end_date": "2024-01-01"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('total_days', data.get('data', {}))
        self.assertEqual(data['data']['total_days'], 365)
        self.assertEqual(data['data']['breakdown']['years'], 1)
        self.assertEqual(data['data']['breakdown']['months'], 0)
        self.assertEqual(data['data']['breakdown']['days'], 0)
        self.assertFalse(data['data']['is_negative'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/datumsdifferenz_rechner', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('start_date', details)
        self.assertIn('end_date', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/datumsdifferenz_rechner', json={
            "start_date": "01.01.2023",
            "end_date": "1st Jan 2024"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('start_date', details)
        self.assertIn('end_date', details)

if __name__ == '__main__':
    unittest.main()
