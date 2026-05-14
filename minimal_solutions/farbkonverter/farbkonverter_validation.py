from typing import Tuple, Dict

def validate_color_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    color_value = data.get('color_value')
    
    if color_value is None:
        errors['color_value'] = "Das Feld 'color_value' ist erforderlich."
    elif not isinstance(color_value, str) or str(color_value).strip() == "":
        errors['color_value'] = "Das Feld 'color_value' darf nicht leer sein und muss ein String sein."
        
    return len(errors) == 0, errors
