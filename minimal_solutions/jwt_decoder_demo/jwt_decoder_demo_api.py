import base64
import json
from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.jwt_decoder_demo.jwt_decoder_demo_validation import validate_jwt_request

api_bp = Blueprint('jwt_decoder_demo_api', __name__)

def decode_base64_url(encoded):
    # Add padding if missing
    padded = encoded + '=' * (4 - len(encoded) % 4)
    return base64.urlsafe_b64decode(padded).decode('utf-8')

@api_bp.route('/api/minimal-solutions/jwt_decoder_demo', methods=['POST'])
def handle_jwt_decoder_demo():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_jwt_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    jwt_token = data.get('jwt')
    parts = jwt_token.split('.')
    
    # Validation already checks if len(parts) == 3
    try:
        header_json = decode_base64_url(parts[0])
        header = json.loads(header_json)
    except Exception:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details={"jwt": "Der Header des JWT ist kein gültiges Base64Url oder JSON."}
        )
        
    try:
        payload_json = decode_base64_url(parts[1])
        payload = json.loads(payload_json)
    except Exception:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details={"jwt": "Der Payload des JWT ist kein gültiges Base64Url oder JSON."}
        )

    return success_response(data={
        "header": header,
        "payload": payload,
        "signature": parts[2]
    })
