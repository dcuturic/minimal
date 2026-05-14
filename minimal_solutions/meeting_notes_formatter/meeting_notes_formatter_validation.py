def validate_meeting_notes_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"_error": "Erwartet wurde ein JSON-Objekt/Dictionary."}
        
    if "notes" not in data:
        errors["notes"] = "Das Feld 'notes' ist erforderlich."
    elif not isinstance(data["notes"], str):
        errors["notes"] = "Das Feld 'notes' muss ein String sein."
    elif not data["notes"].strip():
        errors["notes"] = "Das Feld 'notes' darf nicht leer sein."
        
    if errors:
        return False, errors
    return True, {}
