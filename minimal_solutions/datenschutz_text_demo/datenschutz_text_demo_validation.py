# Validation für Datenschutz Text Demo
def validate_datenschutz_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt."}
        
    for field in ["uses_cookies", "uses_analytics", "uses_contact_form"]:
        if field not in data:
            errors[field] = f"Das Feld '{field}' fehlt."
        elif not isinstance(data[field], bool):
            errors[field] = f"Das Feld '{field}' muss ein Boolean sein."

    if "hosting_provider" not in data:
        errors["hosting_provider"] = "Das Feld 'hosting_provider' fehlt."
    elif not isinstance(data["hosting_provider"], str):
        errors["hosting_provider"] = "Das Feld 'hosting_provider' muss ein String sein."
    elif not data["hosting_provider"].strip():
        errors["hosting_provider"] = "Das Feld 'hosting_provider' darf nicht leer sein."
        
    if errors:
        return False, errors
    return True, {}
