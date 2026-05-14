import unittest
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app

class TestComponentDependencyViewer(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.endpoint = '/api/minimal-solutions/component_dependency_viewer'

    def test_happy_path(self):
        payload = {
            "component_json": json.dumps({
                "component": {
                    "css": "body { color: red; }",
                    "js": "console.log(1);",
                    "env": {"API_KEY": "secret"}
                }
            })
        }
        response = self.client.post(
            self.endpoint,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('dependencies', data['data'])
        self.assertIn('inline-css', data['data']['dependencies']['css'])
        self.assertIn('inline-js', data['data']['dependencies']['js'])
        self.assertIn('API_KEY', data['data']['dependencies']['env'])

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
        self.assertIn('component_json', data['details'])

    def test_invalid_input(self):
        payload = {
            "component_json": 123
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
        self.assertIn('component_json', data['details'])

    def test_invalid_json_string(self):
        payload = {
            "component_json": "{invalid_json}"
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
        self.assertIn('component_json', data['details'])

if __name__ == '__main__':
    unittest.main()
