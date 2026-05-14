from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.language_key_editor_demo.language_key_editor_demo_validation import validate_language_key_editor_request

api_bp = Blueprint('language_key_editor_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/language_key_editor_demo', methods=['POST'])
def handle_language_key_editor_demo():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )

    is_valid, errors = validate_language_key_editor_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    keys = data.get('keys')
    languages = data.get('languages')

    return success_response(data={
        "keys": keys,
        "languages": languages
    })
