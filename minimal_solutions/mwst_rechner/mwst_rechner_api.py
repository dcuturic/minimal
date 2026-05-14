from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.mwst_rechner.mwst_rechner_validation import validate_mwst_request

api_bp = Blueprint('mwst_rechner_api', __name__)

@api_bp.route('/api/minimal-solutions/mwst_rechner', methods=['POST'])
def calculate_mwst():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_mwst_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    amount = float(data.get('amount'))
    mode = data.get('mode')
    vat_rate = float(data.get('vat_rate'))

    if mode == 'net_to_gross':
        net_amount = amount
        vat_amount = amount * (vat_rate / 100)
        gross_amount = amount + vat_amount
    else:  # gross_to_net
        gross_amount = amount
        net_amount = amount / (1 + (vat_rate / 100))
        vat_amount = gross_amount - net_amount

    # Round to 2 decimal places
    net_amount = round(net_amount, 2)
    vat_amount = round(vat_amount, 2)
    gross_amount = round(gross_amount, 2)

    return success_response(data={
        "net_amount": net_amount,
        "vat_amount": vat_amount,
        "gross_amount": gross_amount,
        "amount": amount,
        "mode": mode,
        "vat_rate": vat_rate
    })
