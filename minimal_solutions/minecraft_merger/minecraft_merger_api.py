"""
API for Minecraft Merger
"""
from flask import Blueprint, jsonify, request

minecraft_merger_api = Blueprint('minecraft_merger_api', __name__)

@minecraft_merger_api.route('/api/minimal-solutions/minecraft_merger', methods=['POST'])
def process_request():
    return jsonify({"status": "success", "message": "Minecraft Merger API ready"})
