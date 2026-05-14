from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.port_checker_demo.port_checker_demo_validation import validate_port_checker_request
import socket

api_bp = Blueprint('port_checker_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/port_checker_demo', methods=['POST'])
def check_port():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_port_checker_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    host = data.get('host').strip()
    port = data.get('port')

    is_open = False
    try:
        # socket.create_connection is a convenient way to check
        # use a short timeout so we don't hang the request
        with socket.create_connection((host, port), timeout=2.0):
            is_open = True
    except (socket.timeout, socket.error, OSError):
        is_open = False

    return success_response(data={"host": host, "port": port, "is_open": is_open})
