import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.knowledge_base_card_generator.knowledge_base_card_generator_api import api_bp

class TestKnowledgeBaseCardGenerator(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/knowledge_base_card_generator', json={
            "source_text": "Dies ist ein längerer Text, der als Wissensbasisartikel fungieren soll. Er enthält wichtige Informationen über ein bestimmtes Thema, das für unsere Benutzer von Interesse ist.",
            "category": "Allgemein"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('data', data)
        result_data = data['data']
        self.assertIn('card', result_data)
        self.assertIn('title', result_data['card'])
        self.assertIn('summary', result_data['card'])
        self.assertIn('category', result_data['card'])
        self.assertIn('key_points', result_data['card'])

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/knowledge_base_card_generator', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('source_text', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Invalid source_text format/type
        response = self.client.post('/api/minimal-solutions/knowledge_base_card_generator', json={
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
