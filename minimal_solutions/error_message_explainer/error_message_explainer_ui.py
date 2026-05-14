from flask import Blueprint
import os

ui_bp = Blueprint('error_message_explainer_ui', __name__)

@ui_bp.route('/minimal-solutions/error_message_explainer/demo')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'error_message_explainer_component.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "UI Component Missing"
