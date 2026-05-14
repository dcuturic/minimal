from typing import Tuple, Dict

def validate_einheiten_converter_input(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    value = data.get('value')
    from_unit = data.get('from_unit')
    to_unit = data.get('to_unit')
    category = data.get('category')
    
    if value is None:
        errors['value'] = "Das Feld 'value' ist erforderlich."
    else:
        try:
            float(value)
        except (ValueError, TypeError):
            errors['value'] = "Das Feld 'value' muss eine Zahl sein."
            
    if not from_unit:
        errors['from_unit'] = "Das Feld 'from_unit' ist erforderlich."
    elif not isinstance(from_unit, str):
        errors['from_unit'] = "Das Feld 'from_unit' muss ein String sein."
        
    if not to_unit:
        errors['to_unit'] = "Das Feld 'to_unit' ist erforderlich."
    elif not isinstance(to_unit, str):
        errors['to_unit'] = "Das Feld 'to_unit' muss ein String sein."
        
    if not category:
        errors['category'] = "Das Feld 'category' ist erforderlich."
    elif not isinstance(category, str):
        errors['category'] = "Das Feld 'category' muss ein String sein."
        
    return len(errors) == 0, errors
