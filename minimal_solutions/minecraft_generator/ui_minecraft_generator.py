from flask import Blueprint
import os

ui_bp = Blueprint('minecraft_generator_ui', __name__)

@ui_bp.route('/minimal-solutions/minecraft_generator', methods=['GET'])
def index():
    html_path = os.path.join(os.path.dirname(__file__), 'ui_minecraft_generator.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Demo UI for Minecraft Generator"
