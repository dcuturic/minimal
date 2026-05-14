from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.html_escape_unescape.html_escape_unescape_validation import validate_html_escape_unescape_request
import html

api_bp = Blueprint('html_escape_unescape_api', __name__)

@api_bp.route('/api/minimal-solutions/html_escape_unescape', methods=['POST'])
def handle_html_escape_unescape():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_html_escape_unescape_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    html_text = data.get('html_text', '')
    mode = data.get('mode')
    
    result = ""
    try:
        if mode == 'escape':
            result = html.escape(html_text)
        elif mode == 'unescape':
            result = html.unescape(html_text)
    except Exception:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )
        
    return success_response(data={"result": result})
