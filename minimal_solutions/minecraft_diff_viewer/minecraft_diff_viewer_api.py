from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .minecraft_diff_viewer_validation import validate_input

api_bp = Blueprint('minecraft_diff_viewer_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_diff_viewer', methods=['POST'])
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
    
    # Minimal mapping logic
    mapped_lines = []
    for line in input_string.split("\n"):
        line = line.strip()
        if not line:
            continue
            
        if mode == 'prefix':
            mapped_lines.append(f"[Mapped] {line}")
        elif mode == 'suffix':
            mapped_lines.append(f"{line} [Mapped]")
        else:
            mapped_lines.append(f"-> {line}")
            
    mapped_text = "\n".join(mapped_lines)
    
    result_data = {
        "mapped_text": mapped_text,
        "mode": mode,
        "options": options,
        "message": "Mapping erfolgreich durchgeführt."
    }
    
    return success_response(data=result_data)
