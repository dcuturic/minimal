from flask import Blueprint
import os

ui_bp = Blueprint('word_replacer_ui', __name__)

@ui_bp.route('/minimal-solutions/word_replacer/demo')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Demo UI for Word Replacer"
