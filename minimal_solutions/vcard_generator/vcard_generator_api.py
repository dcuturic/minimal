from flask import Blueprint, jsonify, request
from .vcard_generator_validation import validate_request
from app.responses import success_response, error_response, ErrorCodes

api_bp = Blueprint('vcard_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/vcard_generator', methods=['POST'])
def generate_vcard():
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
    address = data.get("address", "").strip()
    
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
    if address:
        vcard_lines.append(f"ADR;TYPE=WORK,PREF:;;{address};;;;")
        
    vcard_lines.append("END:VCARD")
    vcard_string = "\n".join(vcard_lines)
    
    response_data = {
        "vcard": vcard_string
    }
    
    return success_response(data=response_data)
