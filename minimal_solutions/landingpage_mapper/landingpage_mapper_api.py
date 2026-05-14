from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_mapper.landingpage_mapper_validation import validate_mapper_request

api_bp = Blueprint('landingpage_mapper_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_mapper', methods=['POST'])
def landingpage_mapper():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_mapper_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy mapper logic
    mapping_result = f"Landingpage erfolgreich gemappt.\nThema: '{topic}'\nZielgruppe: '{target}'\nVerwendete Optionen: {options}\nDie Struktur wurde zugewiesen."

    return success_response(data={
        "map_status": "success",
        "map_result": mapping_result,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
