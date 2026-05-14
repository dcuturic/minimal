from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_viewer.landingpage_viewer_validation import validate_viewer_request

api_bp = Blueprint('landingpage_viewer_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_viewer', methods=['POST'])
def landingpage_viewer():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_viewer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy viewer logic
    viewer_result = f"Dies ist der generierte Landingpage-Viewer für das Thema '{topic}'.\n\nZielgruppe: {target}\nOptionen: {options}\n\nAnsicht: [Mobile] [Desktop] [Tablet]\nStatus: Aktiv."

    return success_response(data={
        "viewer_result": viewer_result,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
