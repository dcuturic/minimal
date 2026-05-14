from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_summarizer.landingpage_summarizer_validation import validate_summarizer_request

api_bp = Blueprint('landingpage_summarizer_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_summarizer', methods=['POST'])
def landingpage_summarizer():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_summarizer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy summary logic
    summary = f"Dies ist eine generierte Zusammenfassung für die Landingpage zum Thema '{topic}'.\n\nZielgruppe: {target}\nOptionen: {options}\n\nDie Landingpage bietet eine klare und präzise Darstellung der wichtigsten Informationen. Die Inhalte sind auf die Zielgruppe '{target}' abgestimmt und berücksichtigen die angegebenen Optionen. Eine Optimierung der Call-to-Action-Elemente könnte die Conversion-Rate weiter steigern."

    return success_response(data={
        "summary_result": summary,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
