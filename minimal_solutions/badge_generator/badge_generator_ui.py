from flask import Blueprint
import os

ui_bp = Blueprint('badge_generator_ui', __name__)

@ui_bp.route('/minimal-solutions/badge_generator/demo')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Demo UI for Badge Generator"
