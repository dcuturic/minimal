from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_splitter.landingpage_splitter_validation import validate_splitter_request

api_bp = Blueprint('landingpage_splitter_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_splitter', methods=['POST'])
def landingpage_splitter():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_splitter_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy splitter logic
    split_result = f"Landingpage erfolgreich gesplittet.\nThema: '{topic}'\nZielgruppe: '{target}'\nVerwendete Optionen: {options}\nEs wurden 3 Varianten der Landingpage generiert."

    return success_response(data={
        "split_status": "success",
        "split_result": split_result,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
