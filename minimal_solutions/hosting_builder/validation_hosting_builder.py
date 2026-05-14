def validate_hosting_builder_request(data):
    errors = {}
    if not data:
        return False, {"payload": "Request body darf nicht leer sein"}
        
    if "source" not in data:
        errors["source"] = "Source wird benötigt"
        
    if "config" not in data:
        errors["config"] = "Config wird benötigt"
        
    if "mode" not in data:
        errors["mode"] = "Mode wird benötigt"
        
    if errors:
        return False, errors
        
    return True, {}
