from flask import Blueprint, request
from app.responses import success_response, error_response, ErrorCodes
from minimal_solutions.status_page_incident_generator.status_page_incident_generator_validation import validate_status_page_incident_generator_request
import datetime

api_bp = Blueprint('status_page_incident_generator_api', __name__)

@api_bp.route('/api/minimal-solutions/status_page_incident_generator', methods=['POST'])
def handle_status_page_incident_generator():
    data = request.get_json(silent=True)
    if data is None:
        return error_response(
            code=ErrorCodes.BAD_REQUEST,
            message="Erwartet wurde ein JSON-Objekt/Dictionary."
        )

    is_valid, errors = validate_status_page_incident_generator_request(data)
    if not is_valid:
        return error_response(
            code=ErrorCodes.VALIDATION_ERROR,
            message="Validierungsfehler",
            details=errors
        )
        
    service = data.get('service')
    incident_type = data.get('incident_type')
    status = data.get('status')
    message = data.get('message')
    
    # Generate the standard response
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    incident = {
        "service": service,
        "incident_type": incident_type,
        "status": status,
        "message": message,
        "created_at": timestamp,
        "id": f"inc_{int(datetime.datetime.utcnow().timestamp())}"
    }
    
    formatted_text = f"[{timestamp}] INCIDENT - {service.upper()} ({status.upper()})\n"
    formatted_text += f"Type: {incident_type}\n"
    formatted_text += f"Message: {message}"
    
    result = {
        "incident": incident,
        "formatted_text": formatted_text
    }
        
    return success_response(data={"result": result})
