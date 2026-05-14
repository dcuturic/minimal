from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_normalizer.landingpage_normalizer_validation import validate_normalizer_request

api_bp = Blueprint('landingpage_normalizer_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_normalizer', methods=['POST'])
def landingpage_normalizer():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_normalizer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy normalizer logic
    normalize_result = f"Landingpage erfolgreich normalisiert.\nThema: '{topic}'\nZielgruppe: '{target}'\nVerwendete Optionen: {options}\nDie Struktur wurde an den Standard angepasst."

    return success_response(data={
        "normalize_status": "success",
        "normalize_result": normalize_result,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
