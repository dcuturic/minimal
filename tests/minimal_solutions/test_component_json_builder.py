import unittest
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app

class TestComponentJsonBuilder(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.endpoint = '/api/minimal-solutions/component_json_builder'

    def test_happy_path(self):
        payload = {
            "template": "<div class=\"card\">{{title}}</div>",
            "env": {"title": "Hello"},
            "css": ".card { color: red; }",
            "js": "console.log('hi');"
        }
        response = self.client.post(
            self.endpoint,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('component', data['data'])
        self.assertEqual(data['data']['component']['template'], "<div class=\"card\">{{title}}</div>")
        self.assertEqual(data['data']['component']['env'], {"title": "Hello"})
        self.assertEqual(data['data']['component']['css'], ".card { color: red; }")
        self.assertEqual(data['data']['component']['js'], "console.log('hi');")

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
            "template": "",
            "env": {"key": "val"},
            "css": "",
            "js": ""
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
        self.assertIn('template', data['details'])

if __name__ == '__main__':
    unittest.main()
