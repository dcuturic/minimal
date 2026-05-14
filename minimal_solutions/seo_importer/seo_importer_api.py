from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.seo_importer.seo_importer_validation import validate_seo_importer_request

api_bp = Blueprint('seo_importer_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_importer', methods=['POST'])
def handle_seo_importer_request():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_seo_importer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors,
            status_code=400
        )

    topic = data.get("topic")
    target = data.get("target")
    options = data.get("options", [])

    # Mock behavior for the minimal solution
    result_data = {
        "topic": topic,
        "target": target,
        "options": options,
        "import_status": "success",
        "imported_items": 42,
        "message": f"Daten für '{topic}' erfolgreich importiert."
    }

    return success_response(data=result_data)
