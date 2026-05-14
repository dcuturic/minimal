import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.faq_generator.faq_generator_api import api_bp

class TestFaqGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/faq_generator', json={
            "source_text": "Python is a high-level programming language. Its design philosophy emphasizes code readability.",
            "count": 2
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('data', data)
        result_data = data['data']
        self.assertIn('faqs', result_data)
        self.assertIsInstance(result_data['faqs'], list)
        self.assertGreater(len(result_data['faqs']), 0)

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/faq_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('source_text', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Invalid source_text format/type
        response = self.client.post('/api/minimal-solutions/faq_generator', json={
            "source_text": 12345
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('source_text', details)

if __name__ == '__main__':
    unittest.main()
