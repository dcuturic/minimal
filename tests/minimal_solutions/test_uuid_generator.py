import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.uuid_generator.uuid_generator_api import api_bp

class TestUUIDGenerator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/uuid_generator', json={
            "count": 5,
            "version": 4
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('uuids', data.get('data', {}))
        self.assertEqual(len(data['data']['uuids']), 5)
        
        # Test UUID v1
        response_v1 = self.client.post('/api/minimal-solutions/uuid_generator', json={
            "count": 2,
            "version": 1
        })
        self.assertEqual(response_v1.status_code, 200)
        data_v1 = json.loads(response_v1.data)
        self.assertTrue(data_v1.get('success'))
        self.assertEqual(len(data_v1['data']['uuids']), 2)

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/uuid_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('count', details)
        self.assertIn('version', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/uuid_generator', json={
            "count": -1,
            "version": 500
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('count', details)
        self.assertIn('version', details)
        
        # Test invalid type
        response_type = self.client.post('/api/minimal-solutions/uuid_generator', json={
            "count": "five",
            "version": "four"
        })
        self.assertEqual(response_type.status_code, 400)
        data_type = json.loads(response_type.data)
        details_type = data_type.get('error', {}).get('details', {})
        self.assertIn('count', details_type)
        self.assertIn('version', details_type)

if __name__ == '__main__':
    unittest.main()
