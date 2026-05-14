from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_masker.landingpage_masker_validation import validate_masker_request

api_bp = Blueprint('landingpage_masker_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_masker', methods=['POST'])
def landingpage_masker():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_masker_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy masker logic
    mask_result = f"Landingpage-Maskierung erfolgreich.\nThema: '{topic}'\nZielgruppe: '{target}'\nVerwendete Optionen: {options}\nSensible Daten wurden auf der Landingpage maskiert."

    return success_response(data={
        "mask_status": "success",
        "mask_result": mask_result,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
