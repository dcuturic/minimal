from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.svg_icon_generator.svg_icon_generator_validation import validate_request

api_bp = Blueprint('svg_icon_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/svg_icon_generator', methods=['POST'])
def generate_svg_icon():
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

    shape = data.get('shape', 'square')
    color = data.get('color', '#3b82f6')
    label = data.get('label', '')

    svg_content = ""
    
    if shape == 'circle':
        svg_content = f'<circle cx="256" cy="256" r="256" fill="{color}" />'
    elif shape == 'square':
        svg_content = f'<rect width="512" height="512" fill="{color}" />'
    elif shape == 'rounded':
        svg_content = f'<rect width="512" height="512" rx="128" fill="{color}" />'
    elif shape == 'star':
        svg_content = f'<polygon points="256,10 326,170 502,170 360,270 414,440 256,340 98,440 152,270 10,170 186,170" fill="{color}" />'
    elif shape == 'hexagon':
        svg_content = f'<polygon points="256,0 478,128 478,384 256,512 34,384 34,128" fill="{color}" />'
    elif shape == 'triangle':
        svg_content = f'<polygon points="256,0 512,512 0,512" fill="{color}" />'
    elif shape == 'diamond':
        svg_content = f'<polygon points="256,0 512,256 256,512 0,256" fill="{color}" />'
    elif shape == 'shield':
        svg_content = f'<path d="M0 0 L512 0 L512 170 C512 340 256 512 256 512 C256 512 0 340 0 170 Z" fill="{color}" />'
    
    text_content = ""
    if label:
        text_content = f'<text x="50%" y="50%" font-family="Inter, Arial, sans-serif" font-size="256" font-weight="bold" fill="#ffffff" dominant-baseline="central" text-anchor="middle">{label}</text>'

    svg_code = f\'\'\'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
    {svg_content}
    {text_content}
</svg>\'\'\'

    return success_response(data={
        "svg_code": svg_code,
        "shape": shape,
        "color": color,
        "label": label
    })
