from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.minecraft_converter.validation_minecraft_converter import validate_minecraft_converter_request

api_bp = Blueprint('minecraft_converter_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_converter', methods=['POST'])
def handle_minecraft_converter_request():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_minecraft_converter_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors,
            status_code=400
        )

    input_text = data.get("input_text")
    mode = data.get("mode")
    options = data.get("options", {})

    # Simulate converter result
    result_data = {
        "input_text": input_text,
        "mode": mode,
        "options": options,
        "status": "success",
        "message": f"Minecraft Converter request successfully processed for mode '{mode}'.",
        "result": {
            "converted_text": f"// Converted text for mode {mode}:\n{input_text}",
            "blocks_converted": len(input_text),
            "warnings": []
        }
    }

    return success_response(data=result_data)
