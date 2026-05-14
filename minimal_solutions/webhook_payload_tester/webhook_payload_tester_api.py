import json
from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .webhook_payload_tester_validation import validate_request

api_bp = Blueprint('webhook_payload_tester_api', __name__)

@api_bp.route('/api/minimal-solutions/webhook_payload_tester', methods=['POST'])
def handle_webhook_payload_tester():
    data = request.get_json(silent=True)
    if not data:
        return error_response(ErrorCodes.INVALID_INPUT, "Ungültiges JSON Format im Request-Body.")

    is_valid, errors = validate_request(data)
    if not is_valid:
        return error_response(ErrorCodes.VALIDATION_ERROR, "Validierungsfehler", details=errors)

    payload_json = data.get('payload_json')
    try:
        parsed_payload = json.loads(payload_json)
        return success_response({
            "parsed_payload": parsed_payload,
            "is_valid": True,
            "message": "The webhook payload is valid and correctly formatted JSON."
        })
    except json.JSONDecodeError as e:
        return success_response({
            "parsed_payload": {},
            "is_valid": False,
            "message": f"Invalid JSON format: {str(e)}"
        })
