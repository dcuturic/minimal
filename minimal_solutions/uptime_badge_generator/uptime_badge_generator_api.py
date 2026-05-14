from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.uptime_badge_generator.uptime_badge_generator_validation import validate_badge_request

api_bp = Blueprint('uptime_badge_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/uptime_badge_generator', methods=['POST'])
def generate_badge():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_badge_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    status = data.get('status', '').lower()
    uptime_percent = float(data.get('uptime_percent'))

    if uptime_percent >= 99.9:
        color = "#4c1"
    elif uptime_percent >= 99.0:
        color = "#97CA00"
    elif uptime_percent >= 98.0:
        color = "#dfb317"
    elif uptime_percent >= 95.0:
        color = "#fe7d37"
    else:
        color = "#e05d44"

    if status == 'down' or status == 'offline':
        color = "#e05d44"

    left_text = "uptime"
    right_text = f"{uptime_percent}%"
    
    left_width = len(left_text) * 7 + 10
    right_width = len(right_text) * 7 + 10
    total_width = left_width + right_width

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="20" role="img" aria-label="{left_text}: {right_text}">
    <title>{left_text}: {right_text}</title>
    <linearGradient id="s" x2="0" y2="100%">
        <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
        <stop offset="1" stop-opacity=".1"/>
    </linearGradient>
    <clipPath id="r">
        <rect width="{total_width}" height="20" rx="3" fill="#fff"/>
    </clipPath>
    <g clip-path="url(#r)">
        <rect width="{left_width}" height="20" fill="#555"/>
        <rect x="{left_width}" width="{right_width}" height="20" fill="{color}"/>
        <rect width="{total_width}" height="20" fill="url(#s)"/>
    </g>
    <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110">
        <text aria-hidden="true" x="{left_width * 10 / 2}" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="{len(left_text) * 60}">{left_text}</text>
        <text x="{left_width * 10 / 2}" y="140" transform="scale(.1)" fill="#fff" textLength="{len(left_text) * 60}">{left_text}</text>
        <text aria-hidden="true" x="{left_width * 10 + right_width * 10 / 2}" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="{len(right_text) * 60}">{right_text}</text>
        <text x="{left_width * 10 + right_width * 10 / 2}" y="140" transform="scale(.1)" fill="#fff" textLength="{len(right_text) * 60}">{right_text}</text>
    </g>
</svg>'''

    return success_response(data={
        "status": status,
        "uptime_percent": uptime_percent,
        "svg": svg
    })
