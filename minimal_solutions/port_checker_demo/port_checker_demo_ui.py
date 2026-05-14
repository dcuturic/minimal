from flask import Blueprint
import os

ui_bp = Blueprint('port_checker_demo_ui', __name__)

@ui_bp.route('/minimal-solutions/port_checker_demo/demo')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'port_checker_demo_component.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "UI Component Missing"
