from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.http_status_lookup.http_status_lookup_validation import validate_http_status_request
from http import HTTPStatus
import http.client

api_bp = Blueprint('http_status_lookup_api', __name__)

def get_status_class(code):
    if 100 <= code <= 199:
        return "Informational"
    elif 200 <= code <= 299:
        return "Success"
    elif 300 <= code <= 399:
        return "Redirection"
    elif 400 <= code <= 499:
        return "Client Error"
    elif 500 <= code <= 599:
        return "Server Error"
    return "Unknown"

@api_bp.route('/api/minimal-solutions/http_status_lookup', methods=['POST'])
def handle_http_status_lookup():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_http_status_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    status_code = int(data.get('status_code'))
    
    phrase = http.client.responses.get(status_code, "Unknown Status Code")
    description = "No specific description available."
    
    try:
        status_obj = HTTPStatus(status_code)
        phrase = status_obj.phrase
        description = status_obj.description
    except ValueError:
        pass

    result = {
        "status_code": status_code,
        "phrase": phrase,
        "description": description,
        "class": get_status_class(status_code)
    }

    return success_response(data=result)
