import unittest
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app

class TestHtmlFragmentWrapper(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.endpoint = '/api/minimal-solutions/html_fragment_wrapper'

    def test_happy_path(self):
        payload = {
            "html": "<div class='hello'>Hello</div>",
            "css": ".hello { color: red; }",
            "js": "console.log('hello');",
            "name": "Test Fragment"
        }
        response = self.client.post(
            self.endpoint,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('wrapped_html', data['data'])
        self.assertIn("<title>Test Fragment</title>", data['data']['wrapped_html'])
        self.assertIn("<div class='hello'>Hello</div>", data['data']['wrapped_html'])
        self.assertIn(".hello { color: red; }", data['data']['wrapped_html'])
        self.assertIn("console.log('hello');", data['data']['wrapped_html'])

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
            "html": "",
            "css": 123,
            "js": False,
            "name": None
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
