from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_validator.landingpage_validator_validation import validate_landingpage_validator_request

api_bp = Blueprint('landingpage_validator_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_validator', methods=['POST'])
def validate_landingpage():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_landingpage_validator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic', '').strip()
    target = data.get('target', '').strip()
    options = data.get('options', '').strip()
    
    # Validating landing page content based on basic rules
    validation_results = []
    
    # 1. Topic length check
    if len(topic) < 5:
        validation_results.append("⚠️ Topic might be too short to be descriptive.")
    else:
        validation_results.append("✅ Topic length is optimal.")
        
    # 2. Target audience clarity check
    if len(target.split()) < 2:
        validation_results.append("⚠️ Target audience could be more specific.")
    else:
        validation_results.append("✅ Target audience is specific.")
        
    # 3. Options validation
    if not options:
        validation_results.append("⚠️ No additional options provided. Consider adding context.")
    else:
        validation_results.append("✅ Additional options recognized.")
        
    validation_output = "\n".join(validation_results)

    return success_response(data={
        "result": f"Validation Report:\n------------------\n{validation_output}"
    })
