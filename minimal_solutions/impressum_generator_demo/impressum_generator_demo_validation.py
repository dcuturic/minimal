def validate_impressum_request(data):
    if not isinstance(data, dict):
        return False, ["Erwartet wurde ein JSON-Objekt."]
    
    errors = []
    required_fields = ['company', 'address', 'email', 'phone', 'representative']
    for field in required_fields:
        if field not in data:
            errors.append(f"Das Feld '{field}' fehlt.")
        elif not isinstance(data[field], str) or not data[field].strip():
            errors.append(f"Das Feld '{field}' muss ein nicht-leerer String sein.")
            
    if errors:
        return False, errors
    return True, []
