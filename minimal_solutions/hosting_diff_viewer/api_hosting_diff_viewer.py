from flask import Blueprint, request

api_bp = Blueprint('hosting_diff_viewer_api', __name__)

@api_bp.route('/api/minimal-solutions/hosting_diff_viewer', methods=['POST'])
def handle_request():
    pass
