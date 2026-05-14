from flask import Blueprint
import os

ui_bp = Blueprint('jwt_decoder_demo_ui', __name__)

@ui_bp.route('/minimal-solutions/jwt_decoder_demo/demo')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            return f.read()
    return "Demo UI for jwt_decoder_demo"
