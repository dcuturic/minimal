from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_cleaner.landingpage_cleaner_validation import validate_cleaner_request

api_bp = Blueprint('landingpage_cleaner_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_cleaner', methods=['POST'])
def landingpage_cleaner():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_cleaner_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy cleaner logic
    clean_result = f"Landingpage erfolgreich bereinigt.\nThema: '{topic}'\nZielgruppe: '{target}'\nVerwendete Optionen: {options}\nEs wurden überflüssige Elemente und Tracking-Skripte entfernt."

    return success_response(data={
        "clean_status": "success",
        "clean_result": clean_result,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
