from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.favicon_generator_demo.favicon_generator_demo_validation import validate_request

api_bp = Blueprint('favicon_generator_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/favicon_generator_demo', methods=['POST'])
def generate_favicon():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    letters = data.get('letters', '').upper()
    primary_color = data.get('primary_color', '#000000')
    shape = data.get('shape', 'square')

    rx = 0
    if shape == 'circle':
        rx = 256
    elif shape == 'rounded':
        rx = 128
        
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
        <rect width="512" height="512" rx="{rx}" fill="{primary_color}" />
        <text x="50%" y="50%" font-family="Arial, sans-serif" font-size="256" font-weight="bold" fill="#ffffff" dominant-baseline="central" text-anchor="middle">{letters}</text>
    </svg>'''

    return success_response(data={
        "favicon_svg": svg
    })
