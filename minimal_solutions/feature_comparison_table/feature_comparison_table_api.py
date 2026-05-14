from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.feature_comparison_table.feature_comparison_table_validation import validate_feature_comparison_table_input

api_bp = Blueprint('feature_comparison_table_api', __name__)

@api_bp.route('/api/minimal-solutions/feature_comparison_table', methods=['POST'])
def handle_feature_comparison_table():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )

    is_valid, errors = validate_feature_comparison_table_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    # In this minimal solution, we simply validate and echo back the processed structure.
    features = data.get('features', [])
    items = data.get('items', [])
    
    return success_response(data={
        "features": features,
        "items": items
    })
