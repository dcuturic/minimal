from flask import Blueprint
import os

ui_bp = Blueprint('hosting_template_builder_ui', __name__)

@ui_bp.route('/minimal-solutions/hosting_template_builder')
def ui():
    html_path = os.path.join(os.path.dirname(__file__), 'ui_hosting_template_builder.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "UI for Hosting Template Builder"
