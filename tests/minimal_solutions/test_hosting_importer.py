import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.hosting_importer.api_hosting_importer import api_bp

class TestHostingImporter(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        response = self.client.post('/api/minimal-solutions/hosting_importer', json={
            "source": "https://github.com/example/my-project.git",
            "config": {"branch": "main"},
            "mode": "production"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertEqual(data['data']['source'], "https://github.com/example/my-project.git")
        self.assertEqual(data['data']['config'], {"branch": "main"})
        self.assertEqual(data['data']['mode'], "production")
        self.assertTrue(data['data']['imported'])
        self.assertEqual(data['data']['status'], "success")

    def test_empty_input(self):
        response = self.client.post('/api/minimal-solutions/hosting_importer', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('source', details)
        self.assertIn('mode', details)

    def test_invalid_input(self):
        response = self.client.post('/api/minimal-solutions/hosting_importer', json={
            "source": "   ",
            "mode": ""
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('source', details)
        self.assertIn('mode', details)

if __name__ == '__main__':
    unittest.main()
