from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.hosting_merger.validation_hosting_merger import validate_hosting_merger_request

api_bp = Blueprint('hosting_merger_api', __name__)

@api_bp.route('/api/minimal-solutions/hosting_merger', methods=['POST'])
def handle_hosting_merger_request():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_hosting_merger_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors,
            status_code=400
        )

    source = data.get("source")
    config = data.get("config", {})
    mode = data.get("mode")

    result_data = {
        "source": source,
        "config": config,
        "mode": mode,
        "merged": True,
        "status": "success",
        "message": f"Hosting erfolgreich zusammengeführt im Modus '{mode}'."
    }

    return success_response(data=result_data)
