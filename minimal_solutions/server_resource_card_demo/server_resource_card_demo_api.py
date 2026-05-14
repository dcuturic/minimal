from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.server_resource_card_demo.server_resource_card_demo_validation import validate_resource_request

api_bp = Blueprint('server_resource_card_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/server_resource_card_demo', methods=['POST'])
def generate_card():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_resource_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    cpu = float(data.get('cpu'))
    ram = float(data.get('ram'))
    disk = float(data.get('disk'))

    def get_status(val):
        if val >= 90:
            return "danger"
        if val >= 75:
            return "warning"
        return "normal"

    return success_response(data={
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "status": {
            "cpu": get_status(cpu),
            "ram": get_status(ram),
            "disk": get_status(disk)
        }
    })
