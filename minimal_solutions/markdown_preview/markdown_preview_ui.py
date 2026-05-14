from flask import Blueprint
import os

ui_bp = Blueprint('markdown_preview_ui', __name__)

@ui_bp.route('/minimal-solutions/markdown_preview/demo')
def ui_endpoint():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Markdown Preview UI - demo.html not found"
