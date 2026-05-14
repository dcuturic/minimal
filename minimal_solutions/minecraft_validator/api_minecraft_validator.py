from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.minecraft_validator.validation_minecraft_validator import validate_minecraft_validator_request

api_bp = Blueprint('minecraft_validator_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_validator', methods=['POST'])
def handle_request():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_minecraft_validator_request(data)
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

    # Mock functionality for Minecraft Validator
    is_valid_result = True
    validation_message = f"Minecraft Name/Input '{input_text}' ist gültig für Modus '{mode}'."
    
    # Simple check for demo purposes
    if "invalid" in input_text.lower():
        is_valid_result = False
        validation_message = f"Minecraft Name/Input '{input_text}' ist ungültig für Modus '{mode}'."

    result_data = {
        "input_text": input_text,
        "options": options,
        "mode": mode,
        "is_valid": is_valid_result,
        "status": "success",
        "message": validation_message
    }

    return success_response(data=result_data)
