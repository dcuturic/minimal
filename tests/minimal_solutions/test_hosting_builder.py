import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.hosting_builder.api_hosting_builder import api_bp

class TestHostingBuilder(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        response = self.client.post('/api/minimal-solutions/hosting_builder', json={
            "source": "https://github.com/my-org/my-app",
            "config": '{"provider": "aws", "region": "eu-central-1"}',
            "mode": "production"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertEqual(data['data']['source'], "https://github.com/my-org/my-app")
        self.assertEqual(data['data']['status'], "builder_ready")

    def test_empty_input(self):
        response = self.client.post('/api/minimal-solutions/hosting_builder', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('payload', details)

    def test_invalid_input(self):
        response = self.client.post('/api/minimal-solutions/hosting_builder', json={
            "source": "https://github.com/my-org/my-app"
            # config and mode are missing
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('config', details)
        self.assertIn('mode', details)

if __name__ == '__main__':
    unittest.main()
