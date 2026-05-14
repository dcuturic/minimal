from flask import Blueprint, render_template

ui_bp = Blueprint('hosting_diff_viewer_ui', __name__)

@ui_bp.route('/minimal-solutions/hosting_diff_viewer', methods=['GET'])
def index():
    pass
