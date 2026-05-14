import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.daily_plan_generator.daily_plan_generator_api import api_bp

class TestDailyPlanGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/daily_plan_generator', json={
            "tasks": ["Task 1", "Task 2", "Task 3"],
            "available_hours": 8.0
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('plan', data.get('data', {}))
        self.assertEqual(len(data['data']['plan']), 3)

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/daily_plan_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('tasks', details)
        self.assertIn('available_hours', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/daily_plan_generator', json={
            "tasks": "Not a list",
            "available_hours": -5
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('tasks', details)
        self.assertIn('available_hours', details)

if __name__ == '__main__':
    unittest.main()
