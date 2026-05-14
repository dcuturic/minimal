from flask import Blueprint, jsonify
import os

ui_bp = Blueprint('ssl_expiry_checker_demo_ui', __name__)

@ui_bp.route('/minimal-solutions/ssl_expiry_checker_demo/demo')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            return f.read()
    return "Demo UI for SSL Expiry Checker Demo"
