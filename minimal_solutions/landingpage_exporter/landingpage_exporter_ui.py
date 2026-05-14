from flask import Blueprint
import os

ui_bp = Blueprint('landingpage_exporter_ui', __name__)

@ui_bp.route('/minimal-solutions/landingpage_exporter/demo')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'landingpage_exporter_component.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            return f.read()
    return "Demo UI for landingpage_exporter"
