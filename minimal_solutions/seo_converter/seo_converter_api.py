from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .seo_converter_validation import validate_request

api_bp = Blueprint('seo_converter_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_converter', methods=['POST'])
def process():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(code=ErrorCodes.BAD_REQUEST, message="Erwartet wurde ein JSON-Objekt/Dictionary.")

    is_valid, errors = validate_request(data)
    if not is_valid:
        return error_response(code=ErrorCodes.VALIDATION_ERROR, message="Validierungsfehler", details=errors)

    topic = data.get('topic', '').strip()
    target = data.get('target', '').strip()
    options = data.get('options', {})

    # Generate some SEO converter output
    title = f"Converted {topic} for {target}"
    description = f"Here is the converted SEO content for {topic} targeting {target}."
    keywords = [topic.lower(), target.lower(), "seo", "converter"]

    if options.get("uppercase_title"):
        title = title.upper()

    return success_response(data={
        "result": {
            "title": title,
            "description": description,
            "keywords": ", ".join(keywords)
        },
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
