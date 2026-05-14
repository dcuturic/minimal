from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_formatter.landingpage_formatter_validation import validate_landingpage_formatter_request

api_bp = Blueprint('landingpage_formatter_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_formatter', methods=['POST'])
def format_landingpage():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_landingpage_formatter_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic', '').strip()
    target = data.get('target', '').strip()
    options = data.get('options', '').strip()
    
    # Format landing page structure
    formatted_output = f"""=========================================
 LANDINGPAGE FORMATTER RESULT
=========================================

--- TOPIC ---
{topic.upper()}

--- TARGET AUDIENCE ---
{target}

--- OPTIONS ---
{options if options else 'No options provided'}

=========================================
"""

    return success_response(data={
        "result": formatted_output
    })
