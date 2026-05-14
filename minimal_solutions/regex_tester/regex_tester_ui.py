from flask import Blueprint
import os

ui_bp = Blueprint('regex_tester_ui', __name__)

@ui_bp.route('/minimal-solutions/regex_tester/demo')
def ui_endpoint():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Regex Tester UI - demo.html not found"
