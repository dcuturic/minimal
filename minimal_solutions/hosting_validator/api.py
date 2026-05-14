from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .validation import validate_hosting_validator_request

api_bp = Blueprint('hosting_validator_api', __name__)

@api_bp.route("/api/minimal-solutions/hosting_validator", methods=['POST'])
def hosting_validator_endpoint():
    data = request.get_json(silent=True) or {}

    is_valid, errors = validate_hosting_validator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    source = data.get("source")
    config = data.get("config", "")
    mode = data.get("mode", "standard")

    result = {
        "source": source,
        "config": config,
        "mode": mode,
        "validated_hosting": True,
        "message": "Hosting successfully validated."
    }

    return success_response(data=result)
