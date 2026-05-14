from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.base64_encoder_decoder.base64_encoder_decoder_validation import validate_base64_request
import base64
import binascii

api_bp = Blueprint('base64_encoder_decoder_api', __name__)

@api_bp.route('/api/minimal-solutions/base64_encoder_decoder', methods=['POST'])
def handle_base64():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_base64_request(data)
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
            text_bytes = text.encode('utf-8')
            base64_bytes = base64.b64encode(text_bytes)
            result = base64_bytes.decode('utf-8')
        elif mode == 'decode':
            base64_bytes = text.encode('utf-8')
            text_bytes = base64.b64decode(base64_bytes, validate=True)
            result = text_bytes.decode('utf-8')
    except binascii.Error:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Ungültiges Base64-Format",
            details={"text": "Der eingegebene Text ist kein gültiges Base64."}
        )
    except UnicodeDecodeError:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Ungültiges Base64-Format (Kein UTF-8)",
            details={"text": "Der dekodierte Text ist kein gültiges UTF-8 und kann nicht als String dargestellt werden."}
        )
    except Exception:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )

    return success_response(data={
        "result": result
    })
