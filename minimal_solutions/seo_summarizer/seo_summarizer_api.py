from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.seo_summarizer.seo_summarizer_validation import validate_seo_summarizer_request

api_bp = Blueprint('seo_summarizer_api', __name__)

@api_bp.route('/api/minimal-solutions/seo_summarizer', methods=['POST'])
def handle_seo_summarizer_request():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_seo_summarizer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get("topic", "")
    target = data.get("target", "")
    options = data.get("options", {})

    summary = (
        f"Dies ist eine generierte SEO-Zusammenfassung für das Thema '{topic}'. "
        f"Die Zielgruppe ist '{target}'. "
        "Diese Minimal-Lösung simuliert aktuell nur die Ausgabe ohne externen Dienst."
    )

    return success_response(data={
        "summary": summary,
        "topic": topic,
        "target": target,
        "options": options
    })
