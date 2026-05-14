from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.preis_kalkulator.preis_kalkulator_validation import validate_preis_kalkulator_request

api_bp = Blueprint('preis_kalkulator_api', __name__)

@api_bp.route('/api/minimal-solutions/preis_kalkulator', methods=['POST'])
def calculate_preis():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_preis_kalkulator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    base_price = float(data['base_price'])
    margin_rate = float(data['margin'])
    discount_rate = float(data['discount'])
    markup_amount = float(data['markup'])

    margin_amount = base_price * (margin_rate / 100)
    discount_amount = base_price * (discount_rate / 100)
    final_price = base_price + margin_amount - discount_amount + markup_amount

    # Round to 2 decimal places
    margin_amount = round(margin_amount, 2)
    discount_amount = round(discount_amount, 2)
    markup_amount = round(markup_amount, 2)
    final_price = round(final_price, 2)

    return success_response(data={
        "base_price": base_price,
        "margin_amount": margin_amount,
        "discount_amount": discount_amount,
        "markup_amount": markup_amount,
        "final_price": final_price
    })
