from flask import Blueprint
import os

ui_bp = Blueprint('landingpage_diff_viewer_ui', __name__)

@ui_bp.route('/minimal-solutions/landingpage_diff_viewer/demo')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            return f.read()
    return "Demo UI for landingpage_diff_viewer"

@ui_bp.route('/minimal-solutions/landingpage_diff_viewer')
def ui():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            return f.read()
    return "UI for landingpage_diff_viewer"
