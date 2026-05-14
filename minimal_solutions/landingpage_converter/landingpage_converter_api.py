from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_converter.landingpage_converter_validation import validate_converter_request

api_bp = Blueprint('landingpage_converter_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_converter', methods=['POST'])
def landingpage_converter():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_converter_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    features_list = []
    if options:
        if isinstance(options, str):
            features_list = [f.strip() for f in options.split(',') if f.strip()]
        elif isinstance(options, dict):
            features_list = list(options.keys())
    
    if not features_list:
        features_list = ["Optimized Performance", "Seamless Integration", "User Friendly"]

    converted_data = {
        "headline": f"Discover the Power of {topic}",
        "subheadline": f"The ultimate solution tailored for {target}",
        "features": features_list,
        "call_to_action": "Get Started Today"
    }

    return success_response(data={
        "converted_data": converted_data,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
