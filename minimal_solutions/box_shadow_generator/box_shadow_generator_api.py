from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.box_shadow_generator.box_shadow_generator_validation import validate_box_shadow_request

api_bp = Blueprint('box_shadow_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/box_shadow_generator', methods=['POST'])
def generate_box_shadow():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_box_shadow_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    x = data.get('x')
    y = data.get('y')
    blur = data.get('blur')
    spread = data.get('spread')
    opacity = data.get('opacity')
    hex_color = data.get('color', '#000000')
    inset = data.get('inset', False)

    # Convert hex to rgb
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
    elif len(hex_color) == 3:
        r = int(hex_color[0]*2, 16)
        g = int(hex_color[1]*2, 16)
        b = int(hex_color[2]*2, 16)
    else:
        r, g, b = 0, 0, 0

    rgba_color = f"rgba({r}, {g}, {b}, {opacity})"
    inset_str = "inset " if inset else ""
    
    css = f"{inset_str}{x}px {y}px {blur}px {spread}px {rgba_color}"

    return success_response(data={"css": css})
