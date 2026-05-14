from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_merger.landingpage_merger_validation import validate_merger_request

api_bp = Blueprint('landingpage_merger_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_merger', methods=['POST'])
def landingpage_merger():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_merger_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy merger logic
    merge_result = f"Landingpages erfolgreich gemerged.\nThema: '{topic}'\nZielgruppe: '{target}'\nVerwendete Optionen: {options}\nEs wurden mehrere Varianten zu einer Master-Landingpage zusammengeführt."

    return success_response(data={
        "merge_status": "success",
        "merge_result": merge_result,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
