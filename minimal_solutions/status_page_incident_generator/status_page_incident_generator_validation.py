from typing import Tuple, Dict

def validate_status_page_incident_generator_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    service = data.get('service')
    incident_type = data.get('incident_type')
    status = data.get('status')
    message = data.get('message')
    
    if not service:
        errors['service'] = "Das Feld 'service' ist erforderlich."
    elif not isinstance(service, str):
        errors['service'] = "Das Feld 'service' muss ein String sein."
        
    if not incident_type:
        errors['incident_type'] = "Das Feld 'incident_type' ist erforderlich."
    elif not isinstance(incident_type, str):
        errors['incident_type'] = "Das Feld 'incident_type' muss ein String sein."
        
    if not status:
        errors['status'] = "Das Feld 'status' ist erforderlich."
    elif not isinstance(status, str):
        errors['status'] = "Das Feld 'status' muss ein String sein."
        
    if not message:
        errors['message'] = "Das Feld 'message' ist erforderlich."
    elif not isinstance(message, str):
        errors['message'] = "Das Feld 'message' muss ein String sein."
        
    return len(errors) == 0, errors
