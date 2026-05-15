from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.minecraft_viewer.minecraft_viewer_validation import validate_minecraft_viewer_request

api_bp = Blueprint('minecraft_viewer_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_viewer', methods=['POST'])
def process():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_minecraft_viewer_request(data)
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

    # Simulate viewer result
    result_data = {
        "input_text": input_text,
        "mode": mode,
        "options": options,
        "status": "success",
        "message": f"Minecraft Viewer request successfully processed for mode '{mode}'.",
        "result": {
            "viewer_status": "ready",
            "items_found": 1,
            "details": f"Viewed '{input_text[:50]}...' in mode '{mode}'."
        }
    }

    return success_response(data=result_data)
