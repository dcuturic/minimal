import re
from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.log_highlighter.log_highlighter_validation import validate_log_highlighter_request

api_bp = Blueprint('log_highlighter_api', __name__)

def determine_log_level(line):
    line_upper = line.upper()
    if re.search(r'\b(ERROR|FATAL|CRITICAL)\b', line_upper):
        return 'ERROR'
    if re.search(r'\b(WARN|WARNING)\b', line_upper):
        return 'WARN'
    if re.search(r'\b(INFO)\b', line_upper):
        return 'INFO'
    if re.search(r'\b(DEBUG|TRACE)\b', line_upper):
        return 'DEBUG'
    return 'UNKNOWN'

@api_bp.route('/api/minimal-solutions/log_highlighter', methods=['POST'])
def handle_log_highlighter():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_log_highlighter_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    log_text = data.get('log_text', '')
    
    try:
        lines = log_text.splitlines()
        result_lines = []
        for line in lines:
            level = determine_log_level(line)
            if not line.strip():
                # For empty lines, still return a space so the block element takes up vertical space
                result_lines.append({"text": " ", "level": "UNKNOWN"})
            else:
                result_lines.append({"text": line, "level": level})

    except Exception:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )
        
    return success_response(data={"lines": result_lines})
