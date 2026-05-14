from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.hosting_analyzer.validation_hosting_analyzer import validate_hosting_analyzer_request

api_bp = Blueprint('hosting_analyzer_api', __name__)

@api_bp.route('/api/minimal-solutions/hosting_analyzer', methods=['POST'])
def handle_hosting_analyzer_request():
    if not request.is_json:
        return error_response(ErrorCodes.BAD_REQUEST, "Request must be JSON")

    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_hosting_analyzer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors,
            status_code=400
        )

    source = data.get('source', '')
    mode = data.get('mode', 'default')
    config = data.get('config', {})

    # Mock analysis logic
    domain_count = len(source.split('\n')) if source else 0
    
    result_data = {
        "status": "success",
        "message": "Hosting analysis completed successfully.",
        "analysis_results": {
            "domain_count": domain_count,
            "mode_used": mode,
            "issues_found": 0 if domain_count > 0 else 1,
            "recommendations": ["Optimize DNS settings", "Check SSL certificates"] if domain_count > 0 else ["Provide valid source domains"]
        }
    }

    return success_response(data=result_data)
