from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .minecraft_normalizer_validation import validate_input

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
    
    # Mock behavior for the minimal solution
    result_data = {
        "input_text": input_text,
        "message": "Normalizer erfolgreich durchgeführt."
    }
    
    return success_response(data=result_data)
