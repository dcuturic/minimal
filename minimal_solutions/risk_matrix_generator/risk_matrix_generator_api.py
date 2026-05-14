from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.risk_matrix_generator.risk_matrix_generator_validation import validate_risk_matrix_request

api_bp = Blueprint('risk_matrix_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/risk_matrix_generator', methods=['POST'])
def generate_risk_matrix():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_risk_matrix_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    risks_input = data.get('risks')
    
    matrix_output = "--- RISK MATRIX ---\n\n"
    
    if isinstance(risks_input, list):
        for i, r in enumerate(risks_input, 1):
            if isinstance(r, dict):
                name = r.get("name", "Unknown Risk")
                prob = r.get("probability", "Unknown")
                impact = r.get("impact", "Unknown")
                matrix_output += f"[{i}] {name}\n    Probability: {prob} | Impact: {impact}\n\n"
            else:
                matrix_output += f"[{i}] {str(r)}\n\n"
    else:
        # It's a string
        lines = risks_input.splitlines()
        for i, line in enumerate(lines, 1):
            if line.strip():
                matrix_output += f"- {line.strip()}\n"

    matrix_output += "-------------------"

    return success_response(data={"matrix": matrix_output})
