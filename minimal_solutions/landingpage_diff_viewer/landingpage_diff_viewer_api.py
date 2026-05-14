from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_diff_viewer.landingpage_diff_viewer_validation import validate_diff_viewer_request

api_bp = Blueprint('landingpage_diff_viewer_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_diff_viewer', methods=['POST'])
def landingpage_diff_viewer():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_diff_viewer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy diff viewer logic
    diff_result = f"Landingpage Diff erfolgreich erstellt.\nThema: '{topic}'\nZielgruppe: '{target}'\nVerwendete Optionen: {options}\nDie Diff-Ansicht ist bereit."

    return success_response(data={
        "diff_status": "success",
        "diff_result": diff_result,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
