from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.iframe_preview_url_builder.iframe_preview_url_builder_validation import validate_iframe_preview_url_builder_request
import urllib.parse

api_bp = Blueprint('iframe_preview_url_builder_api', __name__)

@api_bp.route('/api/minimal-solutions/iframe_preview_url_builder', methods=['POST'])
def handle_iframe_preview_url_builder():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_iframe_preview_url_builder_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    page = data.get('page')
    component = data.get('component')
    mode = data.get('mode', 'light')
    
    # Generate the preview URL
    base_url = "/preview"
    params = {
        "page": page,
        "component": component,
    }
    if mode:
        params["mode"] = mode
        
    query_string = urllib.parse.urlencode(params)
    preview_url = f"{base_url}?{query_string}"
    
    iframe_code = f'<iframe src="{preview_url}" width="100%" height="500px" style="border:1px solid #e2e8f0; border-radius:8px; overflow:hidden;"></iframe>'

    return success_response(data={
        "preview_url": preview_url,
        "iframe_code": iframe_code
    })
