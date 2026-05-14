def validate_hosting_preview_request(data):
    errors = {}
    if not data:
        return False, {"payload": "Request body darf nicht leer sein"}
        
    if "source" not in data:
        errors["source"] = "Source wird benötigt"
        
    if errors:
        return False, errors
        
    return True, {}
