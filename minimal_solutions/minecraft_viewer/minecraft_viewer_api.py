from flask import Blueprint, jsonify, request

api_bp = Blueprint('minecraft_viewer_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_viewer', methods=['POST'])
def process():
    data = request.get_json()
    return jsonify({"status": "success", "message": "Minecraft Viewer API ready"})
