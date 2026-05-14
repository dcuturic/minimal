from typing import Tuple, Dict

def validate_url_request(data: dict) -> Tuple[bool, Dict[str, str]]:
    errors = {}
    
    if not isinstance(data, dict):
        return False, {"request": "Invalid JSON format"}
        
    mode = data.get('mode')
    text = data.get('text')
    
    if not mode:
        errors['mode'] = "Das Feld 'mode' ist erforderlich."
    elif mode not in ['encode', 'decode']:
        errors['mode'] = "Das Feld 'mode' muss 'encode' oder 'decode' sein."
        
    if text is None:
        errors['text'] = "Das Feld 'text' ist erforderlich."
    elif not isinstance(text, str):
        errors['text'] = "Das Feld 'text' muss ein String sein."
    elif len(text) == 0:
        errors['text'] = "Das Feld 'text' darf nicht leer sein."
        
    return len(errors) == 0, errors
