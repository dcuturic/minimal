from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.border_radius_generator.border_radius_generator_validation import validate_border_radius_request

api_bp = Blueprint('border_radius_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/border_radius_generator', methods=['POST'])
def generate_border_radius():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_border_radius_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    top_left = data.get('top_left')
    top_right = data.get('top_right')
    bottom_right = data.get('bottom_right')
    bottom_left = data.get('bottom_left')

    css = f"{top_left}px {top_right}px {bottom_right}px {bottom_left}px"

    return success_response(data={"css": css})
