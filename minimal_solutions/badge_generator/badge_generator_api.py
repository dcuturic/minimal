from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.badge_generator.badge_generator_validation import validate_request

api_bp = Blueprint('badge_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/badge_generator', methods=['POST'])
def generate_badge():
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

    label = data.get('label', '')
    value = data.get('value', '')
    style = data.get('style', 'flat')

    # Basic widths logic based on character length
    label_width = len(label) * 8 + 20
    value_width = len(value) * 8 + 20
    total_width = label_width + value_width

    left_color = "#555"
    if style == "social":
        left_color = "#333"
        right_color = "#4c1"
    elif style == "plastic":
        right_color = "#e05d44"
    elif style == "for-the-badge":
        right_color = "#007ec6"
    else:
        right_color = "#4c1"

    svg_code = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="20">
    <linearGradient id="b" x2="0" y2="100%">
        <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
        <stop offset="1" stop-opacity=".1"/>
    </linearGradient>
    <mask id="a">
        <rect width="{total_width}" height="20" rx="3" fill="#fff"/>
    </mask>
    <g mask="url(#a)">
        <path fill="{left_color}" d="M0 0h{label_width}v20H0z"/>
        <path fill="{right_color}" d="M{label_width} 0h{value_width}v20H{label_width}z"/>
        <path fill="url(#b)" d="M0 0h{total_width}v20H0z"/>
    </g>
    <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">
        <text x="{label_width / 2}" y="15" fill="#010101" fill-opacity=".3">{label}</text>
        <text x="{label_width / 2}" y="14">{label}</text>
        <text x="{label_width + value_width / 2}" y="15" fill="#010101" fill-opacity=".3">{value}</text>
        <text x="{label_width + value_width / 2}" y="14">{value}</text>
    </g>
</svg>'''

    return success_response(data={
        "badge_svg": svg_code,
        "label": label,
        "value": value,
        "style": style
    })
