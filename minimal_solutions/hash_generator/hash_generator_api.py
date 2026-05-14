from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.hash_generator.hash_generator_validation import validate_hash_generator_request
import hashlib

api_bp = Blueprint('hash_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/hash_generator', methods=['POST'])
def handle_hash_generator():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_hash_generator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    text = data.get('text', '')
    algorithm = data.get('algorithm')
    
    result = ""
    try:
        text_bytes = text.encode('utf-8')
        if algorithm == 'md5':
            result = hashlib.md5(text_bytes).hexdigest()
        elif algorithm == 'sha1':
            result = hashlib.sha1(text_bytes).hexdigest()
        elif algorithm == 'sha256':
            result = hashlib.sha256(text_bytes).hexdigest()
        elif algorithm == 'sha512':
            result = hashlib.sha512(text_bytes).hexdigest()
    except Exception:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )
        
    return success_response(data={"result": result})
