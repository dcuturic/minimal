from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .minecraft_normalizer_validation import validate_input
import re

api_bp = Blueprint('minecraft_normalizer_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_normalizer', methods=['POST'])
def process():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")
    
    data = request.get_json()
    is_valid, errors = validate_input(data)
    
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors,
            status_code=400
        )
        
    input_text = data.get("input_text", "")
    mode = data.get("mode", "default")
    options = data.get("options", {})
    
    if isinstance(input_text, list):
        items = [str(item) for item in input_text]
        input_string = "\n".join(items)
    else:
        input_string = str(input_text)
    
    lines = input_string.split("\n")
    normalized_lines = []
    
    for line in lines:
        cleaned = re.sub(r'\s+', ' ', line).strip()
        if cleaned:
            if mode == 'lowercase':
                cleaned = cleaned.lower()
            elif mode == 'uppercase':
                cleaned = cleaned.upper()
            normalized_lines.append(cleaned)
            
    normalized_text = "\n".join(normalized_lines)
    
    result_data = {
        "normalized_text": normalized_text,
        "mode": mode,
        "options": options,
        "message": "Normalisierung erfolgreich durchgeführt."
    }
    
    return success_response(data=result_data)
