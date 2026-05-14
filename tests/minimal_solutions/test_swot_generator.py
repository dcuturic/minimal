import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.swot_generator.swot_generator_api import api_bp

class TestSwotGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/swot_generator', json={
            "topic": "Neue Marketing-Strategie",
            "notes": "Fokus auf Social Media"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('strengths', data.get('data', {}))
        self.assertIn('weaknesses', data.get('data', {}))
        self.assertIn('opportunities', data.get('data', {}))
        self.assertIn('threats', data.get('data', {}))
        self.assertEqual(len(data['data']['strengths']), 3) # 2 standard + 1 from notes

    def test_happy_path_without_notes(self):
        """Test with valid input but without notes."""
        response = self.client.post('/api/minimal-solutions/swot_generator', json={
            "topic": "Neue Marketing-Strategie"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('strengths', data.get('data', {}))
        self.assertEqual(len(data['data']['strengths']), 2)

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/swot_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('topic', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Invalid topic length and type
        response = self.client.post('/api/minimal-solutions/swot_generator', json={
            "topic": "A",
            "notes": 123
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('topic', details)
        self.assertIn('notes', details)

if __name__ == '__main__':
    unittest.main()
