from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.minecraft_generator.validation_minecraft_generator import validate_minecraft_generator_request

api_bp = Blueprint('minecraft_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_generator', methods=['POST'])
def handle_request():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_minecraft_generator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors,
            status_code=400
        )

    input_text = data.get("input_text")
    options = data.get("options", {})
    mode = data.get("mode")

    # Mock functionality for Minecraft Generator
    result_data = {
        "input_text": input_text,
        "options": options,
        "mode": mode,
        "generated": True,
        "status": "success",
        "message": f"Minecraft Generator erfolgreich ausgeführt im Modus '{mode}'."
    }

    return success_response(data=result_data)
