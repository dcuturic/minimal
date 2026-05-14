from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.link_shortener_demo.link_shortener_demo_validation import validate_link_shortener_request
import random
import string

api_bp = Blueprint('link_shortener_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/link_shortener_demo', methods=['POST'])
def handle_link_shortener_demo():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_link_shortener_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    long_url = data.get('long_url', '')
    custom_slug = data.get('custom_slug', '')
    
    if not custom_slug:
        # Generate random 6 character slug
        custom_slug = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        
    base_url = "https://short.ch"
    short_url = f"{base_url}/{custom_slug}"
        
    return success_response(data={"short_url": short_url, "clicks": 0})
