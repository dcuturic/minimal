from flask import Blueprint, request
import json
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.component_dependency_viewer.component_dependency_viewer_validation import validate_component_dependency_viewer_input

api_bp = Blueprint('component_dependency_viewer_api', __name__)

@api_bp.route('/api/minimal-solutions/component_dependency_viewer', methods=['POST'])
def handle_component_dependency_viewer_request():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )

    is_valid, errors = validate_component_dependency_viewer_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    component_json_input = data['component_json']
    
    if isinstance(component_json_input, str):
        try:
            component_data = json.loads(component_json_input)
        except json.JSONDecodeError:
            return error_response(
                code=ErrorCodes.VALIDATION_ERROR,
                message="Validierungsfehler",
                details={"component_json": "Das Feld component_json enthält kein gültiges JSON."}
            )
    else:
        component_data = component_json_input

    # Extract dependencies
    dependencies = {
        "css": [],
        "js": [],
        "env": []
    }
    
    if isinstance(component_data, dict):
        comp = component_data.get("component", component_data)
        if isinstance(comp, dict):
            if comp.get("css"):
                dependencies["css"].append("inline-css")
            if comp.get("js"):
                dependencies["js"].append("inline-js")
            if comp.get("env"):
                dependencies["env"].extend(list(comp.get("env", {}).keys()))

    return success_response(data={
        "dependencies": dependencies,
        "component_data": component_data
    })
