import unittest
import json
import os
import sys

# Füge das Hauptverzeichnis zum PYTHONPATH hinzu
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app import create_app
from minimal_solutions.border_radius_generator.border_radius_generator_api import api_bp

class TestBorderRadiusGenerator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        try:
            self.app.register_blueprint(api_bp)
        except Exception:
            pass
        self.client = self.app.test_client()

    def test_happy_path(self):
        payload = {
            "top_left": 10,
            "top_right": 20,
            "bottom_right": 30,
            "bottom_left": 40
        }
        response = self.client.post('/api/minimal-solutions/border_radius_generator', json=payload)
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["data"]["css"], "10px 20px 30px 40px")

    def test_empty_input(self):
        response = self.client.post('/api/minimal-solutions/border_radius_generator', json={})
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["status"], "error")
        self.assertIn("top_left", data["details"])
        self.assertIn("top_right", data["details"])
        self.assertIn("bottom_right", data["details"])
        self.assertIn("bottom_left", data["details"])

    def test_invalid_input_type(self):
        payload = {
            "top_left": "abc",
            "top_right": 20,
            "bottom_right": 30,
            "bottom_left": 40
        }
        response = self.client.post('/api/minimal-solutions/border_radius_generator', json=payload)
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["status"], "error")
        self.assertIn("top_left", data["details"])

    def test_invalid_input_negative(self):
        payload = {
            "top_left": -10,
            "top_right": 20,
            "bottom_right": 30,
            "bottom_left": 40
        }
        response = self.client.post('/api/minimal-solutions/border_radius_generator', json=payload)
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["status"], "error")
        self.assertIn("top_left", data["details"])
        self.assertTrue(any("nicht negativ sein" in err for err in data["details"]["top_left"]))

if __name__ == '__main__':
    unittest.main()
