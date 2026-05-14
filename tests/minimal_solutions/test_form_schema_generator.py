import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.form_schema_generator.form_schema_generator_api import api_bp

class TestFormSchemaGenerator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/form_schema_generator', json={
            "fields": [
                {"name": "username", "type": "string", "required": True},
                {"name": "age", "type": "number"}
            ]
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('schema', data.get('data', {}))
        schema = data['data']['schema']
        self.assertEqual(schema['type'], 'object')
        self.assertIn('username', schema['properties'])
        self.assertIn('age', schema['properties'])
        self.assertIn('username', schema['required'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/form_schema_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', [])
        self.assertTrue(any("Missing required field: 'fields'" in err for err in details))

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/form_schema_generator', json={
            "fields": "not a list"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', [])
        self.assertTrue(any("'fields' must be a list" in err for err in details))
        
        # Test invalid field missing type
        response_field = self.client.post('/api/minimal-solutions/form_schema_generator', json={
            "fields": [
                {"name": "test"} 
            ]
        })
        self.assertEqual(response_field.status_code, 400)
        data_field = json.loads(response_field.data)
        details_field = data_field.get('error', {}).get('details', [])
        self.assertTrue(any("missing 'type'" in err for err in details_field))

if __name__ == '__main__':
    unittest.main()
