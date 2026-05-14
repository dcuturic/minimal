import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.feature_flag_panel_demo.feature_flag_panel_demo_api import api_bp

class TestFeatureFlagPanelDemo(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/feature_flag_panel_demo', json={
            "flags": ["Enable Beta Features", "New UI Layout", "Dark Mode Default"]
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('flags', data.get('data', {}))
        flags = data['data']['flags']
        self.assertEqual(len(flags), 3)
        self.assertEqual(flags[0]['name'], "Enable Beta Features")
        self.assertEqual(flags[0]['enabled'], False)

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/feature_flag_panel_demo', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Invalid data type for flags
        response = self.client.post('/api/minimal-solutions/feature_flag_panel_demo', json={
            "flags": "Not a list"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')

        # Invalid element in flags array
        response2 = self.client.post('/api/minimal-solutions/feature_flag_panel_demo', json={
            "flags": [123, "Test"]
        })
        self.assertEqual(response2.status_code, 400)
        data2 = json.loads(response2.data)
        self.assertFalse(data2.get('success'))
        self.assertEqual(data2.get('error', {}).get('code'), 'VALIDATION_ERROR')

        # Empty array
        response3 = self.client.post('/api/minimal-solutions/feature_flag_panel_demo', json={
            "flags": []
        })
        self.assertEqual(response3.status_code, 400)
        data3 = json.loads(response3.data)
        self.assertFalse(data3.get('success'))
        self.assertEqual(data3.get('error', {}).get('code'), 'VALIDATION_ERROR')

if __name__ == '__main__':
    unittest.main()
