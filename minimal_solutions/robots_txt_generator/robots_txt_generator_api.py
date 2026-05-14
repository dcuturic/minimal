from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.robots_txt_generator.robots_txt_generator_validation import validate_robots_txt_generator_input

api_bp = Blueprint('robots_txt_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/robots_txt_generator', methods=['POST'])
def generate_robots_txt():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_robots_txt_generator_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    allow = data.get('allow', '').strip()
    disallow = data.get('disallow', '').strip()
    sitemap_url = data.get('sitemap_url', '').strip()
    user_agent = data.get('user_agent', '').strip() or '*'

    lines = [f"User-agent: {user_agent}"]
    
    if allow:
        for path in allow.split('\n'):
            path = path.strip()
            if path:
                # Add leading slash if missing and not a wildcard
                if not path.startswith('/') and not path.startswith('*'):
                    path = f"/{path}"
                lines.append(f"Allow: {path}")
                
    if disallow:
        for path in disallow.split('\n'):
            path = path.strip()
            if path:
                if not path.startswith('/') and not path.startswith('*'):
                    path = f"/{path}"
                lines.append(f"Disallow: {path}")
                
    if sitemap_url:
        lines.append(f"Sitemap: {sitemap_url}")

    result = "\n".join(lines)

    return success_response(data={
        "result": result
    })
