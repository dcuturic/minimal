import unittest
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.hosting_preview.api_hosting_preview import api_bp

class TestHostingPreview(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        response = self.client.post('/api/minimal-solutions/hosting_preview', json={
            "source": "https://github.com/my-org/my-react-app",
            "config": "React, Nginx",
            "mode": "preview"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertEqual(data['data']['source'], "https://github.com/my-org/my-react-app")
        self.assertEqual(data['data']['config'], "React, Nginx")
        self.assertEqual(data['data']['mode'], "preview")
        self.assertEqual(data['data']['status'], "preview_ready")

    def test_empty_input(self):
        response = self.client.post('/api/minimal-solutions/hosting_preview', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('payload', details)

    def test_invalid_input(self):
        # Missing 'source' is invalid
        response = self.client.post('/api/minimal-solutions/hosting_preview', json={
            "config": "React",
            "mode": "preview"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('source', details)

if __name__ == '__main__':
    unittest.main()
