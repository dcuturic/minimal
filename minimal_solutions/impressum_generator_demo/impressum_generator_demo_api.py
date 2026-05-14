from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.impressum_generator_demo.impressum_generator_demo_validation import validate_impressum_request

api_bp = Blueprint('impressum_generator_demo_api', __name__)

@api_bp.route('/api/minimal-solutions/impressum_generator_demo', methods=['POST'])
def handle_impressum_generator_demo():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt."
        )
        
    is_valid, errors = validate_impressum_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Validierungsfehler",
            details=errors
        )
        
    company = data.get('company', '').strip()
    address = data.get('address', '').strip()
    email = data.get('email', '').strip()
    phone = data.get('phone', '').strip()
    representative = data.get('representative', '').strip()
    
    impressum_text = (
        f"Impressum\n\n"
        f"Angaben gemäß § 5 TMG:\n"
        f"{company}\n"
        f"{address}\n\n"
        f"Vertreten durch:\n"
        f"{representative}\n\n"
        f"Kontakt:\n"
        f"Telefon: {phone}\n"
        f"E-Mail: {email}"
    )
    
    return success_response(data={
        "impressum": impressum_text
    })
