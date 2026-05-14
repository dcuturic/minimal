import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.time_estimation_calculator.time_estimation_calculator_api import api_bp

class TestTimeEstimationCalculator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/time_estimation_calculator', json={
            "ticket_count": 50,
            "minutes_per_ticket": 30,
            "days": 5,
            "workers": 2
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('total_hours_required', data.get('data', {}))
        self.assertIn('total_hours_available', data.get('data', {}))
        self.assertIn('is_feasible', data.get('data', {}))
        self.assertIn('utilization_percent', data.get('data', {}))

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/time_estimation_calculator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('ticket_count', details)
        self.assertIn('minutes_per_ticket', details)
        self.assertIn('days', details)
        self.assertIn('workers', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/time_estimation_calculator', json={
            "ticket_count": -5,
            "minutes_per_ticket": "abc",
            "days": -1,
            "workers": "no"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('ticket_count', details)
        self.assertIn('minutes_per_ticket', details)
        self.assertIn('days', details)
        self.assertIn('workers', details)

if __name__ == '__main__':
    unittest.main()
