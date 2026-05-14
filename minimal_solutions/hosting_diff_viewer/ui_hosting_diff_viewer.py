from flask import Blueprint
import os

ui_bp = Blueprint('hosting_diff_viewer_ui', __name__)

@ui_bp.route('/minimal-solutions/hosting_diff_viewer', methods=['GET'])
def index():
    html_path = os.path.join(os.path.dirname(__file__), 'ui_hosting_diff_viewer.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Demo UI for Hosting Diff Viewer"
