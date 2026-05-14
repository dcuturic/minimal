from flask import Blueprint, jsonify, request
from .dateigroessen_converter_validation import validate_request
from app.responses import success_response, error_response, ErrorCodes

api_bp = Blueprint('dateigroessen_converter_api', __name__)

UNIT_MULTIPLIERS = {
    "B": 1,
    "KB": 1024,
    "MB": 1024**2,
    "GB": 1024**3,
    "TB": 1024**4
}

@api_bp.route('/api/minimal-solutions/dateigroessen_converter', methods=['POST'])
def convert():
    data = request.get_json(silent=True) or {}
    
    is_valid, errors = validate_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    value = float(data["value"])
    from_unit = data["from_unit"]
    to_unit = data["to_unit"]
    
    # Convert to bytes first
    value_in_bytes = value * UNIT_MULTIPLIERS[from_unit]
    
    # Convert from bytes to target unit
    result = value_in_bytes / UNIT_MULTIPLIERS[to_unit]
    
    response_data = {
        "result": round(result, 6),
        "formatted": f"{result:.2f} {to_unit}"
    }
    
    return success_response(data=response_data)
