import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.hosting_summarizer.api_hosting_summarizer import api_bp

class TestHostingSummarizer(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        response = self.client.post('/api/minimal-solutions/hosting_summarizer', json={
            "source": "https://github.com/example/backend",
            "config": {"format": "pdf"},
            "mode": "detailed"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertEqual(data['data']['source'], "https://github.com/example/backend")
        self.assertEqual(data['data']['mode'], "detailed")
        self.assertEqual(data['data']['status'], "success")
        self.assertTrue(data['data']['summarized'])

    def test_empty_input(self):
        response = self.client.post('/api/minimal-solutions/hosting_summarizer', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('source', details)
        self.assertIn('mode', details)

    def test_invalid_input(self):
        response = self.client.post('/api/minimal-solutions/hosting_summarizer', json={
            "source": 12345,
            "config": "invalid_config_type",
            "mode": ""
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('source', details)
        self.assertIn('config', details)
        self.assertIn('mode', details)

if __name__ == '__main__':
    unittest.main()
