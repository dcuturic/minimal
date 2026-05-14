import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.risk_matrix_generator.risk_matrix_generator_api import api_bp

class TestRiskMatrixGenerator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        response = self.client.post('/api/minimal-solutions/risk_matrix_generator', json={
            "risks": [
                {"name": "Server Outage", "probability": "Low", "impact": "High"},
                {"name": "Data Breach", "probability": "Medium", "impact": "High"}
            ]
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('matrix', data.get('data', {}))
        self.assertIn('Server Outage', data['data']['matrix'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/risk_matrix_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('risks', details)

    def test_invalid_input(self):
        """Test with invalid input (empty list) and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/risk_matrix_generator', json={
            "risks": []
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('risks', details)

if __name__ == '__main__':
    unittest.main()
