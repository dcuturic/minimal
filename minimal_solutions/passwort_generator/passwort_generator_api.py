from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.passwort_generator.passwort_generator_validation import validate_password_request
import string
import secrets

api_bp = Blueprint('passwort_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/passwort_generator', methods=['POST'])
def generate_password():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_password_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    length = data.get('length')
    use_numbers = data.get('use_numbers', False)
    use_symbols = data.get('use_symbols', False)
    use_uppercase = data.get('use_uppercase', False)

    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    password = []
    if use_uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))
    
    # Fill the rest with random choices from the allowed character set
    while len(password) < length:
        password.append(secrets.choice(chars))
        
    # Shuffle to avoid predictable patterns at the beginning
    secrets.SystemRandom().shuffle(password)
    # Truncate to desired length in case required characters exceeded the length (though minimum length check should prevent this)
    password_str = ''.join(password)[:length]

    return success_response(data={"password": password_str})
