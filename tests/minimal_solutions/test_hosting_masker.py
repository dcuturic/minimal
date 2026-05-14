import unittest
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.hosting_masker.api_hosting_masker import api_bp

class TestHostingMasker(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        response = self.client.post('/api/minimal-solutions/hosting_masker', json={
            "source": "192.168.1.100",
            "config": {"mask_pattern": "***.***.*.***"},
            "mode": "IP-Address"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertEqual(data['data']['source'], "192.168.1.100")
        self.assertEqual(data['data']['config'], {"mask_pattern": "***.***.*.***"})
        self.assertEqual(data['data']['mode'], "IP-Address")
        self.assertTrue(data['data']['masked'])

    def test_empty_input(self):
        response = self.client.post('/api/minimal-solutions/hosting_masker', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('source', details)
        self.assertIn('mode', details)

    def test_invalid_input(self):
        response = self.client.post('/api/minimal-solutions/hosting_masker', json={
            "source": 12345,
            "config": "invalid_string_instead_of_dict",
            "mode": 123
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
