import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.feature_comparison_table.feature_comparison_table_api import api_bp

class TestFeatureComparisonTable(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/feature_comparison_table', json={
            "features": ["User Management", "API Access"],
            "items": [
                {
                    "name": "Basic Plan",
                    "User Management": True,
                    "API Access": False
                },
                {
                    "name": "Pro Plan",
                    "User Management": True,
                    "API Access": True
                }
            ]
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('features', data.get('data', {}))
        self.assertIn('items', data.get('data', {}))
        self.assertEqual(len(data['data']['features']), 2)
        self.assertEqual(len(data['data']['items']), 2)

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/feature_comparison_table', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('features', details)
        self.assertIn('items', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/feature_comparison_table', json={
            "features": "not a list",
            "items": [
                {
                    "not-a-name": "Something"
                }
            ]
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('features', details)
        self.assertIn('items[0].name', details)

if __name__ == '__main__':
    unittest.main()
