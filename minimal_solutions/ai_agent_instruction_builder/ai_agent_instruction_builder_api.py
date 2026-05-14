from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.ai_agent_instruction_builder.ai_agent_instruction_builder_validation import validate_ai_agent_instruction_builder_request

api_bp = Blueprint('ai_agent_instruction_builder_api', __name__)

@api_bp.route('/api/minimal-solutions/ai_agent_instruction_builder', methods=['POST'])
def handle_ai_agent_instruction_builder():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_ai_agent_instruction_builder_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    agent_name = data.get('agent_name', '').strip()
    purpose = data.get('purpose', '').strip()
    tools = data.get('tools', '').strip()
    constraints = data.get('constraints', '').strip()
    
    instruction_parts = []
    instruction_parts.append(f"# System Prompt for {agent_name}\n")
    instruction_parts.append(f"## Purpose\n{purpose}\n")
    
    if tools:
        instruction_parts.append(f"## Available Tools\n{tools}\n")
        
    if constraints:
        instruction_parts.append(f"## Constraints & Rules\n{constraints}\n")
        
    result = "\n".join(instruction_parts).strip()

    return success_response(data={
        "result": result
    })
