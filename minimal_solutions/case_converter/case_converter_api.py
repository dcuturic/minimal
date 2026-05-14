from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.case_converter.case_converter_validation import validate_case_converter_request
import re

api_bp = Blueprint('case_converter_api', __name__)

def convert_case(text, target_case):
    if target_case == 'uppercase':
        return text.upper()
    if target_case == 'lowercase':
        return text.lower()
    if target_case == 'titlecase':
        return text.title()
    
    # For programmatic cases, extract words
    # This regex splits on non-alphanumeric chars and also separates camelCase
    # by inserting a space before uppercase letters (except at the start).
    # Then it splits by spaces or non-alphanumeric characters.
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', text)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)
    words = [w for w in re.split(r'[^a-zA-Z0-9]+', s2) if w]
    
    if not words:
        return text
        
    if target_case == 'snakecase':
        return '_'.join(w.lower() for w in words)
    if target_case == 'kebabcase':
        return '-'.join(w.lower() for w in words)
    if target_case == 'pascalcase':
        return ''.join(w.capitalize() for w in words)
    if target_case == 'camelcase':
        return words[0].lower() + ''.join(w.capitalize() for w in words[1:])
        
    return text

@api_bp.route('/api/minimal-solutions/case_converter', methods=['POST'])
def handle_case_converter():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_case_converter_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    text = data.get('text', '')
    target_case = data.get('target_case', 'lowercase')
    
    try:
        result = convert_case(text, target_case)
        return success_response(data={
            "result": result
        })
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )
