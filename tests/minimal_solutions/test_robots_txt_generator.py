import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.robots_txt_generator.robots_txt_generator_api import api_bp

class TestRobotsTxtGenerator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass # Blueprint wurde möglicherweise schon registriert
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/robots_txt_generator', json={
            "allow": "api/\npublic/",
            "disallow": "admin/\nprivate/",
            "sitemap_url": "https://example.com/sitemap.xml",
            "user_agent": "*"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('result', data.get('data', {}))
        result_text = data['data']['result']
        self.assertIn("User-agent: *", result_text)
        self.assertIn("Allow: /api/", result_text)
        self.assertIn("Disallow: /admin/", result_text)
        self.assertIn("Sitemap: https://example.com/sitemap.xml", result_text)

    def test_empty_input(self):
        """Test with empty input and expect a success response with default user-agent."""
        response = self.client.post('/api/minimal-solutions/robots_txt_generator', json={})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('result', data.get('data', {}))
        result_text = data['data']['result']
        self.assertIn("User-agent: *", result_text)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/robots_txt_generator', json={
            "allow": 123
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('allow', details)

if __name__ == '__main__':
    unittest.main()
