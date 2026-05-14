from flask import Blueprint
import os

ui_bp = Blueprint('impressum_generator_demo_ui', __name__)

@ui_bp.route('/minimal-solutions/impressum_generator_demo/demo')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            return f.read()
    return "Demo UI for Impressum Generator Demo"
