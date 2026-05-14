from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.regex_tester.regex_tester_validation import validate_regex_request
import re

api_bp = Blueprint('regex_tester_api', __name__)

@api_bp.route('/api/minimal-solutions/regex_tester', methods=['POST'])
def handle_regex_tester():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_regex_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    pattern = data.get('pattern')
    text = data.get('text')
    flags_str = data.get('flags', '')
    
    re_flags = 0
    if 'i' in flags_str:
        re_flags |= re.IGNORECASE
    if 'm' in flags_str:
        re_flags |= re.MULTILINE
    if 's' in flags_str:
        re_flags |= re.DOTALL

    try:
        compiled = re.compile(pattern, re_flags)
        
        matches = []
        for match in compiled.finditer(text):
            matches.append({
                'match': match.group(0),
                'start': match.start(),
                'end': match.end(),
                'groups': list(match.groups())
            })
            
        result = {
            'matches': matches,
            'count': len(matches)
        }
        
    except re.error as e:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message=f"Ungültiger Regex: {str(e)}"
        )
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten."
        )

    return success_response(data=result)
