from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_exporter.landingpage_exporter_validation import validate_exporter_request

api_bp = Blueprint('landingpage_exporter_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_exporter', methods=['POST'])
def landingpage_exporter():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_exporter_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    # Dummy logic
    topic = data.get('topic', '')
    target = data.get('target', '')
    options = data.get('options', '')

    exporter_result = f"Dies ist der generierte Landingpage-Exporter für das Thema '{topic}'.\nZielgruppe: {target}\nOptionen: {options}"

    return success_response(data={
        "exporter_result": exporter_result,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
