import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.csv_zu_json_converter.csv_zu_json_converter_api import api_bp

class TestCsvZuJsonConverter(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/csv_zu_json_converter', json={
            "csv_text": "id,name,age\n1,Alice,30\n2,Bob,25",
            "delimiter": ",",
            "has_header": True
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('json_data', data.get('data', {}))
        self.assertEqual(data['data']['parsed_count'], 2)
        self.assertEqual(len(data['data']['json_data']), 2)
        self.assertEqual(data['data']['json_data'][0]['name'], 'Alice')

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/csv_zu_json_converter', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('csv_text', details)
        self.assertIn('delimiter', details)
        self.assertIn('has_header', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/csv_zu_json_converter', json={
            "csv_text": 12345,  # Invalid type (should be string)
            "delimiter": ",",
            "has_header": True
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('csv_text', details)

if __name__ == '__main__':
    unittest.main()
