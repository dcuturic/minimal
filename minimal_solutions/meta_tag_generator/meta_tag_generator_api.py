from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.meta_tag_generator.meta_tag_generator_validation import validate_meta_tag_request
import html

api_bp = Blueprint('meta_tag_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/meta_tag_generator', methods=['POST'])
def generate():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )
        
    is_valid, errors = validate_meta_tag_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    title = data.get('title', '').strip() if data.get('title') else ''
    description = data.get('description', '').strip() if data.get('description') else ''
    image_url = data.get('image_url', '').strip() if data.get('image_url') else ''
    page_url = data.get('page_url', '').strip() if data.get('page_url') else ''
    
    tags = []
    
    # HTML Meta Tags
    if title:
        tags.append(f"<title>{html.escape(title)}</title>")
    if description:
        tags.append(f'<meta name="description" content="{html.escape(description)}">')
        
    # Open Graph / Facebook
    tags.append('<meta property="og:type" content="website">')
    if page_url:
        tags.append(f'<meta property="og:url" content="{html.escape(page_url)}">')
    if title:
        tags.append(f'<meta property="og:title" content="{html.escape(title)}">')
    if description:
        tags.append(f'<meta property="og:description" content="{html.escape(description)}">')
    if image_url:
        tags.append(f'<meta property="og:image" content="{html.escape(image_url)}">')
        
    # Twitter
    if image_url:
        tags.append('<meta name="twitter:card" content="summary_large_image">')
    else:
        tags.append('<meta name="twitter:card" content="summary">')
        
    if page_url:
        tags.append(f'<meta property="twitter:url" content="{html.escape(page_url)}">')
    if title:
        tags.append(f'<meta name="twitter:title" content="{html.escape(title)}">')
    if description:
        tags.append(f'<meta name="twitter:description" content="{html.escape(description)}">')
    if image_url:
        tags.append(f'<meta name="twitter:image" content="{html.escape(image_url)}">')
        
    html_output = "\n".join(tags)
    
    return success_response(data={
        "html": html_output
    })
