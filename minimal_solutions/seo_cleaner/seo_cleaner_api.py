from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.seo_cleaner.seo_cleaner_validation import validate_seo_cleaner_request

api_bp = Blueprint('seo_cleaner_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_cleaner', methods=['POST'])
def handle_seo_cleaner_request():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_seo_cleaner_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors,
            status_code=400
        )

    topic = data.get("topic")
    target = data.get("target")
    options = data.get("options", {})

    # Mock behavior for the minimal solution
    result_data = {
        "topic": topic,
        "target": target,
        "options": options,
        "clean_status": "success",
        "clean_items": 5,
        "message": f"Daten für '{topic}' erfolgreich bereinigt."
    }

    return success_response(data=result_data)
