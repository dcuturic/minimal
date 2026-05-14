from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .seo_formatter_validation import validate_seo_formatter_input
import re

api_bp = Blueprint('seo_formatter_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_formatter', methods=['POST'])
def process():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_seo_formatter_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
    
    topic = data.get('topic', '')
    target = data.get('target', '')
    options = data.get('options', {})

    format_type = options.get('format', 'html')
    
    # Fake SEO formatting logic for the minimal solution
    slug = re.sub(r'[^a-z0-9]+', '-', topic.lower()).strip('-')
    
    if format_type == 'markdown':
        formatted_result = f"# {topic.title()}\n\n**Target Audience:** {target}\n\n*SEO optimized formatted text goes here.*"
    else:
        formatted_result = f"<h1>{topic.title()}</h1>\n<p><b>Target Audience:</b> {target}</p>\n<p><i>SEO optimized formatted text goes here.</i></p>"
    
    return success_response(data={
        "formatted_text": formatted_result,
        "slug": slug,
        "character_count": len(formatted_result)
    })
