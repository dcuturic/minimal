def validate_iban_request(data):
    errors = {}
    if not data:
        return False, {"payload": "Invalid JSON payload"}
    
    if 'iban' not in data:
        errors['iban'] = "IBAN ist erforderlich."
    elif not isinstance(data['iban'], str):
        errors['iban'] = "IBAN muss eine Zeichenkette sein."
    elif not data['iban'].strip():
        errors['iban'] = "IBAN darf nicht leer sein."
        
    if errors:
        return False, errors
    return True, None
