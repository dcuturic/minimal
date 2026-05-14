def validate_html_fragment_wrapper_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt."}
        
    if "html" not in data:
        errors["html"] = "Das Feld 'html' fehlt."
    elif not isinstance(data["html"], str):
        errors["html"] = "Das Feld 'html' muss ein String sein."
    elif not data["html"].strip():
        errors["html"] = "Das Feld 'html' darf nicht leer sein."
        
    for field in ["css", "js", "name"]:
        if field in data and not isinstance(data[field], str):
            errors[field] = f"Das Feld '{field}' muss ein String sein."

    if errors:
        return False, errors
    return True, {}
