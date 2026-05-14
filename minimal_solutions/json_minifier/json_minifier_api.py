from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.json_minifier.json_minifier_validation import validate_json_minifier_request
import json

api_bp = Blueprint('json_minifier_api', __name__)

@api_bp.route('/api/minimal-solutions/json_minifier', methods=['POST'])
def minify_json():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_json_minifier_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    json_text = data.get('json_text')

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
        minified_json = json.dumps(parsed_json, separators=(',', ':'), ensure_ascii=False)
        original_size_bytes = len(json_text.encode('utf-8'))
        minified_size_bytes = len(minified_json.encode('utf-8'))
        
        saved_percentage = 0.0
        if original_size_bytes > 0:
            saved_percentage = round((1 - (minified_size_bytes / original_size_bytes)) * 100, 2)
            
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Interner Fehler beim Minifizieren des JSON."
        )

    return success_response(data={
        "minified_json": minified_json,
        "original_size_bytes": original_size_bytes,
        "minified_size_bytes": minified_size_bytes,
        "saved_percentage": saved_percentage
    })
