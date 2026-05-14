from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_checker.landingpage_checker_validation import validate_checker_request

api_bp = Blueprint('landingpage_checker_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_checker', methods=['POST'])
def landingpage_checker():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_checker_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy checker logic
    result_text = f"Dies ist ein generierter Check für die Landingpage zum Thema '{topic}'.\n\nZielgruppe: {target}\nOptionen: {options}\n\nDie Struktur der Landingpage sieht gut aus. Die Überschriften sind klar formuliert. Empfehlung: Mehr Call-to-Action Buttons einfügen, um die Conversion zu steigern."

    return success_response(data={
        "check_result": result_text,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
