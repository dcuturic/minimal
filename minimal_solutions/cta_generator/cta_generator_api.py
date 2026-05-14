from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.cta_generator.cta_generator_validation import validate_cta_request
import random

api_bp = Blueprint('cta_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/cta_generator', methods=['POST'])
def generate_cta():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_cta_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic').strip()
    audience = data.get('audience').strip()
    tone = data.get('tone').strip()

    templates = [
        f"Ready to master {topic}? Join our community of {audience} today! [Sign Up Now]",
        f"Don't let {topic} hold you back. Discover the solution built for {audience}. [Get Started]",
        f"Transform your approach to {topic}. Exclusive insights for {audience}. [Learn More]",
        f"Experience the ultimate {topic} guide designed specially for {audience}. [Download Free Guide]"
    ]
    
    prefix = ""
    suffix = ""
    if tone.lower() in ['urgent', 'dringend']:
        prefix = "Hurry! "
        suffix = " Limited time offer!"
    elif tone.lower() in ['professional', 'professionell']:
        prefix = "Elevate your business: "
    elif tone.lower() in ['casual', 'locker']:
        prefix = "Hey there! "
        suffix = " Let's dive in!"

    ctas = []
    for template in random.sample(templates, min(3, len(templates))):
        ctas.append(f"{prefix}{template}{suffix}")

    return success_response(data={"ctas": ctas})
