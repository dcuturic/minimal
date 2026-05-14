from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_importer.landingpage_importer_validation import validate_importer_request

api_bp = Blueprint('landingpage_importer_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_importer', methods=['POST'])
def landingpage_importer():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_importer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy importer logic
    import_result = f"Landingpage-Import erfolgreich.\nThema: '{topic}'\nZielgruppe: '{target}'\nVerwendete Optionen: {options}\nDie Landingpage wurde in das System übernommen."

    return success_response(data={
        "import_status": "success",
        "import_result": import_result,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
