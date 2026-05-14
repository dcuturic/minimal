import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.seo_generator.seo_generator_api import api_bp

class TestSEOGenerator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/seo_generator', json={
            "topic": "Hausbau",
            "target": "Junge Familien",
            "options": {
                "language": "de",
                "tone": "professional"
            }
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('meta_title', data.get('data', {}))
        self.assertIn('meta_description', data.get('data', {}))
        self.assertIn('keywords', data.get('data', {}))

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/seo_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('topic', details)
        self.assertIn('target', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Test invalid type for topic and target
        response = self.client.post('/api/minimal-solutions/seo_generator', json={
            "topic": 123,
            "target": {"invalid": "type"},
            "options": "should_be_dict"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('topic', details)
        self.assertIn('target', details)
        self.assertIn('options', details)
        
        # Test empty strings
        response_empty_str = self.client.post('/api/minimal-solutions/seo_generator', json={
            "topic": "   ",
            "target": ""
        })
        self.assertEqual(response_empty_str.status_code, 400)
        data_empty_str = json.loads(response_empty_str.data)
        details_empty_str = data_empty_str.get('error', {}).get('details', {})
        self.assertIn('topic', details_empty_str)
        self.assertIn('target', details_empty_str)

if __name__ == '__main__':
    unittest.main()
