import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.docker_container_card_demo.docker_container_card_demo_api import api_bp

class TestDockerContainerCardDemo(unittest.TestCase):
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
        response = self.client.post('/api/minimal-solutions/docker_container_card_demo', json={
            "name": "crafthoster-web",
            "status": "running",
            "image": "nginx:alpine",
            "ports": "80:80, 443:443"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertIn('data', data)
        self.assertEqual(data['data']['name'], 'crafthoster-web')
        self.assertEqual(data['data']['status'], 'running')
        self.assertEqual(data['data']['image'], 'nginx:alpine')
        self.assertEqual(data['data']['ports'], '80:80, 443:443')

    def test_empty_input(self):
        """Test with empty input and expect handled error."""
        response = self.client.post('/api/minimal-solutions/docker_container_card_demo', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        self.assertIn('name', details)
        self.assertIn('status', details)
        self.assertIn('image', details)
        self.assertIn('ports', details)

    def test_invalid_input(self):
        """Test with invalid input (wrong types) and expect validation error response."""
        response = self.client.post('/api/minimal-solutions/docker_container_card_demo', json={
            "name": 123,
            "status": 456,
            "image": True,
            "ports": None
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(data.get('error', {}).get('code'), 'VALIDATION_ERROR')
        details = data.get('error', {}).get('details', {})
        # Name should be invalid type
        self.assertIn('name', details)

if __name__ == '__main__':
    unittest.main()
