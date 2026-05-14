from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.seo_viewer.seo_viewer_validation import validate_seo_viewer_request

api_bp = Blueprint('seo_viewer_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_viewer', methods=['POST'])
def handle_seo_viewer_request():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_seo_viewer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get("topic", "")
    target = data.get("target", "")
    options = data.get("options", {})

    view_data = {
        "title": f"SEO View für {topic}",
        "target_audience": target,
        "metrics": {
            "visibility_score": 85,
            "keyword_density": "2.5%",
            "readability_index": "Gut"
        },
        "recommendations": [
            "Füge mehr interne Links hinzu.",
            "Optimiere die Meta-Description."
        ]
    }

    return success_response(data={
        "view": view_data,
        "topic": topic,
        "target": target,
        "options": options
    })
