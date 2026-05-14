import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.release_notes_generator.release_notes_generator_api import api_bp

class TestReleaseNotesGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/release_notes_generator', json={
            "version": "v1.0.0",
            "features": ["Feature 1", "Feature 2"],
            "fixes": ["Fix 1"],
            "breaking_changes": ["Breaking Change 1"]
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('result', data.get('data', {}))
        self.assertIn('# Release Notes - v1.0.0', data['data']['result'])
        self.assertIn('## 🚀 Features', data['data']['result'])
        self.assertIn('- Feature 1', data['data']['result'])
        self.assertIn('## 🐛 Bug Fixes', data['data']['result'])
        self.assertIn('## ⚠️ Breaking Changes', data['data']['result'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/release_notes_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('version', details)

    def test_invalid_input(self):
        """Test with invalid input types and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/release_notes_generator', json={
            "version": 123,
            "features": "Not a list",
            "fixes": [123],
            "breaking_changes": [True]
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('version', details)
        self.assertIn('features', details)
        self.assertIn('fixes', details)
        self.assertIn('breaking_changes', details)

if __name__ == '__main__':
    unittest.main()
