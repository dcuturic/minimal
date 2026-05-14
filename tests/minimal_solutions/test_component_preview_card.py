import unittest
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app

class TestComponentPreviewCard(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.endpoint = '/api/minimal-solutions/component_preview_card'

    def test_happy_path(self):
        payload = {
            "component_name": "Primary Button",
            "category": "Buttons",
            "preview_html": "<button class='btn btn-primary'>Click me</button>"
        }
        response = self.client.post(
            self.endpoint,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('preview_card', data['data'])
        self.assertEqual(data['data']['preview_card']['component_name'], "Primary Button")
        self.assertEqual(data['data']['preview_card']['category'], "Buttons")
        self.assertEqual(data['data']['preview_card']['preview_html'], "<button class='btn btn-primary'>Click me</button>")

    def test_empty_input(self):
        response = self.client.post(
            self.endpoint,
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['code'], 'VALIDATION_ERROR')

    def test_invalid_input(self):
        payload = {
            "component_name": "",
            "category": "UI",
            "preview_html": 123
        }
        response = self.client.post(
            self.endpoint,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['code'], 'VALIDATION_ERROR')

if __name__ == '__main__':
    unittest.main()
