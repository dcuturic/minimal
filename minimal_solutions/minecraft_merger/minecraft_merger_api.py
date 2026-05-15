from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .minecraft_merger_validation import validate_input

api_bp = Blueprint('minecraft_merger_api', __name__)

@api_bp.route('/api/minimal-solutions/minecraft_merger', methods=['POST'])
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
        
    input_text = data.get("input_text")
    mode = data.get("mode")
    options = data.get("options", {})
    
    # Mock behavior for the minimal solution
    result_data = {
        "input_text": input_text,
        "mode": mode,
        "options": options,
        "message": "Merge erfolgreich durchgeführt."
    }
    
    return success_response(data=result_data)
