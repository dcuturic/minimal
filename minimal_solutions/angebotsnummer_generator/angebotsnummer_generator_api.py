from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.angebotsnummer_generator.angebotsnummer_generator_validation import validate_angebotsnummer_request

api_bp = Blueprint('angebotsnummer_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/angebotsnummer_generator', methods=['POST'])
def generate():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_angebotsnummer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    prefix = data.get('prefix')
    date = data.get('date')
    customer_short = data.get('customer_short')
    number = data.get('number')
    
    # Format the number: zero-pad if integer or numeric string
    if isinstance(number, int):
        formatted_number = f"{number:03d}"
    elif isinstance(number, str) and number.isdigit():
        formatted_number = f"{int(number):03d}"
    else:
        formatted_number = str(number)

    parts = [p for p in [prefix, date, customer_short, formatted_number] if p]
    angebotsnummer = "-".join(parts)

    pattern_parts = []
    if prefix: pattern_parts.append("[Prefix]")
    if date: pattern_parts.append("[Date]")
    if customer_short: pattern_parts.append("[Customer]")
    pattern_parts.append("[Number]")
    pattern = "-".join(pattern_parts)

    return success_response(data={
        "numbers": [angebotsnummer],
        "pattern": pattern,
        "prefix": prefix,
        "date": date,
        "customer_short": customer_short,
        "number": number
    })
