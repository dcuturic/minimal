import unittest
import json
import os
import sys
from unittest.mock import patch, MagicMock

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.website_health_check_demo.website_health_check_demo_api import api_bp

class TestWebsiteHealthCheckDemo(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    @patch('urllib.request.urlopen')
    def test_happy_path(self, mock_urlopen):
        """Test with valid input and expect a success response."""
        mock_response = MagicMock()
        mock_response.getcode.return_value = 200
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        response = self.client.post('/api/minimal-solutions/website_health_check_demo', json={
            "url": "https://crafthoster.de"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('status_code', data.get('data', {}))
        self.assertEqual(data['data']['status_code'], 200)
        self.assertTrue(data['data']['is_up'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/website_health_check_demo', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('url', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/website_health_check_demo', json={
            "url": "not-a-valid-url"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('url', details)

if __name__ == '__main__':
    unittest.main()
