import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.json_zu_csv_converter.json_zu_csv_converter_api import api_bp

class TestJsonZuCsvConverter(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/json_zu_csv_converter', json={
            "json_text": '[{"name": "Danijel", "age": 30}, {"name": "Alice", "age": 25}]',
            "delimiter": ","
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('csv_data', data.get('data', {}))
        self.assertIn('name,age', data['data']['csv_data'])
        self.assertIn('Danijel,30', data['data']['csv_data'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/json_zu_csv_converter', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('json_text', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Invalid json_text format (not string)
        response = self.client.post('/api/minimal-solutions/json_zu_csv_converter', json={
            "json_text": 123
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('json_text', details)

        # Invalid delimiter length
        response2 = self.client.post('/api/minimal-solutions/json_zu_csv_converter', json={
            "json_text": "[]",
            "delimiter": ",,"
        })
        self.assertEqual(response2.status_code, 400)
        data2 = json.loads(response2.data)
        self.assertFalse(data2.get('success'))
        self.assertEqual(data2.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details2 = data2.get('error', {}).get('details', {})
        self.assertIn('delimiter', details2)
        
        # Invalid json format (not parsable JSON)
        response3 = self.client.post('/api/minimal-solutions/json_zu_csv_converter', json={
            "json_text": "invalid_json"
        })
        self.assertEqual(response3.status_code, 400)
        data3 = json.loads(response3.data)
        self.assertFalse(data3.get('success'))
        self.assertEqual(data3.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details3 = data3.get('error', {}).get('details', {})
        self.assertIn('json_text', details3)

if __name__ == '__main__':
    unittest.main()
