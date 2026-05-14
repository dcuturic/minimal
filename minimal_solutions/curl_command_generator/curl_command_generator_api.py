from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.curl_command_generator.curl_command_generator_validation import validate_curl_request
import json

api_bp = Blueprint('curl_command_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/curl_command_generator', methods=['POST'])
def handle_curl_command_generator():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_curl_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    method = data.get('method', 'GET').upper()
    url = data.get('url', '').strip()
    headers = data.get('headers', {})
    body = data.get('body')

    try:
        curl_parts = [f"curl -X {method} '{url}'"]

        for key, value in headers.items():
            # escape single quotes in value
            safe_value = str(value).replace("'", "'\\''")
            curl_parts.append(f"-H '{key}: {safe_value}'")

        if body is not None and method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            if isinstance(body, (dict, list)):
                body_str = json.dumps(body)
            else:
                body_str = str(body)
            safe_body = body_str.replace("'", "'\\''")
            curl_parts.append(f"-d '{safe_body}'")

        curl_command = " \\\n  ".join(curl_parts)

    except Exception:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )

    return success_response(data={
        "curl_command": curl_command
    })
