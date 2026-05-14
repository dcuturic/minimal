import unittest
import json
import os
import sys
import datetime

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.sitemap_xml_generator.sitemap_xml_generator_api import api_bp

class TestSitemapXmlGenerator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()
        self.endpoint = '/api/minimal-solutions/sitemap_xml_generator'

    def test_happy_path(self):
        """Happy-Path Test existiert."""
        payload = {
            "urls": "https://example.com/\nhttps://example.com/about\nhttps://example.com/contact",
            "changefreq": "monthly",
            "priority": "0.8"
        }
        response = self.client.post(
            self.endpoint,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get("status"), "success")
        
        result = data.get("data", {}).get("result", "")
        self.assertIn('<?xml version="1.0" encoding="UTF-8"?>', result)
        self.assertIn('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', result)
        self.assertIn('<loc>https://example.com/</loc>', result)
        self.assertIn('<loc>https://example.com/about</loc>', result)
        self.assertIn('<loc>https://example.com/contact</loc>', result)
        self.assertIn('<changefreq>monthly</changefreq>', result)
        self.assertIn('<priority>0.8</priority>', result)

        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        self.assertIn(f'<lastmod>{current_date}</lastmod>', result)

    def test_empty_input(self):
        """Empty-Input Test existiert."""
        response = self.client.post(
            self.endpoint,
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get("status"), "success")
        
        result = data.get("data", {}).get("result", "")
        self.assertIn('<?xml version="1.0" encoding="UTF-8"?>', result)
        self.assertIn('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', result)
        self.assertIn('</urlset>', result)
        self.assertNotIn('<url>', result)

    def test_invalid_input(self):
        """Invalid-Input Test existiert."""
        payload = {
            "urls": 12345, # Invalid type
            "changefreq": 123, # Invalid type
            "priority": [] # Invalid type
        }
        response = self.client.post(
            self.endpoint,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data.get("status"), "error")
        details = str(data.get("details", {}))
        self.assertIn("urls", details)
        self.assertIn("changefreq", details)
        self.assertIn("priority", details)

if __name__ == '__main__':
    unittest.main()
