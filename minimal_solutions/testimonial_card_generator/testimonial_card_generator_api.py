# API Handler for Testimonial Card Generator
from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.testimonial_card_generator.testimonial_card_generator_validation import validate_testimonial_request

api_bp = Blueprint('testimonial_card_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/testimonial_card_generator', methods=['POST'])
def generate_testimonial_card():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_testimonial_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    name = data.get('name', '').strip()
    role = data.get('role', '').strip()
    quote = data.get('quote', '').strip()

    result = {
        "name": name,
        "role": role,
        "quote": quote,
        "avatar_url": f"https://api.dicebear.com/7.x/initials/svg?seed={name}"
    }

    return success_response(data={"result": result})
