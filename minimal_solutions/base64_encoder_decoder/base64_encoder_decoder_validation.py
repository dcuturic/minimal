def validate_base64_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt."}
        
    if "mode" not in data:
        errors["mode"] = "Das Feld 'mode' fehlt."
    elif data["mode"] not in ["encode", "decode"]:
        errors["mode"] = "Das Feld 'mode' muss 'encode' oder 'decode' sein."

    if "text" not in data:
        errors["text"] = "Das Feld 'text' fehlt."
    elif not isinstance(data["text"], str):
        errors["text"] = "Das Feld 'text' muss ein String sein."
    elif not data["text"]:
        errors["text"] = "Das Feld 'text' darf nicht leer sein."
        
    if errors:
        return False, errors
    return True, {}
