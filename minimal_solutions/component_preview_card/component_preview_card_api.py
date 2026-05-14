from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.component_preview_card.component_preview_card_validation import validate_preview_card_request

api_bp = Blueprint('component_preview_card_api', __name__)

@api_bp.route('/api/minimal-solutions/component_preview_card', methods=['POST'])
def handle_preview_card():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_preview_card_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    component_name = data.get('component_name')
    category = data.get('category')
    preview_html = data.get('preview_html')
    
    return success_response(data={
        "preview_card": {
            "component_name": component_name,
            "category": category,
            "preview_html": preview_html
        }
    })
