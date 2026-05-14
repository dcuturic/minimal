def validate_regex_request(data):
    if not isinstance(data, dict):
        return False, ["Erwartet wurde ein JSON-Objekt/Dictionary."]
    
    errors = []
    if 'pattern' not in data:
        errors.append("Feld 'pattern' fehlt.")
    elif not isinstance(data['pattern'], str):
        errors.append("Feld 'pattern' muss ein String sein.")
    
    if 'text' not in data:
        errors.append("Feld 'text' fehlt.")
    elif not isinstance(data['text'], str):
        errors.append("Feld 'text' muss ein String sein.")
        
    if 'flags' in data and not isinstance(data['flags'], str):
        errors.append("Feld 'flags' muss ein String sein.")
        
    return len(errors) == 0, errors
