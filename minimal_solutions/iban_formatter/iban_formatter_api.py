from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.iban_formatter.iban_formatter_validation import validate_iban_request
import re

api_bp = Blueprint('iban_formatter_api', __name__)

@api_bp.route('/api/minimal-solutions/iban_formatter', methods=['POST'])
def format_iban():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_iban_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    iban_input = data.get('iban', '').strip()
    
    # Clean the IBAN (remove spaces, uppercase)
    cleaned_iban = "".join(iban_input.split()).upper()
    
    # Format the IBAN: chunks of 4 characters separated by space
    formatted_iban = " ".join([cleaned_iban[i:i+4] for i in range(0, len(cleaned_iban), 4)])
    
    # Basic validation for IBAN structure
    # Country code (2 letters), Check digits (2 digits), BBAN (up to 30 alphanumeric characters)
    is_valid_format = bool(re.match(r'^[A-Z]{2}\d{2}[A-Z0-9]{1,30}$', cleaned_iban))
    if len(cleaned_iban) > 34:
        is_valid_format = False

    return success_response(data={
        "iban": cleaned_iban,
        "formatted_iban": formatted_iban,
        "is_valid": is_valid_format
    })
