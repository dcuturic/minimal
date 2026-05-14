from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.css_gradient_generator.css_gradient_generator_validation import validate_gradient_request

api_bp = Blueprint('css_gradient_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/css_gradient_generator', methods=['POST'])
def generate_gradient():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_gradient_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    colors = data.get('colors')
    angle = data.get('angle')
    gradient_type = data.get('type')

    colors_str = ", ".join(colors)

    if gradient_type == 'linear':
        css = f"linear-gradient({angle}deg, {colors_str})"
    elif gradient_type == 'radial':
        css = f"radial-gradient(circle, {colors_str})"
    else:
        css = ""

    return success_response(data={"css": css})
