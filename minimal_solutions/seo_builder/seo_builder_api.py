from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .seo_builder_validation import validate_request

api_bp = Blueprint('seo_builder_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_builder', methods=['POST'])
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

    # Generate some SEO builder output
    title = f"{topic} - {target} | Best Practices"
    description = f"Erfahre alles über {topic} im Bereich {target}. Optimiere deine Inhalte mit unserem SEO Builder."
    keywords = [topic.lower(), target.lower(), "seo", "builder", "optimierung"]

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
