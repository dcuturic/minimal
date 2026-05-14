import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.webhook_payload_tester.webhook_payload_tester_api import api_bp

class TestWebhookPayloadTester(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        # Registriere die API-Blueprint für den Test, falls noch nicht geschehen
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass # Blueprint wurde möglicherweise schon registriert
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/webhook_payload_tester', json={
            "payload_json": '{"event": "user.created", "data": {"id": 123, "name": "Test User"}}'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertTrue(data.get('data', {}).get('is_valid'))
        self.assertIn('parsed_payload', data.get('data', {}))
        self.assertEqual(data['data']['parsed_payload']['event'], "user.created")

    def test_happy_path_invalid_json_format(self):
        """Test with valid string but invalid JSON content."""
        response = self.client.post('/api/minimal-solutions/webhook_payload_tester', json={
            "payload_json": '{event: "user.created", "data": {"id": 123, "name": "Test User"}' # Invalid JSON string
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertFalse(data.get('data', {}).get('is_valid'))
        self.assertIn('Invalid JSON format', data.get('data', {}).get('message', ''))

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/webhook_payload_tester', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertIn('payload_json', data.get('error', {}).get('details', {}))

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/webhook_payload_tester', json={
            "payload_json": 123 # Invalid type
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        self.assertIn('payload_json', data.get('error', {}).get('details', {}))

if __name__ == '__main__':
    unittest.main()
