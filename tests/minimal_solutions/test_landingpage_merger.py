import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.landingpage_merger.landingpage_merger_api import api_bp

class TestLandingpageMerger(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/landingpage_merger', json={
            "topic": "Sommerkollektion 2026",
            "target": "Junge Erwachsene",
            "options": "Fokus auf Nachhaltigkeit"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertEqual(data.get('data', {}).get('merge_status'), 'success')
        self.assertIn('merge_result', data.get('data', {}))

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/landingpage_merger', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertTrue('topic' in data.get('error', {}).get('details', {}) or '_global' in data.get('error', {}).get('details', {}))

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/landingpage_merger', json={"topic": 12345, "target": []})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertIn('topic', data.get('error', {}).get('details', {}))
        self.assertIn('target', data.get('error', {}).get('details', {}))

if __name__ == '__main__':
    unittest.main()
