import unittest
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app

class TestTranslationMissingKeyFinder(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_happy_path(self):
        base_json = {
            "welcome": "Welcome",
            "button": {
                "submit": "Submit",
                "cancel": "Cancel"
            }
        }
        target_json = {
            "welcome": "Willkommen",
            "button": {
                "submit": "Absenden"
            }
        }
        response = self.client.post('/api/minimal-solutions/translation_missing_key_finder', json={
            "base_json": base_json,
            "target_json": target_json
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertIn('missing_keys', data['data'])
        self.assertIn('button.cancel', data['data']['missing_keys'])

    def test_empty_input(self):
        response = self.client.post('/api/minimal-solutions/translation_missing_key_finder', json={})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['error']['code'], 'VALIDATION_ERROR')

    def test_invalid_input(self):
        response = self.client.post('/api/minimal-solutions/translation_missing_key_finder', json={
            "base_json": "not a dictionary",
            "target_json": 123
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['error']['code'], 'VALIDATION_ERROR')

if __name__ == '__main__':
    unittest.main()
