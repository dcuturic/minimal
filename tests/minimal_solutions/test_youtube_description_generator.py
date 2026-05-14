import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.youtube_description_generator.youtube_description_generator_api import api_bp

class TestYoutubeDescriptionGenerator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass # Blueprint wurde möglicherweise schon registriert
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/youtube_description_generator', json={
            "title": "Mein tolles Video",
            "summary": "In diesem Video zeige ich euch tolle Dinge.",
            "links": "https://example.com"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('description', data.get('data', {}))
        
        description = data['data']['description']
        self.assertIn("Mein tolles Video", description)
        self.assertIn("In diesem Video zeige ich euch tolle Dinge.", description)
        self.assertIn("https://example.com", description)

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/youtube_description_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('title', details)
        self.assertIn('summary', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Invalid long title
        long_title = "a" * 201
        response = self.client.post('/api/minimal-solutions/youtube_description_generator', json={
            "title": long_title,
            "summary": "Kurze Zusammenfassung"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('title', details)

if __name__ == '__main__':
    unittest.main()
