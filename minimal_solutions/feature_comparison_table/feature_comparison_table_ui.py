from flask import Blueprint
import os

ui_bp = Blueprint('feature_comparison_table_ui', __name__)

@ui_bp.route('/minimal-solutions/feature_comparison_table')
def index():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            return f.read()
    return "Demo UI for feature_comparison_table"
