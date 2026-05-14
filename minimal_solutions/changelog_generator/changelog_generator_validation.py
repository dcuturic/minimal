def validate_changelog_generator_request(data):
    errors = {}
    if not isinstance(data, dict):
        return False, {"payload": "Erwartet wurde ein JSON-Objekt."}
        
    if "version" not in data:
        errors["version"] = "Das Feld 'version' fehlt."
    elif not isinstance(data["version"], str) or not data["version"].strip():
        errors["version"] = "Das Feld 'version' muss ein nicht-leerer String sein."
        
    if "date" not in data:
        errors["date"] = "Das Feld 'date' fehlt."
    elif not isinstance(data["date"], str) or not data["date"].strip():
        errors["date"] = "Das Feld 'date' muss ein nicht-leerer String sein."

    if "changes" not in data:
        errors["changes"] = "Das Feld 'changes' fehlt."
    elif not isinstance(data["changes"], (str, list)):
        errors["changes"] = "Das Feld 'changes' muss ein String oder eine Liste sein."
    elif isinstance(data["changes"], str) and not data["changes"].strip():
        errors["changes"] = "Das Feld 'changes' darf nicht leer sein."
    elif isinstance(data["changes"], list) and not data["changes"]:
        errors["changes"] = "Die Liste 'changes' darf nicht leer sein."
        
    if errors:
        return False, errors
    return True, {}
