from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.dns_record_builder.dns_record_builder_validation import validate_dns_record_request

api_bp = Blueprint('dns_record_builder_api', __name__)

@api_bp.route('/api/minimal-solutions/dns_record_builder', methods=['POST'])
def build_dns_record():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_dns_record_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )

    record_type = data.get('type').upper()
    name = data.get('name').strip()
    value = data.get('value').strip()
    ttl = int(data.get('ttl'))
    
    if record_type == 'TXT' and not value.startswith('"'):
        formatted_value = f'"{value}"'
    else:
        formatted_value = value
        
    # Generate BIND format string
    record = f"{name}\t{ttl}\tIN\t{record_type}\t{formatted_value}"
    
    return success_response(data={
        "record": record,
        "type": record_type,
        "name": name,
        "value": formatted_value,
        "ttl": ttl
    })
