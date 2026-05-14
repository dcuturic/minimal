from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.seo_checker.seo_checker_validation import validate_seo_checker_request

api_bp = Blueprint('seo_checker_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_checker', methods=['POST'])
def handle_seo_checker_request():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_seo_checker_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get("topic", "")
    target = data.get("target", "")
    options = data.get("options", {})

    result = {
        "score": 85,
        "feedback": f"SEO Check für Thema '{topic}' auf Ziel '{target}' erfolgreich.",
        "details": {
            "topic_used": topic,
            "target_used": target,
            "options_applied": options
        }
    }

    return success_response(data=result)
