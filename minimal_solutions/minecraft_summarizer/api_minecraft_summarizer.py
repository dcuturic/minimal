from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.minecraft_summarizer.validation_minecraft_summarizer import validate_minecraft_summarizer_request

api_bp = Blueprint('minecraft_summarizer_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_summarizer', methods=['POST'])
def handle_minecraft_summarizer_request():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_minecraft_summarizer_request(data)
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

    # Simulate summarizer result
    result_data = {
        "input_text": input_text,
        "mode": mode,
        "options": options,
        "status": "success",
        "message": f"Minecraft Summarizer request successfully processed for mode '{mode}'.",
        "result": {
            "summary_text": f"// Summary for mode {mode}:\n{input_text[:50]}...",
            "words_analyzed": len(input_text.split()),
            "warnings": []
        }
    }

    return success_response(data=result_data)
