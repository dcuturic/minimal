import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.timestamp_converter.timestamp_converter_api import api_bp

class TestTimestampConverter(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        # Test timestamp to date
        response = self.client.post('/api/minimal-solutions/timestamp_converter', json={
            "mode": "timestamp_to_date",
            "value": 1715368920,
            "timezone": "UTC"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('result', data.get('data', {}))
        
        # Test date to timestamp
        response_date = self.client.post('/api/minimal-solutions/timestamp_converter', json={
            "mode": "date_to_timestamp",
            "value": "2026-05-10T19:22:00Z",
            "timezone": "UTC"
        })
        self.assertEqual(response_date.status_code, 200)
        data_date = json.loads(response_date.data)
        self.assertTrue(data_date.get('success'))
        self.assertIn('result', data_date.get('data', {}))

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/timestamp_converter', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('mode', details)
        self.assertIn('value', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Test invalid mode
        response_mode = self.client.post('/api/minimal-solutions/timestamp_converter', json={
            "mode": "invalid_mode",
            "value": 1715368920
        })
        self.assertEqual(response_mode.status_code, 400)
        data_mode = json.loads(response_mode.data)
        self.assertFalse(data_mode.get('success'))
        self.assertEqual(data_mode.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertIn('mode', data_mode.get('error', {}).get('details', {}))
        
        # Test invalid timestamp value
        response_ts = self.client.post('/api/minimal-solutions/timestamp_converter', json={
            "mode": "timestamp_to_date",
            "value": "not_a_number"
        })
        self.assertEqual(response_ts.status_code, 400)
        data_ts = json.loads(response_ts.data)
        self.assertEqual(data_ts.get('error', {}).get('code'), 'VALIDATION_ERROR')
        
        # Test invalid date value
        response_dt = self.client.post('/api/minimal-solutions/timestamp_converter', json={
            "mode": "date_to_timestamp",
            "value": "not_a_date"
        })
        self.assertEqual(response_dt.status_code, 400)
        data_dt = json.loads(response_dt.data)
        self.assertEqual(data_dt.get('error', {}).get('code'), 'VALIDATION_ERROR')

if __name__ == '__main__':
    unittest.main()
