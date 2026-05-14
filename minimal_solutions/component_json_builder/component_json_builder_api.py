from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.component_json_builder.component_json_builder_validation import validate_component_json_builder_input

api_bp = Blueprint('component_json_builder_api', __name__)

@api_bp.route('/api/minimal-solutions/component_json_builder', methods=['POST'])
def handle_component_json_builder_request():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )

    is_valid, errors = validate_component_json_builder_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    template = data.get('template', '')
    env = data.get('env', {})
    css = data.get('css', '')
    js = data.get('js', '')

    component_json = {
        "component": {
            "template": template,
            "env": env,
            "css": css,
            "js": js
        }
    }

    return success_response(data=component_json)
