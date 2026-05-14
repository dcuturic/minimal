def validate_maintenance_page_generator_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt."}
        
    if "title" not in data:
        errors["title"] = "Das Feld 'title' fehlt."
    elif not isinstance(data["title"], str):
        errors["title"] = "Das Feld 'title' muss ein String sein."
    elif not data["title"].strip():
        errors["title"] = "Das Feld 'title' darf nicht leer sein."
        
    if "message" not in data:
        errors["message"] = "Das Feld 'message' fehlt."
    elif not isinstance(data["message"], str):
        errors["message"] = "Das Feld 'message' muss ein String sein."
    elif not data["message"].strip():
        errors["message"] = "Das Feld 'message' darf nicht leer sein."
        
    if "eta" not in data:
        errors["eta"] = "Das Feld 'eta' fehlt."
    elif not isinstance(data["eta"], str):
        errors["eta"] = "Das Feld 'eta' muss ein String sein."
        
    if errors:
        return False, errors
    return True, {}
