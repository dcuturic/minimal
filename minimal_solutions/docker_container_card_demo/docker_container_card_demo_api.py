from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.docker_container_card_demo.docker_container_card_demo_validation import validate_docker_card_request

api_bp = Blueprint('docker_container_card_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/docker_container_card_demo', methods=['POST'])
def generate_card():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_docker_card_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    name = data.get('name')
    status = data.get('status')
    image = data.get('image')
    ports = data.get('ports')

    return success_response(data={
        "name": name,
        "status": status,
        "image": image,
        "ports": ports
    })
