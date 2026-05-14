from flask import Blueprint
import os

ui_bp = Blueprint('hosting_mapper_ui', __name__)

@ui_bp.route('/minimal-solutions/hosting_mapper/demo')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'ui_hosting_mapper.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Demo UI for Hosting Mapper"
