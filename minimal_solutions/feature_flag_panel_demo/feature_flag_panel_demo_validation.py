from typing import Tuple, Dict

def validate_feature_flag_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    flags = data.get('flags')
    
    if flags is None:
        errors['flags'] = "Das Feld 'flags' ist erforderlich."
    elif not isinstance(flags, list):
        errors['flags'] = "Das Feld 'flags' muss eine Liste von Strings sein."
    elif not all(isinstance(f, str) for f in flags):
        errors['flags'] = "Alle Elemente in 'flags' müssen Strings sein."
    elif len(flags) == 0:
        errors['flags'] = "Die Liste 'flags' darf nicht leer sein."
        
    return len(errors) == 0, errors
