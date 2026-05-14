from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .validation_hosting_builder import validate_hosting_builder_request

api_bp = Blueprint('hosting_builder_api', __name__)

@api_bp.route("/api/minimal-solutions/hosting_builder", methods=['POST'])
def hosting_builder_endpoint():
    data = request.get_json(silent=True) or {}

    is_valid, errors = validate_hosting_builder_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    source = data.get("source")
    config = data.get("config")
    mode = data.get("mode")

    result = {
        "source": source,
        "config": config,
        "mode": mode,
        "status": "builder_ready",
        "message": "Hosting successfully built."
    }

    return success_response(data=result)
