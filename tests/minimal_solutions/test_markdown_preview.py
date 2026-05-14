import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.markdown_preview.markdown_preview_api import api_bp

class TestMarkdownPreview(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/markdown_preview', json={
            "markdown_text": "# Hello World\n**Bold Text**"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('html', data.get('data', {}))
        self.assertIn('original_length', data.get('data', {}))
        self.assertIn('<h1>Hello World</h1>', data['data']['html'])
        self.assertIn('<strong>Bold Text</strong>', data['data']['html'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/markdown_preview', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('markdown_text', details)

    def test_invalid_input(self):
        """Test with invalid input type and expect validation error response."""
        # Invalid input (number instead of string)
        response = self.client.post('/api/minimal-solutions/markdown_preview', json={
            "markdown_text": 12345
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('markdown_text', details)

if __name__ == '__main__':
    unittest.main()
