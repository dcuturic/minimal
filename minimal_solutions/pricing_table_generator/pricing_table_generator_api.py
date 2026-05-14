from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.pricing_table_generator.pricing_table_generator_validation import validate_pricing_table_generator_input

api_bp = Blueprint('pricing_table_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/pricing_table_generator', methods=['POST'])
def generate_pricing_table():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_pricing_table_generator_input(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    plans = data.get('plans', [])

    result_plans = []
    for plan in plans:
        processed_plan = {
            "name": str(plan.get("name", "")).strip(),
            "price": str(plan.get("price", "0")).strip(),
            "currency": str(plan.get("currency", "$")).strip() if plan.get("currency") else "$",
            "period": str(plan.get("period", "/mo")).strip() if plan.get("period") else "/mo",
            "features": plan.get("features", []) if isinstance(plan.get("features"), list) else [],
            "is_popular": bool(plan.get("is_popular", False)),
            "button_text": str(plan.get("button_text", "Select Plan")).strip() if plan.get("button_text") else "Select Plan"
        }
        result_plans.append(processed_plan)

    return success_response(data={"result": result_plans})
