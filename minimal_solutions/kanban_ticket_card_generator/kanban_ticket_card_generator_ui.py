from flask import Blueprint
import os

ui_bp = Blueprint('kanban_ticket_card_generator_ui', __name__)

@ui_bp.route('/minimal-solutions/kanban_ticket_card_generator')
def demo():
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            return f.read()
    return "Demo UI for kanban_ticket_card_generator"
