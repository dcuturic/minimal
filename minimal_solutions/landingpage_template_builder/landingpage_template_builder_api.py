from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.landingpage_template_builder.landingpage_template_builder_validation import validate_template_builder_request

api_bp = Blueprint('landingpage_template_builder_api', __name__)

@api_bp.route('/api/minimal-solutions/landingpage_template_builder', methods=['POST'])
def landingpage_template_builder():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_template_builder_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    topic = data.get('topic')
    target = data.get('target')
    options = data.get('options', '')

    # Dummy template builder logic
    template_result = f"Landingpage Template erfolgreich erstellt.\nThema: '{topic}'\nZielgruppe: '{target}'\nOptionen: {options}\nDas Template steht zur weiteren Bearbeitung bereit."

    return success_response(data={
        "build_status": "success",
        "template_result": template_result,
        "meta": {
            "topic": topic,
            "target": target,
            "options": options
        }
    })
