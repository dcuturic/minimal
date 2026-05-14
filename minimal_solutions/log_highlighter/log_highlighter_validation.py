def validate_log_highlighter_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt."}
        
    if "log_text" not in data:
        errors["log_text"] = "Das Feld 'log_text' fehlt."
    elif not isinstance(data["log_text"], str):
        errors["log_text"] = "Das Feld 'log_text' muss ein String sein."
    elif len(data["log_text"].strip()) == 0:
        errors["log_text"] = "Das Feld 'log_text' darf nicht leer sein."
        
    if errors:
        return False, errors
    return True, {}
