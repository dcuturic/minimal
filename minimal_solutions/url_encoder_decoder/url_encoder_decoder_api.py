from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.url_encoder_decoder.url_encoder_decoder_validation import validate_url_request
import urllib.parse

api_bp = Blueprint('url_encoder_decoder_api', __name__)

@api_bp.route('/api/minimal-solutions/url_encoder_decoder', methods=['POST'])
def handle_url_encoder_decoder():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_url_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    mode = data.get('mode')
    text = data.get('text')
    
    result = ""

    try:
        if mode == 'encode':
            result = urllib.parse.quote(text, safe='')
        elif mode == 'decode':
            result = urllib.parse.unquote(text)
    except Exception:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )

    return success_response(data={
        "result": result
    })
