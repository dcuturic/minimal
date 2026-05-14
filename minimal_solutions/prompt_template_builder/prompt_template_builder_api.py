from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.prompt_template_builder.prompt_template_builder_validation import validate_prompt_template_builder_request

api_bp = Blueprint('prompt_template_builder_api', __name__)

@api_bp.route('/api/minimal-solutions/prompt_template_builder', methods=['POST'])
def handle_prompt_template_builder():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_prompt_template_builder_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    goal = data.get('goal', '').strip()
    variables = data.get('variables', '').strip()
    constraints = data.get('constraints', '').strip()
    
    prompt_parts = []
    
    prompt_parts.append(f"Goal:\n{goal}")
    
    if variables:
        prompt_parts.append(f"\nVariables:\n{variables}")
        
    if constraints:
        prompt_parts.append(f"\nConstraints:\n{constraints}")
        
    result = "\n".join(prompt_parts)

    return success_response(data={
        "result": result
    })
