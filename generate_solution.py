import os
import sys
import json

def generate_solution(identify):
    base_dir = f"minimal_solutions/{identify}"
    test_dir = "tests/minimal_solutions"
    
    if os.path.exists(base_dir):
        print(f"Error: Solution '{identify}' already exists at {base_dir}. Aborting to prevent overwrite.")
        sys.exit(1)
        
    # Create directories
    os.makedirs(base_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    
    # 1. __init__.py
    init_content = f"# Initialization for {identify}\n"
    with open(os.path.join(base_dir, "__init__.py"), "w") as f:
        f.write(init_content)
        
    # 2. api.py
    api_content = f'''from flask import Blueprint, jsonify
from app.responses import success_response, error_response

api_bp = Blueprint('{identify}_api', __name__)

@api_bp.route('/api/minimal-solutions/{identify}', methods=['GET'])
def get_data():
    return success_response(data={{"message": "API for {identify} is working."}})
'''
    with open(os.path.join(base_dir, "api.py"), "w") as f:
        f.write(api_content)
        
    # 3. ui.py
    ui_content = f'''from flask import Blueprint, render_template

ui_bp = Blueprint('{identify}_ui', __name__)

@ui_bp.route('/minimal-solutions/{identify}/demo')
def demo():
    return "Demo UI for {identify}"
'''
    with open(os.path.join(base_dir, "ui.py"), "w") as f:
        f.write(ui_content)
        
    # 4. README.md
    readme_content = f'''# {identify}

## Overview
Minimal solution for {identify}.

## API Endpoint
`/api/minimal-solutions/{identify}`

## UI Route
`/minimal-solutions/{identify}`

## Tests
Tests for this solution follow the global test pattern:
- **Happy-Path**
- **Empty-Input**
- **Invalid-Input**
'''
    with open(os.path.join(base_dir, "README.md"), "w") as f:
        f.write(readme_content)
        
    # 5. demo_data.json
    demo_data_content = json.dumps({"example_key": "example_value", "identify": identify}, indent=4)
    with open(os.path.join(base_dir, "demo_data.json"), "w") as f:
        f.write(demo_data_content)
        
    # 6. Test file
    test_content = f'''import unittest
import json

class Test{identify.replace('_', ' ').title().replace(' ', '')}(unittest.TestCase):
    def setUp(self):
        # Prepare test client or state here
        pass

    def test_happy_path(self):
        """Test with valid input and expect a success response."""
        # e.g., response = self.client.post('/api/minimal-solutions/{identify}', json={{"valid": "data"}})
        # self.assertEqual(response.status_code, 200)
        self.assertTrue(True)

    def test_empty_input(self):
        """Test with empty input and expect handled error or default."""
        # e.g., response = self.client.post('/api/minimal-solutions/{identify}', json={{}})
        # self.assertEqual(response.status_code, 400)
        self.assertTrue(True)

    def test_invalid_input(self):
        """Test with invalid input and expect validation error response."""
        # e.g., response = self.client.post('/api/minimal-solutions/{identify}', json={{"invalid": "data"}})
        # self.assertEqual(response.status_code, 400)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
'''
    with open(os.path.join(test_dir, f"test_{identify}.py"), "w") as f:
        f.write(test_content)
        
    print(f"Successfully generated standard files and folders for '{identify}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_solution.py <identify>")
        sys.exit(1)
    
    identify = sys.argv[1]
    generate_solution(identify)
