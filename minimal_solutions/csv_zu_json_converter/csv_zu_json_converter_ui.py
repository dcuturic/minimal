from flask import Blueprint
import os

ui_bp = Blueprint('csv_zu_json_converter_ui', __name__)

@ui_bp.route('/minimal-solutions/csv_zu_json_converter')
def ui_endpoint():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "CSV zu JSON Converter UI - demo.html not found"
