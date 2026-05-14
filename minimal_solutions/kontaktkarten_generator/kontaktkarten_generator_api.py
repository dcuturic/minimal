from flask import Blueprint, jsonify, request
from .kontaktkarten_generator_validation import validate_request
from app.responses import success_response, error_response, ErrorCodes

api_bp = Blueprint('kontaktkarten_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/kontaktkarten_generator', methods=['POST'])
def generate_kontaktkarte():
    data = request.get_json(silent=True) or {}
    
    is_valid, errors = validate_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    phone = data.get("phone", "").strip()
    company = data.get("company", "").strip()
    website = data.get("website", "").strip()
    
    vcard_lines = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"FN:{name}",
        f"N:{name};;;;",
    ]
    
    if company:
        vcard_lines.append(f"ORG:{company}")
    if phone:
        vcard_lines.append(f"TEL;TYPE=WORK,VOICE:{phone}")
    if email:
        vcard_lines.append(f"EMAIL;TYPE=PREF,INTERNET:{email}")
    if website:
        vcard_lines.append(f"URL:{website}")
        
    vcard_lines.append("END:VCARD")
    vcard_string = "\n".join(vcard_lines)
    
    response_data = {
        "vcard": vcard_string
    }
    
    return success_response(data=response_data)
