import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.base64_encoder_decoder.base64_encoder_decoder_api import api_bp

class TestBase64EncoderDecoder(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        # Registriere die API-Blueprint für den Test, falls noch nicht geschehen
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass # Blueprint wurde möglicherweise schon registriert
        self.client = self.app.test_client()

    def test_happy_path_encode(self):
        """Test with valid input and expect a success response for encoding."""
        response = self.client.post('/api/minimal-solutions/base64_encoder_decoder', json={
            "text": "CraftHoster",
            "mode": "encode"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('result', data.get('data', {}))
        self.assertEqual(data['data']['result'], 'Q3JhZnRIb3N0ZXI=')

    def test_happy_path_decode(self):
        """Test with valid input and expect a success response for decoding."""
        response = self.client.post('/api/minimal-solutions/base64_encoder_decoder', json={
            "text": "Q3JhZnRIb3N0ZXI=",
            "mode": "decode"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('result', data.get('data', {}))
        self.assertEqual(data['data']['result'], 'CraftHoster')

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/base64_encoder_decoder', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('text', details)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # Invalid base64 decode input
        response = self.client.post('/api/minimal-solutions/base64_encoder_decoder', json={
            "text": "invalid_base64!@#",
            "mode": "decode"
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('text', details)

if __name__ == '__main__':
    unittest.main()
