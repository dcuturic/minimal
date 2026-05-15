from flask import Blueprint
import os

ui_bp = Blueprint('minecraft_analyzer_ui', __name__)

@ui_bp.route('/minimal-solutions/minecraft_analyzer', methods=['GET'])
def index():
    html_path = os.path.join(os.path.dirname(__file__), 'ui_minecraft_analyzer.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Demo UI for Minecraft Analyzer"
