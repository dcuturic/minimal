# API for Hosting Template Builder
from flask import Blueprint, jsonify, request

api_hosting_template_builder_bp = Blueprint('api_hosting_template_builder', __name__)

@api_hosting_template_builder_bp.route('/api/minimal-solutions/hosting_template_builder', methods=['POST'])
def process():
    return jsonify({"status": "success"})
