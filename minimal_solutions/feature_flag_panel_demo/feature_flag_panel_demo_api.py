from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.feature_flag_panel_demo.feature_flag_panel_demo_validation import validate_feature_flag_request

api_bp = Blueprint('feature_flag_panel_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/feature_flag_panel_demo', methods=['POST'])
def handle_feature_flag_panel_demo():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_feature_flag_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    flags = data.get('flags')
    
    flag_list = []
    
    try:
        for flag_name in flags:
            if flag_name.strip():
                flag_list.append({
                    "name": flag_name.strip(),
                    "enabled": False
                })
    except Exception as e:
        return error_response(
            code=ErrorCodes.INTERNAL_SERVER_ERROR,
            message="Fehler bei der Verarbeitung der Flags."
        )

    return success_response(data={
        "flags": flag_list
    })
