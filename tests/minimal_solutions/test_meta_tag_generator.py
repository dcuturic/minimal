import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.meta_tag_generator.meta_tag_generator_api import api_bp

class TestMetaTagGenerator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()
        self.endpoint = '/api/minimal-solutions/meta_tag_generator'

    def test_happy_path(self):
        """Testet die erfolgreiche Generierung von Meta Tags mit gültigen Daten."""
        payload = {
            "title": "Test Title",
            "description": "Test Description",
            "image_url": "https://example.com/image.jpg",
            "page_url": "https://example.com"
        }
        response = self.client.post(
            self.endpoint,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get("status"), "success")
        html_output = data.get("data", {}).get("html", "")
        self.assertIn("<title>Test Title</title>", html_output)
        self.assertIn('content="Test Description"', html_output)

    def test_empty_input(self):
        """Testet das Verhalten bei komplett fehlendem oder leerem Input."""
        # Weder title noch description
        response = self.client.post(
            self.endpoint,
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data.get("status"), "error")
        self.assertIn("Mindestens 'title' oder 'description'", str(data.get("details", [])))

    def test_invalid_input(self):
        """Testet das Verhalten bei fehlerhaftem Input (falsche Typen)."""
        payload = {
            "title": 123,
            "description": ["liste"]
        }
        response = self.client.post(
            self.endpoint,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data.get("status"), "error")
        details = str(data.get("details", []))
        self.assertIn("'title' muss ein String sein", details)
        self.assertIn("'description' muss ein String sein", details)

if __name__ == '__main__':
    unittest.main()
