from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from .seo_preview_validation import validate_request

api_bp = Blueprint('seo_preview_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_preview', methods=['POST'])
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

    title_suffix = f" | {target}" if target else ""
    preview_title = f"{topic}{title_suffix}"
    
    # Simulate a realistic URL slug
    slug = topic.lower().replace(" ", "-").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    slug = "".join(c for c in slug if c.isalnum() or c == "-")
    preview_url = f"https://www.example.com/{slug[:30]}"
    
    preview_description = f"Erfahren Sie alles über {topic}. Wir bieten detaillierte Einblicke und Lösungen für {target}. Jetzt lesen!"

    if options.get("uppercase_title"):
        preview_title = preview_title.upper()

    return success_response(data={
        "preview": {
            "title": preview_title,
            "url": preview_url,
            "description": preview_description
        },
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
