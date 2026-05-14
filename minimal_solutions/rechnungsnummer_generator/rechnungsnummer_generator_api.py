from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.rechnungsnummer_generator.rechnungsnummer_generator_validation import validate_rechnungsnummer_request

api_bp = Blueprint('rechnungsnummer_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/rechnungsnummer_generator', methods=['POST'])
def generate_rechnungsnummer():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )

    is_valid, errors = validate_rechnungsnummer_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    prefix = data.get('prefix', '')
    year = data.get('year', '')
    start_number = int(data.get('start_number', 1))
    count = int(data.get('count', 1))

    numbers = []
    for i in range(count):
        current_num = start_number + i
        # Format: PREFIX-YEAR-NUMBER (e.g. RE-2026-0001)
        # We can pad the number to 4 digits or dynamic depending on requirement.
        # Minimal solution standard: let's pad to 4 digits.
        number_str = f"{prefix}-{year}-{current_num:04d}" if prefix and year else \
                     f"{prefix}-{current_num:04d}" if prefix else \
                     f"{year}-{current_num:04d}" if year else \
                     f"{current_num:04d}"
        numbers.append(number_str)

    pattern = f"{prefix + '-' if prefix else ''}{year + '-' if year else ''}[Number(4 digits)]"
    return success_response(data={"numbers": numbers, "pattern": pattern, "count": len(numbers)})
