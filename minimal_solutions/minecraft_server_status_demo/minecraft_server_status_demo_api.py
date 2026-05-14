from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.minecraft_server_status_demo.minecraft_server_status_demo_validation import validate_mc_status_request

api_bp = Blueprint('minecraft_server_status_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_server_status_demo', methods=['POST'])
def check_status():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_mc_status_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    host = data.get('host')
    port = data.get('port')

    # Mock response for demo purposes
    return success_response(data={
        "host": host,
        "port": port,
        "online": True,
        "players_online": 35000,
        "players_max": 100000,
        "version": "1.20.1",
        "motd": "A Minecraft Server"
    })
