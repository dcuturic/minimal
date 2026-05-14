from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.word_replacer.word_replacer_validation import validate_word_replacer_request
import re

api_bp = Blueprint('word_replacer_api', __name__)

@api_bp.route('/api/minimal-solutions/word_replacer', methods=['POST'])
def handle_word_replacer():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_word_replacer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    text = data.get('text', '')
    search = data.get('search', '')
    replace = data.get('replace', '')
    case_sensitive = data.get('case_sensitive', False)
    
    if isinstance(case_sensitive, str):
        case_sensitive = case_sensitive.lower() == 'true'

    try:
        if case_sensitive:
            result = text.replace(search, replace)
        else:
            # Case insensitive replace
            escaped_search = re.escape(search)
            pattern = re.compile(escaped_search, re.IGNORECASE)
            result = pattern.sub(lambda m: replace, text)
            
        return success_response(data={
            "result": result
        })
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )
