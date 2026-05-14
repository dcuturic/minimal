from flask import Blueprint
import os

ui_bp = Blueprint('task_breakdown_generator_ui', __name__)

@ui_bp.route('/minimal-solutions/task_breakdown_generator')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            return f.read()
    return "Demo UI for task_breakdown_generator"
