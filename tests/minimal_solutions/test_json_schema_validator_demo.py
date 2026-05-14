import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.json_schema_validator_demo.json_schema_validator_demo_api import api_bp

class TestJsonSchemaValidatorDemo(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/json_schema_validator_demo', json={
            "json_text": {
                "name": "Test"
            },
            "schema_text": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            }
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertTrue(data.get('data', {}).get('is_valid'))

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/json_schema_validator_demo', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertIn(data.get('error', {}).get('code'), ['VALIDATION_ERROR', 'BAD_REQUEST'])

    def test_invalid_input(self):
        """Test with input that violates the schema."""
        response = self.client.post('/api/minimal-solutions/json_schema_validator_demo', json={
            "json_text": {
                "name": 123
            },
            "schema_text": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            }
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertFalse(data.get('data', {}).get('is_valid'))
        self.assertGreater(len(data.get('data', {}).get('errors', [])), 0)

if __name__ == '__main__':
    unittest.main()
