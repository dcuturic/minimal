from flask import Blueprint
import os

ui_bp = Blueprint('decision_log_generator_ui', __name__)

@ui_bp.route('/minimal-solutions/decision_log_generator')
def index():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            return f.read()
    return "Demo UI for decision_log_generator"
