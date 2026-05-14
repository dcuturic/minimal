from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.json_formatter.json_formatter_validation import validate_json_formatter_request
import json

api_bp = Blueprint('json_formatter_api', __name__)

@api_bp.route('/api/minimal-solutions/json_formatter', methods=['POST'])
def format_json():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_json_formatter_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    json_text = data.get('json_text')
    indent_input = data.get('indent')
    
    # Process indent. It can be an integer or a string.
    # We might get '2', '4', '\t', 'tab' from the UI.
    if isinstance(indent_input, str):
        if indent_input == 'tab':
            indent = '\t'
        elif indent_input.isdigit():
            indent = int(indent_input)
        else:
            indent = indent_input
    else:
        indent = indent_input

    try:
        parsed_json = json.loads(json_text)
    except json.JSONDecodeError as e:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Ungültiges JSON-Format",
            details={"json_text": f"Fehler beim Parsen des JSON: {str(e)}"}
        )
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Verarbeiten des JSON."
        )

    try:
        formatted_json = json.dumps(parsed_json, indent=indent, ensure_ascii=False)
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Formatieren des JSON."
        )

    return success_response(data={"formatted_json": formatted_json})
