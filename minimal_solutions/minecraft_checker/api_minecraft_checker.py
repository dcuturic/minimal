from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.minecraft_checker.minecraft_checker_validation import validate_minecraft_checker_request

api_bp = Blueprint('minecraft_checker_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_checker', methods=['POST'])
def handle_minecraft_checker_request():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_minecraft_checker_request(data)
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

    # Simulate checker result
    result_data = {
        "input_text": input_text,
        "mode": mode,
        "options": options,
        "status": "success",
        "message": f"Minecraft Checker request successfully processed for mode '{mode}'.",
        "result": {
            "check_status": "passed",
            "issues_found": 0,
            "details": f"Checked '{input_text[:50]}...' in mode '{mode}'. No issues found."
        }
    }

    return success_response(data=result_data)
