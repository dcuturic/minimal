def validate_html_escape_unescape_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt."}
        
    if "html_text" not in data:
        errors["html_text"] = "Das Feld 'html_text' fehlt."
    elif not isinstance(data["html_text"], str):
        errors["html_text"] = "Das Feld 'html_text' muss ein String sein."
        
    if "mode" not in data:
        errors["mode"] = "Das Feld 'mode' fehlt."
    elif data["mode"] not in ['escape', 'unescape']:
        errors["mode"] = "Ungültiger Modus. Erwartet wird 'escape' oder 'unescape'."
        
    if errors:
        return False, errors
    return True, {}
