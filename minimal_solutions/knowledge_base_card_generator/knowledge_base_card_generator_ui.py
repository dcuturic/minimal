from flask import Blueprint
import os

ui_bp = Blueprint('knowledge_base_card_generator_ui', __name__)

@ui_bp.route('/minimal-solutions/knowledge_base_card_generator/demo')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'knowledge_base_card_generator_component.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "UI Component Missing"
