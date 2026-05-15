from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.minecraft_analyzer.validation_minecraft_analyzer import validate_minecraft_analyzer_request

api_bp = Blueprint('minecraft_analyzer_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_analyzer', methods=['POST'])
def handle_minecraft_analyzer_request():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_minecraft_analyzer_request(data)
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

    # Simulate analyzer result
    result_data = {
        "input_text": input_text,
        "mode": mode,
        "options": options,
        "status": "success",
        "message": f"Minecraft Analyzer request successfully processed for mode '{mode}'.",
        "result": {
            "analyzed_text": f"// Analyzed text for mode {mode}:\n{input_text}",
            "blocks_analyzed": len(input_text),
            "warnings": []
        }
    }

    return success_response(data=result_data)
