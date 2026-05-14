from typing import Tuple, Dict

def validate_timestamp_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    mode = data.get('mode')
    value = data.get('value')
    
    if not mode:
        errors['mode'] = "Das Feld 'mode' ist erforderlich."
    elif mode not in ['timestamp_to_date', 'date_to_timestamp']:
        errors['mode'] = "Das Feld 'mode' muss 'timestamp_to_date' oder 'date_to_timestamp' sein."
        
    if value is None:
        errors['value'] = "Das Feld 'value' ist erforderlich."
    elif str(value).strip() == "":
        errors['value'] = "Das Feld 'value' darf nicht leer sein."
        
    return len(errors) == 0, errors
