from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .validation_hosting_preview import validate_hosting_preview_request

api_bp = Blueprint('hosting_preview_api', __name__)

@api_bp.route("/api/minimal-solutions/hosting_preview", methods=['POST'])
def hosting_preview_endpoint():
    data = request.get_json(silent=True) or {}

    is_valid, errors = validate_hosting_preview_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    source = data.get("source")
    config = data.get("config", "")
    mode = data.get("mode", "default")

    result = {
        "source": source,
        "config": config,
        "mode": mode,
        "status": "preview_ready",
        "message": "Hosting successfully previewed."
    }

    return success_response(data=result)
