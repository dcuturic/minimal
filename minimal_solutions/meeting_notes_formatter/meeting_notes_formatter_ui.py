from flask import Blueprint

ui_bp = Blueprint('meeting_notes_formatter_ui', __name__)

@ui_bp.route('/minimal-solutions/meeting_notes_formatter')
def index():
    import os
    html_path = os.path.join(os.path.dirname(__file__), 'demo.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            return f.read()
    return "Demo UI for meeting_notes_formatter"
