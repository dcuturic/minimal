from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .seo_masker_validation import validate_input

api_bp = Blueprint('seo_masker_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_masker', methods=['POST'])
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
        
    topic = data.get("topic")
    target = data.get("target")
    options = data.get("options", {})
    
    # Mock behavior for the minimal solution
    result_data = {
        "topic": topic,
        "target": target,
        "options": options,
        "masked_url": f"https://example.com/mask/{topic.replace(' ', '-').lower()}",
        "message": f"Maskierung für '{topic}' erfolgreich durchgeführt."
    }
    
    return success_response(data=result_data)
