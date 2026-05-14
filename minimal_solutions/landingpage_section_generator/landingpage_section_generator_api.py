# API handler for Landingpage Section Generator
from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_section_generator.landingpage_section_generator_validation import validate_section_request

api_bp = Blueprint('landingpage_section_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_section_generator', methods=['POST'])
def generate_section():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_section_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    section_type = data.get('section_type', '').strip().lower()
    topic = data.get('topic', '').strip()

    if section_type == 'hero':
        result = {
            "type": "hero",
            "headline": f"Supercharge your {topic}",
            "subheadline": f"The best way to manage your {topic} workflow efficiently and effortlessly.",
            "call_to_action": "Get Started Now"
        }
    elif section_type == 'features':
        result = {
            "type": "features",
            "headline": f"Why choose our {topic}?",
            "subheadline": "Everything you need to succeed.",
            "features": [
                {"title": "Fast Integration", "description": "Quickly set up and start using the tool."},
                {"title": "Secure by Default", "description": "Enterprise-grade security built right in."},
                {"title": "24/7 Support", "description": "We are here to help whenever you need."}
            ]
        }
    elif section_type == 'testimonials':
        result = {
            "type": "testimonials",
            "headline": "What our users say",
            "subheadline": f"Join thousands of satisfied {topic} customers.",
            "testimonials": [
                {"author": "Jane Doe", "role": "CEO", "quote": f"This {topic} completely transformed our business."},
                {"author": "John Smith", "role": "CTO", "quote": "Incredible performance and easy to use."}
            ]
        }
    elif section_type == 'cta':
        result = {
            "type": "cta",
            "headline": f"Ready to try {topic}?",
            "subheadline": "Join us today and see the difference.",
            "call_to_action": "Start Free Trial"
        }
    elif section_type == 'faq':
        result = {
            "type": "faq",
            "headline": "Frequently Asked Questions",
            "subheadline": f"Everything you need to know about our {topic}.",
            "faqs": [
                {"question": "How do I get started?", "answer": "Simply click the get started button and follow the instructions."},
                {"question": "Is there a free trial?", "answer": "Yes, we offer a 14-day free trial on all plans."}
            ]
        }
    else:
        result = {
            "type": section_type,
            "headline": f"Welcome to {topic}",
            "subheadline": "Discover more about our offerings.",
            "call_to_action": "Learn More"
        }

    return success_response(data={"result": result})
